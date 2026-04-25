import streamlit as st
import os
from utils.file_parser import parse_uploaded_file
from utils.llm_client import analyze_resume, optimize_resume
from utils.exporter import export_to_markdown, export_to_docx, export_to_pdf

# 页面配置
st.set_page_config(page_title="简历优化 Agent", page_icon="📄", layout="wide")
st.title("📄 AI 简历优化 Agent")
st.subheader("智能匹配岗位JD，一键优化简历")

# 初始化会话状态
if "resume_text" not in st.session_state:
    st.session_state.resume_text = ""
if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = ""
if "optimized_resume" not in st.session_state:
    st.session_state.optimized_resume = ""

# 1. 简历输入模块
st.divider()
st.header("1. 输入你的简历")
input_mode = st.radio("选择简历输入方式", ["上传文件", "粘贴文本"])

if input_mode == "上传文件":
    uploaded_file = st.file_uploader("上传简历（PDF/DOCX/MD/TXT）", type=["pdf", "docx", "md", "txt"])
    if uploaded_file:
        st.session_state.resume_text = parse_uploaded_file(uploaded_file)
        st.success("文件解析成功！")
else:
    st.session_state.resume_text = st.text_area("粘贴简历文本", height=200)

# 2. JD输入模块
st.divider()
st.header("2. 输入目标岗位 JD")
jd_text = st.text_area("粘贴目标职位描述（JD）", height=150)

# 3. 分析模块
st.divider()
st.header("3. 简历匹配分析")
if st.button("🔍 开始分析匹配度"):
    if not st.session_state.resume_text:
        st.error("请先输入简历内容！")
    elif not jd_text:
        st.error("请输入目标岗位JD！")
    else:
        with st.spinner("正在分析..."):
            st.session_state.analysis_result = analyze_resume(st.session_state.resume_text, jd_text)
            st.success("分析完成！")

if st.session_state.analysis_result:
    st.markdown("### 📊 匹配分析报告")
    st.write(st.session_state.analysis_result)

# 4. 优化生成模块
st.divider()
st.header("4. 生成优化简历")
confirm = st.checkbox("我确认基于原始简历事实生成优化版")
if st.button("🚀 生成优化简历") and confirm and st.session_state.analysis_result:
    with st.spinner("正在生成优化简历..."):
        st.session_state.optimized_resume = optimize_resume(
            st.session_state.resume_text, jd_text, st.session_state.analysis_result
        )
    st.success("优化简历生成完成！")

if st.session_state.optimized_resume:
    st.markdown("### ✅ 优化后的简历")
    st.markdown(st.session_state.optimized_resume)

    st.divider()
    st.header("5. 导出优化简历")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.download_button(
            label="导出 MD",
            data=export_to_markdown(st.session_state.optimized_resume),
            file_name="优化简历.md",
            mime="text/markdown"
        )
    with col2:
        doc_bytes = export_to_docx(st.session_state.optimized_resume)
        st.download_button(
            label="导出 DOCX",
            data=doc_bytes,
            file_name="优化简历.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
    with col3:
        pdf_bytes = export_to_pdf(st.session_state.optimized_resume)
        st.download_button(
            label="导出 PDF",
            data=pdf_bytes,
            file_name="优化简历.pdf",
            mime="application/pdf"
        )
    