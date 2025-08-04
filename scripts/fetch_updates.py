import feedparser
import json
import os
from datetime import datetime
import time

# --- 配置区 ---
# 在这里添加您想追踪的 RSS 订阅源
RSS_FEEDS = {
    # --- 国际厂商 ---
    "OpenAI": "https://openai.com/blog/rss.xml",
    "Google AI": "https://blog.google/technology/ai/rss/",
    "Anthropic": "https://www.anthropic.com/news.rss",
    "Meta AI": "https://ai.meta.com/blog/rss/",

    # --- 国内厂商 (部分源可能需要验证) ---
    "智谱AI": "https://www.zhipuai.cn/news/rss.xml", # 智谱AI官方新闻RSS
    "阿里通义千问 (ModelScope)": "https://www.modelscope.cn/rss.xml", # 魔搭社区作为阿里的信息源代理
    "月之暗面 (Kimi)": "", # 官方暂未发现明确的RSS源，可以后续补充
    "DeepSeek": "", # 官方暂未发现明确的RSS源，可以后续补充
    "零一万物": "", # 官方暂未发现明确的RSS源，可以后续补充
    "MiniMax": "", # 官方暂未发现明确的RSS源，可以后续补充

    # --- 行业资讯 ---
    "InfoQ China AI": "https://www.infoq.cn/topic/AI-ML?sort=newest&type=feed", # InfoQ中国的AI频道
    "新智元": "https://www.sohu.com/a/rss", # 新智元在搜狐的RSS源
}

# 用于在文章标题或摘要中识别模型更新的关键词
MODEL_KEYWORDS = [
    # 国际模型
    "gpt", "gemini", "claude", "llama", "sonnet", "opus", "flash", "grok",
    # 国内模型
    "qwen", "通义", "kimi", "moonshot", "deepseek", "glm", "智谱", "yi-", "零一万物", "minimax", "海螺", "百川", "baichuan", "step", "跃问"
]

DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.json')

def parse_entry_for_model_update(entry, company):
    """
    尝试解析一篇文章，判断它是否为模型更新。
    这是最具挑战性的部分，可能需要为每个信息源定制逻辑。
    如果认为是更新，则返回包含模型信息的字典，否则返回 None。
    """
    title_lower = entry.title.lower()
    
    # 简单的关键词检查
    if any(keyword in title_lower for keyword in MODEL_KEYWORDS):
        # 发现潜在匹配，开始提取信息
        model_name = entry.title  # 模型名称通常在标题中，这里做一个简单猜测
        
        # 获取发布日期
        update_date_parsed = entry.get("published_parsed") or entry.get("updated_parsed")
        if update_date_parsed:
            update_date = time.strftime('%Y-%m-%d', update_date_parsed)
        else:
            update_date = datetime.now().strftime('%Y-%m-%d')

        # 使用摘要作为特性描述
        features = entry.get("summary", "")

        return {
            "company": company,
            "model_name": model_name,
            "update_date": update_date,
            "features": features,
            "link": entry.link  # 使用链接来检查和避免重复
        }
        
    return None

def fetch_updates():
    """从 RSS 源抓取更新并更新 data.json。"""
    print("开始抓取更新...")
    
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []
        
    existing_links = {item.get('link') for item in existing_data if item.get('link')}
    new_updates_found = False
    
    for company, url in RSS_FEEDS.items():
        print(f"正在从 {url} 为 {company} 抓取信息...")
        feed = feedparser.parse(url)
        
        for entry in feed.entries:
            if entry.link in existing_links:
                continue  # 跳过已处理的条目
            
            model_update = parse_entry_for_model_update(entry, company)
            
            if model_update:
                print(f"  发现潜在的新模型更新: {model_update['model_name']}")
                existing_data.append(model_update)
                existing_links.add(model_update['link'])
                new_updates_found = True

    if new_updates_found:
        print("发现新更新，正在写入 data.json...")
        existing_data.sort(key=lambda x: datetime.strptime(x['update_date'], '%Y-%m-%d'), reverse=True)
        
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(existing_data, f, indent=4, ensure_ascii=False)
        print("data.json 更新成功。")
    else:
        print("未发现新更新。")

if __name__ == "__main__":
    fetch_updates()