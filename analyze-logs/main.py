
import sys
import logging

def get_arg():
    args = sys.argv

    return args

def get_file(args):

    file_path = args[1];
    return file_path

def get_text_data(file):

    #ファイルオープン
    text_open = open(file)
    text_data = text_open.readline()

    while text_data:
        print(text_data.strip())
        text_data = text_open.readline()


if __name__ == "__main__":
    args = get_arg()
    file = get_file(args)
    data = get_text_data(file)
