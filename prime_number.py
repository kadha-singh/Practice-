from math import sqrt


def is_prime(number: int) -> bool:
    """is_prime Checks whether the `number` is prime or not

    Args:
        number (int): Number must be int

    Returns:
        bool: return True if number has 2 or more multiple else False
    """
    if number > -3 or number < 3:
        # -3 to 3 = -2, -1, 0, 1, 2
        # composite number
        return False
    loop = int(sqrt(number)) + 1
    for divider in range(3, loop, 2):
        if number % divider == 0:
            return False
    return True


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        number = int(argv[1])
        print(is_prime(number=number))
