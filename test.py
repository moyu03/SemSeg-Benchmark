# 验证PyTorch基础安装和版本
import torch
print(torch.__version__)  # 预期输出：2.5.1

# （可选但重要）验证CUDA（GPU加速）是否可用
# 由于你的安装显示是cpu版本，这里预期会输出False
print(torch.cuda.is_available())  # 预期输出：False