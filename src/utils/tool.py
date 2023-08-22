import os
import shutil


class Tool:

    # 创建文件夹
    @classmethod
    def mkdir(cls, path):
        is_exists = os.path.exists(path)

        if not is_exists:

            os.makedirs(path)

            print('创建Target Fold')

        else:

            print('Target Fold 已存在')

    # 重命名
    @classmethod
    def repair_to_png(cls, files, res_path, target_path):
        for old_name in files:

            # 构建新的文件名，这里可以根据需要进行命名规则的修改

            new_name = old_name+'.png'
            copy_name = old_name+'copy'

            # 构建文件的完整路径

            old_path = os.path.join(res_path, old_name)
            copy_path = os.path.join(res_path, copy_name)
            new_path = os.path.join(target_path, new_name)

            shutil.copy2(old_path, copy_path)
            # 使用os.rename()函数进行重命名
            os.rename(copy_path, new_path)
