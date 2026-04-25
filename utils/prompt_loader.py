import os

# 获取项目根目录
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PROMPT_DIR = os.path.join(BASE_DIR, "prompts")

def load_prompt(file_name: str) -> str:
    """读取 prompts 目录下的 md 提示词文件"""
    file_path = os.path.join(PROMPT_DIR, file_name)
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        raise RuntimeError(f"读取提示词文件失败 {file_name}：{str(e)}")

# 全局加载两个提示词
ANALYZE_PROMPT = load_prompt("analyze_resume_prompt.md")
OPTIMIZE_PROMPT = load_prompt("optimize_resume_prompt.md")