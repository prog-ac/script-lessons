import sys

def get_arg():
    args = sys.argv

    return args

def get_file(args):

    file_path = args[1];
    return file_path

def get_text_data(file):

    #ファイルオープン
    text_open = open(file)
    text_data = text_open.read()

    return text_data

def output_data(data):

    print(data.count("kobe"))

if __name__ == "__main__":
    args = get_arg()
    file = get_file(args)
    data = get_text_data(file)

    output_data(data)
