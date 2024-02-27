arr = [int(x) for x in input("Enter numbers:").split( )]
def primecheck(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primecheck_list(numbers):
    prime_numbers = [num for num in numbers if primecheck(num)]
    print(f"Prime numbers: {prime_numbers}")
    print(f"Largest prime number: {max(prime_numbers)}")
    print(f"Total of the prime number: {sum(prime_numbers)}")

primecheck_list(arr)
    