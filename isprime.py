from sys import argv


def isPrime(number: int) -> bool:
    assert number > 1

    if number == 2:
        return True
    divisor: int = number // 2

    while divisor >= 2:
        if number % divisor == 0:
            return False
        divisor -= 1
    return True


if __name__ == "__main__":
    if argv[1::]:
        print(isPrime(int(argv[1])))

    else:
        print(isPrime(int(input("Enter number: "))))
