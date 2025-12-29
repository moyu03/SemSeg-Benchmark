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