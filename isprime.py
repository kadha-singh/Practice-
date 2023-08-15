def isPrime(number: int) -> bool:
    divisor: int = number - 1
    while number >= 1:
        if number % divisor == 0:
            return True
        divisor -= 1
    return False


print(isPrime(4))
