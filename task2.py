def task2(number):
    if number >= 0:
        original_num = number
        number_len = 0
        sum_num = 0
        # Calculating number length
        while True:
            number = number // 10
            number_len += 1
            if number == 0:
                break
        # Calculating new 'mirror' number
        while True:
            mirror_num = original_num % 10
            original_num = original_num // 10
            sum_num = mirror_num * (10 ** (number_len - 1)) + sum_num
            number_len -= 1
            if original_num == 0:
                break

    else:
        return "Incorrect value, supported only non-negative numbers"

    return sum_num


if __name__ == "__main__":
    print(task2(1234))
