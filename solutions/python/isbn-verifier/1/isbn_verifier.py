def is_valid(isbn):
    clean = isbn.replace("-", "")

    if len(clean) != 10:
        return False

    digits = []

    for index, char in enumerate(clean):
        if char == "X" and index == 9:
            digits.append(10)
        elif char.isdigit():
            digits.append(int(char))
        else:
            return False

    multipliers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    total = 0

    for digit, multiplier in zip(digits, multipliers):
        total += digit * multiplier

    return total % 11 == 0