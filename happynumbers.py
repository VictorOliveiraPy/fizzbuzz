def happy(number=(1, 10, 100)):
    if number:
        string = str(number)
        digits = [int(char) for char in string]
        total = sum(digits)

        return total == 1

    return False


assert happy(1)
assert happy(10)
assert happy(100)
assert not happy(4)
