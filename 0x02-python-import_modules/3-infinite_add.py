#!/usr/bin/python3
def add_arg(argv):
    y = len(argv) - 1
    if y == 0:
        print("{:d}".format(y))
        return
    else:
        j = 1
        add = 0
        while j <= y:
            add += int(argv[j])
            j += 1
        print("{:d}".format(add))


if __name__ == "__main__":
    import sys
    add_arg(sys.argv)
