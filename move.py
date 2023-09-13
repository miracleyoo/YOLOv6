import os
import shutil

val_dir = '/workspace/YOLOv6/MVSEC/images/val'
train_dir = '/workspace/YOLOv6/MVSEC/images/train'

# 列出val文件夹中的所有文件，并按数字排序
val_files = sorted([int(f) for f in os.listdir(val_dir)])

# 获取train文件夹中最大的文件编号
train_files = [int(f) for f in os.listdir(train_dir)]
max_train = max(train_files) if train_files else 0

# 计算要移动的文件数
num_move = int(len(val_files) * 0.6)

# 移动文件
for i in range(num_move):
    old_path = os.path.join(val_dir, str(val_files[i]))
    new_path = os.path.join(train_dir, str(max_train + i + 1))
    shutil.move(old_path, new_path)