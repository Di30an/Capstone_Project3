def isEmail():
# Checks the endings of the email to make sure it has propers extension
    extentsions_list = (".net", ".com", ".edu")
    email = input("Please enter an Artist Email")
# Index to check the last 4 values of the email. 
    if email[:-4] not in extentsions_list :
        email = input("Please enter an Artist Email that ends with a .com")
    else: 
        return email

def isName():
# Mainly checks if a name is present. Difficult to Regex names 
    name = input("Please enter an Artist Name")
    while not name :
        name = input("Please enter an Artist Name")
    return name