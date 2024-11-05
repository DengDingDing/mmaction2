# 使用仅支持 CPU 的 PyTorch 基础镜像
ARG PYTORCH="1.8.1"
FROM pytorch/pytorch:${PYTORCH}-cpu

# 设置 CMake 环境变量路径，帮助 CMake 找到 Conda 环境中的库
ENV CMAKE_PREFIX_PATH="$(dirname $(which conda))/../"

# 安装必要的依赖
RUN apt-get update && apt-get install -y git ninja-build libglib2.0-0 libsm6 libxrender-dev libxext6 ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 安装 MMCV 及其他依赖
RUN pip install openmim
RUN mim install mmengine "mmcv<2.2.0"  # 选择兼容版本的 mmcv

# 安装 MMAction2
RUN conda clean --all
RUN git clone https://github.com/open-mmlab/mmaction2.git /mmaction2
WORKDIR /mmaction2
RUN mkdir -p /mmaction2/data
RUN git checkout main
RUN pip install cython --no-cache-dir
RUN pip install --no-cache-dir -e .
