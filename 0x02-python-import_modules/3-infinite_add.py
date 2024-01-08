#!/usr/bin/python3
if __name__ == "__main__":
    import sys
list_1 = sys.argv
sum_1 = 0
for i in range(1, len(list_1)):
    sum_1 += int(list_1[i])
print("{}".format(sum_1))
