"""
Описание: программа принимает начало и конец отрезка и находит все простые числа в нём
"""


def findPrimeNumbers(start, end):
    """
    Findes all prime numbers in given range

    Parameters:
        start(int): begining of the range
        end(int): end of the range

    Returns:
        primeNumbers: list of all prime numbers
    """
    primeNumbers = []
    for number in range(start, end + 1):
        check = True
        # Goes throw all possible dividers and when finds numbers which is devides without reminder breaks out
        for divider in range(2, number):
            if number % divider == 0:
                check = False
                break
        # If devider isn't found add number to list of prime numbers
        if check:
            primeNumbers.append(number)
    return primeNumbers


start = 2
end = 50
primeNumbers = findPrimeNumbers(start, end)
print(primeNumbers)
