import os

def get_path():
    #ホームディレクトリ取得
    return os.environ['HOME']

def find_all_files(path):
    #カレントディレクトリ, 内包ディレクトリ, 内包するファイル
    for root, dirs, files in os.walk(path):
        for file in files:
            #yield os.path.join(root, file)     #パスとファイル名を返す
            #yield root                         #パスのみ返す（ファイル名は含まない）
            yield file                          #ファイル名のみ返す　


if __name__ == "__main__":

    path = get_path()
    for file in find_all_files(path):
        print(file)
