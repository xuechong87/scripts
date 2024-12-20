# coding: utf-8
import os
import re

def find_and_print_log_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if re.match(r"^.*\.log$", file) or re.match(r"^.*\.log\.([^\.]*)$", file):
                file_path = os.path.join(root, file)
                print(f"Deleting {file_path}")
                os.remove(file_path)  # 删除文件

if __name__ == '__main__':
    find_and_print_log_files("/Users/xuechong/Desktop/hb/")