import json
import os
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

# 加载环境变量 (用于本地开发)
load_dotenv()

# --- 配置区 ---
DATA_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'docs', 'data.json')

# 从环境变量获取配置
# 如果使用 OpenAI，API_KEY 存在 GitHub Secrets 的 OPENAI_API_KEY
# 如果使用 Perplexity (推荐用于搜索)，BASE_URL 为 https://api.perplexity.ai
API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("LLM_MODEL", "gpt-4o") # 如果是 Perplexity，改为 sonar 等模型

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

def load_existing_data():
    """加载现有数据"""
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(data):
    """保存数据到文件"""
    # 按日期排序，最新的在前面
    data.sort(key=lambda x: datetime.strptime(x['update_date'], '%Y-%m-%d'), reverse=True)
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def get_updates_from_llm(existing_models):
    """调用支持搜索的 LLM 获取更新信息"""
    today = datetime.now().strftime('%Y-%m-%d')
    
    # 构造 Prompt
    # existing_models 用于告诉 LLM 哪些我们已经知道了，避免重复
    prompt = f"""
    今天是 {today}。你是一个专业的 AI 行业分析师，负责追踪全球大语言模型（LLM）的最新发布和重大更新。
    
    请搜索并列出在 {today}（或最近 24 小时内）新发布的模型或重大版本更新。
    
    重点关注：OpenAI, Anthropic, Google, Meta, xAI, DeepSeek, 智谱AI, 阿里巴巴(Qwen), 字节跳动, 腾讯, MiniMax, 月之暗面(Kimi) 等。
    
    目前我们已有的模型列表（部分）: {', '.join(existing_models[:5])}...
    
    请返回一个 JSON 数组，格式如下：
    [
        {{
            "company": "公司名称",
            "model_name": "模型准确名称",
            "update_date": "YYYY-MM-DD",
            "blog_url": "官方公告或技术博客链接",
            "license_type": "open_source 或 closed_source",
            "features_zh": "中文特性简述（50字以内）",
            "features_en": "English features summary (short)"
        }}
    ]
    
    注意：
    1. 必须是真实的发布，严禁编造。
    2. 如果今天没有新模型发布，请返回空数组 []。
    3. 只要返回 JSON，不要包含任何其他文字说明。
    """

    print(f"正在调用 LLM 搜索今日更新 (Model: {MODEL_NAME})...")
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "你是一个只输出 JSON 的 AI 助手。"},
                {"role": "user", "content": prompt}
            ],
            # 开启 JSON 模式 (如果供应商支持)
            response_format={"type": "json_object"} if "gpt" in MODEL_NAME else None
        )
        
        content = response.choices[0].message.content
        # 尝试解析结果
        # 有些非 OpenAI 模型可能会在内容前后加 ```json ... ```
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0]
        elif "```" in content:
            content = content.split("```")[1].split("```")[0]
            
        result = json.loads(content)
        # 如果返回的是 {"updates": [...]} 这种格式，提取数组
        if isinstance(result, dict) and "updates" in result:
            return result["updates"]
        return result if isinstance(result, list) else []

    except Exception as e:
        print(f"❌ 调用 LLM 失败: {e}")
        return []

def is_duplicate(new_item, existing_data):
    """简单去重逻辑"""
    for item in existing_data:
        if (item['company'].lower() == new_item['company'].lower() and 
            item['model_name'].lower() == new_item['model_name'].lower()):
            return True
    return False

def main():
    existing_data = load_existing_data()
    existing_model_names = [item['model_name'] for item in existing_data]
    
    new_updates = get_updates_from_llm(existing_model_names)
    
    if not new_updates:
        print("ℹ️ 今日未发现新模型发布。")
        return

    added_count = 0
    for update in new_updates:
        if not is_duplicate(update, existing_data):
            existing_data.append(update)
            added_count += 1
            print(f"✅ 发现新模型: {update['company']} - {update['model_name']}")
    
    if added_count > 0:
        save_data(existing_data)
        print(f"🎉 成功添加 {added_count} 条新更新！数据已保存到 docs/data.json")
    else:
        print("ℹ️ 发现的更新均已在数据库中。")

if __name__ == "__main__":
    main()
