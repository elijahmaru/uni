def formatUsers(users):
    """
    formats name of users to start from upper case letter an rest of the letter being lower case
    parameters:
        users (list of strings): list of names

    returns:
        list: with formated user names
    """
    clean_users = []

    for u in users:
        # find empty fields of names and ignores them
        if u == "  ":
            continue

        # ignores spaces in user names
        temp = ""
        for char in u:
            if char != " ":
                temp = temp + char
        # makes first letter uppers case and rest lower case
        if len(temp) > 0:
            first = temp[0].upper()
            rest = temp[1:].lower()
            fixed_name = first + rest
            clean_users.append(fixed_name)
    return clean_users


users = ["  aNNA  ", "boris", "  ", "cLAra", "   daniEL ", "eva"]
clean_users = formatUsers(users)
print(f"Результат: {clean_users}")
