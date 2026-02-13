import json
import os
import requests
from datetime import datetime, timedelta
from dateutil import parser
import re
import time
from bs4 import BeautifulSoup

# --- 配置区 ---
DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.json')

# 只关注重要公司的模型关键词和API映射
MODEL_PATTERNS = {
    "OpenAI": {
        "keywords": ["gpt", "chatgpt", "o1", "o3", "davinci", "curie", "babbage", "ada"],
        "api_endpoints": ["https://api.github.com/repos/openai/openai-python/releases"],
        "official_sites": ["https://openai.com/blog/rss.xml"]
    },
    "Anthropic": {
        "keywords": ["claude", "sonnet", "opus", "haiku"],
        "api_endpoints": ["https://api.github.com/repos/anthropics/anthropic-sdk-python/releases"],
        "official_sites": ["https://www.anthropic.com/news.rss"]
    },
    "Google": {
        "keywords": ["gemini", "palm", "lamda", "pathways"],
        "api_endpoints": ["https://api.github.com/repos/google/generative-ai-python/releases"],
        "official_sites": ["https://blog.google/technology/ai/rss/"]
    },
    "Meta": {
        "keywords": ["llama", "code llama", "purple llama"],
        "api_endpoints": ["https://api.github.com/repos/facebookresearch/llama/releases"],
        "official_sites": ["https://ai.meta.com/blog/rss/"]
    },
    "xAI": {
        "keywords": ["grok"],
        "api_endpoints": [],
        "official_sites": []
    },
    "DeepSeek": {
        "keywords": ["deepseek"],
        "api_endpoints": ["https://api.github.com/repos/deepseek-ai/DeepSeek-LLM/releases"],
        "official_sites": []
    },
    "Alibaba": {
        "keywords": ["qwen", "通义", "tongyi"],
        "api_endpoints": ["https://api.github.com/repos/QwenLM/Qwen/releases"],
        "official_sites": []
    },
    "Moonshot": {
        "keywords": ["kimi", "moonshot"],
        "api_endpoints": [],
        "official_sites": []
    },
    "ByteDance": {
        "keywords": ["doubao", "豆包", "bytedance"],
        "api_endpoints": [],
        "official_sites": []
    }
}

class IntelligentModelTracker:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
    def load_existing_data(self):
        """加载现有数据"""
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def save_data(self, data):
        """保存数据到文件"""
        # 按日期排序，最新的在前面
        data.sort(key=lambda x: datetime.strptime(x['update_date'], '%Y-%m-%d'), reverse=True)
        
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    
    def fetch_github_releases(self, repo_url):
        """从GitHub API获取最新发布信息"""
        try:
            response = self.session.get(repo_url, timeout=10)
            if response.status_code == 200:
                releases = response.json()
                return releases[:5]  # 只取最新的5个发布
        except Exception as e:
            print(f"获取GitHub发布信息失败: {repo_url}, 错误: {e}")
        return []
    
    def extract_model_info_from_github(self, release, company):
        """从GitHub发布信息中提取模型信息"""
        try:
            # 解析发布日期
            published_at = parser.parse(release['published_at']).strftime('%Y-%m-%d')
            
            # 提取模型名称（从name或tag_name）
            model_name = release.get('name', release.get('tag_name', 'Unknown'))

            # 如果模型名称仅仅是版本号，则跳过
            if re.fullmatch(r'v?(\d+\.)*\d+', model_name):
                return None
            
            # 清理模型名称
            cleaned_model_name = re.sub(r'^v?(\d+\.)*\d+', '', model_name).strip('-').strip()
            
            if not cleaned_model_name:
                cleaned_model_name = model_name

            # 提取特性描述
            features = release.get('body', '')[:500]  # 限制长度

            # 检查标题或特性描述是否包含关键字，增加相关性
            title_and_features = f"{cleaned_model_name} {features}"
            if not any(keyword.lower() in title_and_features.lower() for keyword in MODEL_PATTERNS[company]['keywords']):
                 return None
            
            return {
                "company": company,
                "model_name": cleaned_model_name,
                "update_date": published_at,
                "blog_url": "",
                "license_type": "unknown",
                "features": features,
            }
        except Exception as e:
            print(f"解析GitHub发布信息失败: {e}")
        return None
    
    def is_today_update(self, update_date):
        """检查是否为今天发布的更新"""
        try:
            update_dt = datetime.strptime(update_date, '%Y-%m-%d')
            today = datetime.now().date()
            return update_dt.date() == today
        except:
            return False
    
    def is_duplicate(self, new_item, existing_data):
        """检查是否为重复数据"""
        for item in existing_data:
            # 检查模型名称和公司是否相同
            if (item.get('company') == new_item.get('company') and 
                item.get('model_name') == new_item.get('model_name')):
                return True
        
        return False
    
    def fetch_official_rss_updates(self):
        """从官方RSS源获取AI模型更新信息"""
        import feedparser
        
        updates = []
        for company, info in MODEL_PATTERNS.items():
            for rss_url in info.get('official_sites', []):
                try:
                    print(f"  正在检查 {company} 官方RSS...")
                    feed = feedparser.parse(rss_url)
                    
                    for entry in feed.entries[:5]:  # 只取最新5条
                        title_lower = entry.title.lower()
                        summary_lower = entry.get('summary', '').lower()
                        
                        # 检查是否包含模型相关关键词
                        if any(keyword.lower() in title_lower or keyword.lower() in summary_lower 
                               for keyword in info['keywords']):
                            # 检查是否为模型发布相关
                            if any(word in title_lower for word in ['release', 'launch', 'announce', 'unveil', 'introduce', 'available', 'new']):
                                published_date = entry.get('published_parsed')
                                if published_date:
                                    update_date = time.strftime('%Y-%m-%d', published_date)
                                else:
                                    update_date = datetime.now().strftime('%Y-%m-%d')
                                
                                # 只要今天发布的
                                if self.is_today_update(update_date):
                                    updates.append({
                                        "company": company,
                                        "model_name": entry.title,
                                        "update_date": update_date,
                                        "blog_url": entry.get('link', ''),
                                        "license_type": "unknown",
                                        "features": entry.get('summary', '')[:300],
                                    })
                                    print(f"    ✅ 发现今日官方发布: {entry.title}")
                except Exception as e:
                    print(f"    ❌ 获取 {company} RSS失败: {e}")
                    continue
        
        return updates
    
    def fetch_all_updates(self):
        """获取所有来源的今日更新"""
        today_str = datetime.now().strftime('%Y-%m-%d')
        print(f"🤖 开始抓取 {today_str} 的AI模型更新...")
        print("📋 关注公司: OpenAI, Anthropic, Google, Meta, xAI, DeepSeek, Alibaba(Qwen), Moonshot(Kimi), ByteDance(豆包)")
        
        existing_data = self.load_existing_data()
        new_updates = []
        
        # 1. 从官方RSS源获取更新
        print("\n📰 正在从官方RSS源获取今日更新...")
        rss_updates = self.fetch_official_rss_updates()
        for update in rss_updates:
            if not self.is_duplicate(update, existing_data + new_updates):
                new_updates.append(update)
        
        # 2. 从GitHub获取更新
        print("\n📦 正在从GitHub获取今日更新...")
        for company, info in MODEL_PATTERNS.items():
            for api_endpoint in info['api_endpoints']:
                print(f"  正在检查 {company} GitHub...")
                releases = self.fetch_github_releases(api_endpoint)
                for release in releases:
                    model_info = self.extract_model_info_from_github(release, company)
                    if (model_info and 
                        self.is_today_update(model_info['update_date']) and
                        not self.is_duplicate(model_info, existing_data + new_updates)):
                        new_updates.append(model_info)
                        print(f"    ✅ 发现今日GitHub发布: {model_info['model_name']}")
        
        # 4. 保存更新
        if new_updates:
            print(f"\n🎉 发现 {len(new_updates)} 个今日新发布的模型，正在保存...")
            all_data = existing_data + new_updates
            self.save_data(all_data)
            print("✅ 数据已成功更新到 data.json")
            
            # 打印新更新摘要
            print(f"\n📋 {today_str} 新发布模型摘要:")
            for update in new_updates:
                print(f"  • {update['company']}: {update['model_name']} (来源: {update['source']})")
        else:
            print(f"ℹ️  {today_str} 暂未发现指定公司的新模型发布")

def fetch_updates():
    """主函数：智能抓取AI模型更新"""
    tracker = IntelligentModelTracker()
    tracker.fetch_all_updates()

if __name__ == "__main__":
    fetch_updates()