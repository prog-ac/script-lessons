import sys

def get_arg():
    args = sys.argv

    return args

def sort_array(args):
    del args[0]

    tmp_args = []
    for num in range(len(args)):
        tmp_args.append(int(args[num]))

    tmp_args.sort(reverse = True)
    return tmp_args

def output_data(sort_args):
    for num in range(len(sort_args)):
        if num == (len(sort_args) - 1):
           print(sort_args[num])
        else:
            print("{0}{1}".format(sort_args[num], " "), end="")


if __name__ == "__main__":
    args = get_arg()
    sort_args = sort_array(args)

    output_data(sort_args)
