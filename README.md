# 简历优化智能 Agent

## 项目简介

本项目为简历优化智能 Agent，基于 Python + Streamlit + DeepSeek LLM 开发。  
实现简历文件解析、JD 岗位匹配分析、简历合规优化、多格式文件导出完整流程。

项目严格遵循开发规范：
- 大模型 Key 通过环境变量配置，无硬编码；
- 提示词与业务代码完全解耦，独立 MD 文件管理；
- 优化内容严格忠于原始简历事实，禁止虚构经历；
- 采用模块化 Agent 架构，包含上下文工程、会话记忆、工具执行器；
- 全量支持 Docker 容器化构建与一键部署，开箱即用。

## 技术栈

Python、Streamlit、DeepSeek LLM API、Docker、PyPDF2、python-docx、reportlab

## 快速部署指南

### 1. 项目克隆

```bash
git clone https://github.com/xxx/resume-optimizer-agent.git
cd resume-optimizer-agent

```

### 2. 环境变量配置
复制环境变量模板
```bash
cp .env.example .env
```
编辑 .env 文件，填入合法 DeepSeek API Key：
```env
DEEPSEEK_API_KEY = sk-....
```

### 3. Docker 构建镜像
项目根目录执行，自动安装系统依赖与 Python 依赖
```bash
docker-compose build
```

### 4. 启动应用服务
```bash
docker-compose up -d
```
服务后台常驻运行
本地 8501 端口映射容器服务端口

### 5. 访问应用
浏览器直接打开链接即可进入系统：
```text
http://localhost:8501
```

## 功能使用流程
简历录入：支持上传 PDF/DOCX/MD/TXT 文件 或 直接粘贴简历文本；

JD 录入：粘贴目标岗位职位描述；

匹配分析：点击分析按钮，自动生成 JD 逐项匹配表、短板诊断、ATS 关键词清单、优化优先级方案；

简历优化：确认后，AI 严格依照分析报告建议优化简历，附带修改对照表；

文件导出：支持 Markdown / Word / PDF 三种格式导出，PDF 中文无乱码，可直接打开使用。




