# 基于机器学习的图像语义分割

## 项目结构
```
SemSeg-Benchmark/
├── data/
│   ├── datasets/      # 存放数据集
│   ├── __init__.py
│   └── dataset.py     # 核心：统一的数据加载器
├── src/
│   ├── models/
│   │   ├── unet.py       # U-Net模型
│   │   └── deeplab.py    # 其他的模型例如deeplab
│   ├── utils/
│   │   ├── metrics.py    # 评估指标（如mIoU）
│   │   └── logger.py
│   ├── config.py         # 统一参数配置
│   ├── trainer.py        # 训练循环
│   └── evaluator.py      # 模型评估
├── scripts/
│   ├── train.py          # 训练入口
│   └── evaluate.py       # 评估入口
├── outputs/
│   ├── checkpoints/      # 模型权重
│   └── predictions/      # 预测结果
├── requirements.txt
└── README.md
```
## 核心库
查看镜像源
```
pip config list
conda config --show-sources

```
pip添加清华源
```
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pip config set install.trusted-host pypi.tuna.tsinghua.edu.cn
```
conda添加清华源
```
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
```