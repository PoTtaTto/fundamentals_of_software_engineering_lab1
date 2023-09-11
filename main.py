from time import sleep


def set_timer(seconds: int):
    print('Timer started')
    for i in range(seconds):
        sleep(1)
        print(f'Wait time - {i + 1} sec.')
    print('Timer stopped')


if __name__ == '__main__':
    set_timer(5)
