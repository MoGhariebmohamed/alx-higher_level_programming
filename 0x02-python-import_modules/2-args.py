#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    def myarg(argv):
        x = len(argv)
        if x == 0:
            print("{}argument.".format(x))
        elif x == 1:
            print("{}argument:".format(x))
        else:
            print("{}arguments:".format(x))
            i = 1
            for i in range(x):
                print("{}: {}".format(x, argv[i]))
