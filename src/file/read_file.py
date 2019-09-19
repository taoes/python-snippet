import os

# the path is linux style
# if you use windows os ,the path need replace windows style like `C://Document/text.txt`
file_path = '/tmp/text.txt'


def write_file():
    with open(file_path, 'w') as data_file:
        data_file.write("人生若只如初见，何事悲风秋画扇\n")
        data_file.write("等闲识得东风面，万紫千红总是春\n")
    print("文件写入完成，下面使用的是shell 执行的脚本(仅支持linux and unix*)：\n")
    os.system("cat " + file_path)


if __name__ == '__main__':
    write_file()
