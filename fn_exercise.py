

def print_hello():
    print("hello")
    print("hi")
    


# if n > 0: 1  if n == 0: 0   if n < 0: -1

def compare(n):
    try:
        if n > 0:
            print(1)
        elif n == 0:
            print(0)
        else:
            print(-1)
    except TypeError:
        print(f"The value `{n}` is invalid")


def area(width, height):
    return (width * height)



def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


# "hello world."


def count_char(s):
    words = s.count(' ') + 1
    char = len(s)
    return words, char


is_even(5)
is_even(10)

is_even(50)
