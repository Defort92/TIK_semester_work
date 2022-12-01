def from_decimal_to_binary(number, digits) -> str:
    if int(number) >= 2 ** digits:
        return "1" * digits

    final = ''
    while number > 0:
        final = str(number % 2) + final
        number = number // 2

    return final


def from_binary_to_decimal(number) -> int:
    number = str(number)
    final = 0
    counter = 0
    for element in number:
        position = len(number) - 1 - counter
        final += int(element) * (2 ** position)
        counter += 1

    return final
