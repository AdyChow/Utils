import os
import shutil

# 将一个目录下所有指定文件，挪到另一个目录下

def search_dir(path, result):
    child_files = os.listdir(path)

    for f in child_files:
        child = os.path.join(path, f)
        if os.path.isdir(child):
            search_dir(child, result)
        else:
            result.append(child)


if __name__ == '__main__':
    input_dir = "/Users/momo/Desktop/log"
    output_dir = "/Users/momo/Desktop/log_new"
    files = list()
    search_dir(input_dir, files)
    for f in files:
        print("find %s" % f)
        if os.path.isfile(f) and f.endswith(".json"):
            print("move file %s" % f)
            shutil.move(f, output_dir)