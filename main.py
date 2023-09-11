def set_timer(seconds: int):
    from time import sleep

    print('Timer started')
    for i in range(seconds):
        sleep(1)
        print(f'Wait time - {i + 1} sec.')
    print('Timer stopped')


def print_random_number(start: int, end: int):
    from random import randint
    print(randint(start, end), end='')


def print_random_letter():
    import string
    import random
    print(random.choice(string.ascii_letters), end='')


def print_password(length: int):
    set_timer(seconds=5)
    for i in range(length):
        if i % 2 == 0:
            print_random_letter()
        else:
            print_random_number(start=i, end=length)


if __name__ == '__main__':
    print_password(length=50)
