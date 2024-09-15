import os

input("Press Enter to Proceed")
while True:
    product=1
    for odd_numbers in range(3, 11, 2):
        product *=odd_numbers
    print("the product is:", product)
    if input("do you want to continue?(Yes/No)").upper() == "NO":
        break
os.system("pause")
