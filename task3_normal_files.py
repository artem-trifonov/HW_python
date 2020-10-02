def task3(file1, file2, file3):
    i = 0
    j = 0
    k = 0
    with open(file1) as f1, open(file2) as f2, open(file3) as f3:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        lines3 = f3.readlines()

        f1_length = len(lines1)
        f2_length = len(lines2)
        f3_length = len(lines3)

        while True:
            if f1_length > 0:
                print(lines1[i].strip())
                i += 1
                f1_length -= 1
            else:
                i = 0
                print(lines1[i].strip())
                i += 1
                f1_length = len(lines1) - 1

            if f2_length > 0:
                print(lines2[j].strip())
                j += 1
                f2_length -= 1
            else:
                j = 0
                print(lines2[j].strip())
                j += 1
                f2_length = len(lines2) - 1

            if f3_length > 0:
                print(lines3[k].strip())
                k += 1
                f3_length -= 1
            else:
                k = 0
                print(lines3[k].strip())
                k += 1
                f3_length = len(lines3) - 1


if __name__ == "__main__":
    task3("resources/file1.txt", "resources/file2.txt", "resources/file3.txt")
