#!/usr/bin/python3
if __name__ == "__main__":
    import sys
list_1 = sys.argv
if len(list_1) == 1:
    print("0 arguments.")
elif len(list_1) != 2:
    print("{} arguments:".format(len(list_1) - 1))
    L_count = 0
    for i in list_1:
        L_count += 1
        if i[0] != '.':
            print("{}: {}".format(L_count - 1, i))
else:
    print("1 argument:\n1: {}".format(list_1[1]))
