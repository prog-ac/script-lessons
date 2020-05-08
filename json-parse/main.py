import sys
import json

def get_arg():
    args = sys.argv

    return args

def get_file(args):

    file_path = args[1];

    return file_path

def get_json_data(file):

    #ファイルオープン
    json_open = open(file, 'r')
    #ファイルロード
    json_load = json.load(json_open)
    return json_load

def output_data(dic_data):
    for data in dic_data["profiles"]:
        print("{0}:{1}".format(data["name"], data["age"]))


if __name__ == "__main__":
    args = get_arg()
    file = get_file(args)
    dic_data = get_json_data(file)

    output_data(dic_data)
