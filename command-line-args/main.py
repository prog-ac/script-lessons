import sys

def get_argv():
    args = sys.argv

    return args

def output_data(args):
    first_num = int(args[1])
    second_num = int(args[2])

    ans = (first_num / second_num)

    print("{0}{1}".format(ans, "%"))

if __name__ == "__main__":
    args = get_argv()
    output_data(args)
