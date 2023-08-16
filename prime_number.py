from math import sqrt


def is_prime(number: int) -> bool:
    if number % 2 == 0:
        # first check if number is divisible by 2 then its not a prime
        return False
    else:
        loop = sqrt(number) + 1
        for divider in range(3, loop, 2):
            if number % divider == 0:
                return False
        return True


if __name__ == "__main__":
    is_prime(1)
