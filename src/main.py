import os
from utils.tool import Tool


def main():
    source_folder = os.getcwd()
    print(f'路径：{source_folder}')

    res_folder = os.path.join(source_folder, '../../source')
    target_folder = os.path.join(source_folder, 'target')

    # 获取源文件夹中的所有文件列表
    file_list = os.listdir(res_folder)

    Tool.mkdir(target_folder)
    Tool.repair_to_png(file_list, res_folder, target_folder)


# __main__ 是python的一个特殊的内置变量名。
# 在 Python 中，__main__ 是一个用于表示当前模块（或脚本）正在执行的命名空间的名称。
# 当你直接运行一个 Python 脚本时，解释器会将该脚本视为一个主程序（main program）。
# 在这种情况下，Python 会自动将该脚本的命名空间指定为 __main__，以便你可以在脚本中获取和处理该命名空间中的变量和函数。
# 在这个例子中，if __name__ == "__main__": 语句用于检查当前模块是否正在作为主程序执行。
# 如果是，则执行该语句块中的代码。这样，你可以在脚本中将一些代码仅在脚本直接运行时执行，而在被导入为模块时不执行。
if __name__ == "__main__":
    main()
