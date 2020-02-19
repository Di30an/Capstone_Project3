"""
Input and validation utilites

"""

def isEmail():
# Checks the endings of the email to make sure it has propers extension
    extentsions_list = (".net", ".com", ".edu")
    email = input("Please enter an Artist Email")
# Index to check the last 4 values of the email. 
    if email[:-4] not in extentsions_list :
        email = input("Please enter an Artist Email that ends with a .com")
    else: 
        return email

def isName(person):
# Mainly checks if a name is present. Difficult to Regex names 
    while True:
        try:
            name = input(f"Please enter an {person} name : ")
            if name == "":
                print("Please enter a name : ")
            else: 
                return name
        except ValueError as e:
            print("Enter a name please : ")

def input_positive_float(question):
    while True:
        try:
            number = float(input(question))
            if number < 0:
                print('Enter a positive number')
            else:
                return number 
        except ValueError as e:
            print('Enter a number.')
def is_availbilty():
    while True:
        
            status = input('Please enter available or not available : ').upper()
            if status == "AVAILABLE" :
                return status
            if status == "NOT AVAILABLE" :
                return status
            else:
                status = input('Please enter available or not available : ').upper()

def header(text):
    stars = len(text) * '*'
    print(f'\n{stars}\n{text}\n{stars}\n')
        
