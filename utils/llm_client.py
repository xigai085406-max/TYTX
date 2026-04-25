# 替换 utils/llm_client.py 全部内容
import os
import requests
from dotenv import load_dotenv

load_dotenv()
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"

def get_llm_response(system_prompt, user_prompt):
    """调用 DeepSeek API 获取回复"""
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.3
    }

    try:
        # 👇 这是修复的核心代码
        response = requests.post(DEEPSEEK_API_URL, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"LLM 调用失败：{str(e)}"

def analyze_resume(resume_text, jd_text):
    """分析简历与 JD 匹配度"""
    system_prompt = """
    你是专业的简历优化顾问，严格基于原始简历事实分析，不虚构信息。
    输出格式：
    1. 匹配亮点（3-5条，贴合JD）
    2. 主要缺口（2-3条，客观差距）
    3. 具体优化建议（可落地修改建议）
    语言简洁专业，使用中文。
    """
    user_prompt = f"简历内容：{resume_text}\n目标JD：{jd_text}\n请分析匹配度"
    return get_llm_response(system_prompt, user_prompt)

def optimize_resume(resume_text, jd_text, analysis):
    """生成优化后的简历"""
    system_prompt = """
    你是专业简历优化师，基于原始简历事实+JD要求优化简历。
    规则：
    1. 不虚构任何经历、技能、项目
    2. 优化措辞、突出关键词、贴合JD
    3. 输出标准markdown格式简历
    4. 结构清晰：个人信息、求职意向、专业技能、项目经历、教育背景
    """
    user_prompt = f"原始简历：{resume_text}\nJD：{jd_text}\n分析报告：{analysis}\n生成优化简历"
    return get_llm_response(system_prompt, user_prompt)