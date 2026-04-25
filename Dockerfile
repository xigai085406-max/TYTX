# 基础镜像：轻量级Python3.11
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 安装系统依赖（解决中文/字体问题）
RUN apt-get update && apt-get install -y --no-install-recommends \
    fonts-wqy-zenhei \
    && rm -rf /var/lib/apt/lists/*

# 复制依赖文件
COPY requirements.txt .

# 安装Python依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制全部项目代码
COPY . .

# 暴露Streamlit默认端口
EXPOSE 8501

# 启动命令（关键：设置0.0.0.0允许外部访问）
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8501"]