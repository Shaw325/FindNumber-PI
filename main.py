# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys

# Press the green button in the gutter to run the script.
import time
import math


def find_position(number):
    with open("pi-million.txt", "r")as f:
        pai = f.read()
    p_max = len(pai)
    for i in range(p_max):
        code = pai[i:i + 6]
        print("Find progress: {:.4f}%".format(i / p_max * 100))
        sys.stdout.flush()
        if code == str(number):
            print("\r", end="")
            print("找到了[{0}]，位置在：{1} 位".format(str(number), str(i)))
            break


if __name__ == '__main__':
    find_position(980906)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
