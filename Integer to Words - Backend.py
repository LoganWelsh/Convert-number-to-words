# This program asks the user to input an integer between 1 and 9999,
# then prints the inputted integer using words

input('This program takes an inputted number between 1 and 9999 and prints the number in words.\n'
      'Press enter to begin!')

def length_1(x):
    output = ""
    if x[0] == str(0):
        output = ""
    if x[0] == str(1):
        output = "one"
    if x[0] == str(2):
        output = "two"
    if x[0] == str(3):
        output = "three"
    if x[0] == str(4):
        output = "four"
    if x[0] == str(5):
        output = "five"
    if x[0] == str(6):
        output = "six"
    if x[0] == str(7):
        output = "seven"
    if x[0] == str(8):
        output = "eight"
    if x[0] == str(9):
        output = "nine"
    return output

def length_2(x):
    if x[0] == str(1):
        if x[1] == str(0):
            print ("ten")
        if x[1] == str(1):
            print ("eleven")
        if x[1] == str(2):
            print ("twelve")
        if x[1] == str(3):
            print ("thirteen")
        if x[1] == str(4):
            print ("fourteen")
        if x[1] == str(5):
            print ("fifteen")
        if x[1] == str(6):
            print ("sixteen")
        if x[1] == str(7):
            print ("seventeen")
        if x[1] == str(8):
            print ("eighteen")
        if x[1] == str(9):
            print ("nineteen")
    if x[0] == str(2):
        print("twenty ", end = "")
        print(length_1(x[1]))
    if x[0] == str(3):
        print("thirty ", end = "")
        print(length_1(x[1]))
    if x[0] == str(4):
        print("forty ", end = "")
        print(length_1(x[1]))
    if x[0] == str(5):
        print("fifty ", end = "")
        print(length_1(x[1]))
    if x[0] == str(6):
        print("sixty ", end = "")
        print(length_1(x[1]))
    if x[0] == str(7):
        print("seventy ", end = "")
        print(length_1(x[1]))
    if x[0] == str(8):
        print("eighty ", end = "")
        print(length_1(x[1]))
    if x[0] == str(9):
        print("ninety ", end = "")
        print(length_1(x[1]))

def length_3 (x):
    print(length_1(x[0]), end = " ")
    print("hundred ", end = "")
    (length_2(x[1:]))

def length_4(x):
    print(length_1(x[0]), end = " ")
    print("thousand ", end = "")
    (length_3(x[1:]))
    
def integer_to_word (integer):
    x = str(integer)
    if len(x) == 1:
        print(length_1(x))
    if len(x) == 2:
        length_2(x)
    if len(x) == 3:
        length_3(x)
    if len(x) == 4:
        length_4(x)

integer = 0
valid = False
while not valid:
    try:
        integer = int(input("Please enter an integer between 1 and 9999: "))
    except:
        print('Error! Entered value is not an integer.')
        continue
    valid = True
while integer not in range (1, 10000):
    print('Error! Integer is not between 1 and 9999.')
    valid = False
    while not valid:
        try:
            integer = int(input("Please enter an integer between 1 and 9999: "))
        except:
            print('Error! Entered value is not an integer.')
            continue
        valid = True
print('---------------------------------------------------------------------------------------------------------------')
integer_to_word (integer)

print('\n')
input('Finished! Click close to exit or press enter.')
