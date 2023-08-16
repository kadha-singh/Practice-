from math import sqrt


def is_prime(number: int) -> bool:
    """is_prime Checks whether the `number` is prime or not

    Args:
        number (int): Number must be int

    Returns:
        bool: return True if number has 2 or more multiple else False
    """
    if number % 2 == 0:
        # first check if number is divisible by 2 then its not a prime
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
