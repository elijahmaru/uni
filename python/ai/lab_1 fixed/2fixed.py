"""
Описание:
Программа принимает фразу и находит самую часто встречающиюся букву. Сначало она проходит по всей фразу и находит сколько раз какая буква встречается и сохраняет это в словарь, а потом проходится по словарю и находит наибольшие значение и ассоциированный с ней ключ(букву)
"""


def findMostFrequent(string):
    """
    Findes most frequent character in a phrase
    Parameters:
        string: phrase in a string form
    Returns:
        tuple: character that is most frequent and how many times it apears
    """
    # dictionary of characters that uses character as key and how many times it appears as value
    dictionaryOfChars = {}
    for char in string:
        # update dictionary of characters: if new is found add to a dictionary, if it is space ignore it, increment amount if it alredy in dictonary
        if char == " ":
            continue
        if char in dictionaryOfChars:
            dictionaryOfChars[char] = dictionaryOfChars[char] + 1
        else:
            dictionaryOfChars[char] = 1
    timesFound = 0
    mostFrequentChar = ""
    for symbol in dictionaryOfChars:
        # if current character is found more times than the previous most frequent update most frequent character and how many times it found
        if dictionaryOfChars[symbol] > timesFound:
            timesFound = dictionaryOfChars[symbol]
            mostFrequentChar = symbol
    return mostFrequentChar, timesFound


string = "programming is fun"
char, times = findMostFrequent(string)
print(f"Most frequent: {char} appears {times} times")
