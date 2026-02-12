def isValidPassword(password):
    """
    Checks if password passes requirements

    Parameters:
        password (int): password

    Returns:
        boolean
    """
    lengthRequirement = False
    hasUpper = False
    hasLower = False
    hasDigit = False
    if len(password) >= 8:
        lengthRequirement = True
    for ch in password:
        if ch.isupper():
            hasUpper = True
        if ch.islower():
            hasLower = True
        if ch.isdigit():
            hasDigit = True
    if lengthRequirement and hasUpper and hasLower and hasDigit:
        return True
    else:
        return False


password = "MyPass123!"
if isValidPassword(password):
    print("Valid password")
else:
    print("Invalid password")
