import os
from tool import Tool

source_folder = os.getcwd()
print(f'路径：{source_folder}')

res_folder = os.path.join(source_folder, 'source')
target_folder = os.path.join(source_folder, 'target')

# 获取源文件夹中的所有文件列表
file_list = os.listdir(res_folder)

Tool.mkdir(target_folder)
Tool.rename(file_list, res_folder, target_folder)
