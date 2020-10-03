import os


def file_one(file):
    while True:
        with open(file) as f:
            for line in f:
                yield line.strip()


def file_two(file):
    while True:
        with open(file) as f:
            for line in f:
                yield line.strip()


def file_three(file):
    while True:
        with open(file) as f:
            for line in f:
                yield line.strip()


if __name__ == "__main__":
    file1 = file_one(os.path.join('resources', 'file1.txt'))
    file2 = file_two(os.path.join('resources', 'file2.txt'))
    file3 = file_three(os.path.join('resources', 'file3.txt'))
    while True:
        print(next(file1))
        print(next(file2))
        print(next(file3))
