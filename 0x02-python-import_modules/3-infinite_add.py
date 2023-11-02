#!/usr/bin/python3
def add_arg(argv):
    x = len(argv) - 1
    if x == 0:
        print("{:d}".format(x))
        return
    else:
        i = 1
        add = 0
        while i <= x:
            add += int(argv[i])
            i += 1
        print("{:d}".format(add))

if __name__ == "__main__":
    import sys
    add_arg(sys.argv)
