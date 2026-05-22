import torch
import time

print('=== GPU Setup & Cloud - Lesson 03 ===')
print(f'PyTorch 版本: {torch.__version__}')
print()

# 测试 1：MPS 可用性
print('--- 测试 1：硬件检测 ---')
print(f'MPS 可用: {torch.backends.mps.is_available()}')
device = torch.device('mps' if torch.backends.mps.is_available() else 'cpu')
print(f'使用设备: {device}')
print()

# 测试 2：神经网络训练速度对比
print('--- 测试 2：CPU vs MPS 训练速度对比 ---')
batch_size, input_dim, hidden_dim, output_dim, steps = 256, 1024, 2048, 512, 100

W1 = torch.randn(input_dim, hidden_dim)
W2 = torch.randn(hidden_dim, output_dim)
x = torch.randn(batch_size, input_dim)

start = time.time()
for _ in range(steps):
    h = torch.relu(x @ W1)
    out = h @ W2
cpu_time = time.time() - start
print(f'CPU {steps} 步: {cpu_time:.3f} 秒')

if torch.backends.mps.is_available():
    W1_m, W2_m, x_m = W1.to('mps'), W2.to('mps'), x.to('mps')
    for _ in range(3):
        _ = torch.relu(x_m @ W1_m) @ W2_m
    torch.mps.synchronize()
    start = time.time()
    for _ in range(steps):
        h = torch.relu(x_m @ W1_m)
        out = h @ W2_m
    torch.mps.synchronize()
    mps_time = time.time() - start
    print(f'MPS {steps} 步: {mps_time:.3f} 秒')
    print(f'加速比: {cpu_time / mps_time:.1f} 倍')
print()

# 测试 3：显存估算
print('--- 测试 3：可装载模型估算 ---')
available_gb = 16 * 0.75
models = [
    ('GPT-2 Small', 0.117), ('GPT-2 Large', 0.774),
    ('LLaMA 3.2 1B', 1.0), ('LLaMA 3.2 3B', 3.0),
    ('LLaMA 3 8B', 8.0),
]
for name, params_b in models:
    mem_gb = params_b * 1e9 * 2 / 1024**3
    status = '✅' if mem_gb < available_gb else '❌'
    print(f'{status} {name}: 需要 {mem_gb:.1f}GB')
