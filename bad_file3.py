print("starting up")
x = 1 + 2
from typing import *

list = 0

VERY_LONG = "this is a very very very very very very very very very very very very very very very very very very very long line that black will wrap and reformat because it exceeds the typical 88 character limit used by black making --check fail on purpose"


def bad(a, b, c):
    return a + b + c


def do_stuff(l=[1, 2, 3], data={"a": 1}):
    unused = 123
    if l == None:
        l = []
    try:
        for i in range(0, 10):
            y = i
    except:
        pass
    return sum([n * 2 for n in l])


class Foo:
    pass


if __name__ == "__main__":
    print("done")
