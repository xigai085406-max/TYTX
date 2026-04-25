import os
import requests
from dotenv import load_dotenv
from utils.prompt_loader import ANALYZE_PROMPT, OPTIMIZE_PROMPT

load_dotenv()
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"

def get_llm_response(system_prompt, user_prompt):
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
        "temperature": 0.3,
        "max_tokens": 4096
    }
    try:
        response = requests.post(DEEPSEEK_API_URL, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"LLM 调用异常：{str(e)}"

def analyze_resume(resume_text, jd_text):
    user_prompt = f"""**职位描述（JD）：**
{jd_text}

**简历内容：**
{resume_text}"""
    return get_llm_response(ANALYZE_PROMPT, user_prompt)

def optimize_resume(resume_text, jd_text, analysis):
    user_prompt = f"""**原始简历：**
{resume_text}

**目标岗位 JD：**
{jd_text}

**匹配分析报告：**
{analysis}"""
    return get_llm_response(OPTIMIZE_PROMPT, user_prompt)