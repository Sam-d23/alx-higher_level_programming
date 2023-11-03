#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    x = 0
    for j in range(len(sys.argv) - 1):
        x += int (sys.argv[j + 1])
        print("{}".format(total))
