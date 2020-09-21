from threading import Thread
import time


def file_one(file):
    while True:
        with open(file) as f:
            for line in f:
                print(line, end='')
                time.sleep(1)


def file_two(file):
    while True:
        with open(file) as f:
            for line in f:
                print(line, end='')
                time.sleep(1)


def file_three(file):
    while True:
        with open(file) as f:
            for line in f:
                print(line, end='')
                time.sleep(1)


if __name__ == "__main__":
    f1_thread = Thread(target=file_one, args=('resources/file1.txt',))
    f2_thread = Thread(target=file_two, args=('resources/file2.txt',))
    f3_thread = Thread(target=file_three, args=('resources/file3.txt',))

    f1_thread.start()
    time.sleep(0.2)
    f2_thread.start()
    time.sleep(0.2)
    f3_thread.start()
