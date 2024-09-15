import os
while True:
    i=range(3, 11, 2)
    print("odd numbers:", list(i))
    product=1
    for odd_numbers in i:
        product *=odd_numbers
    print("the product is:", product)
    if input("do you want to continue?(Yes/No)").upper() == "NO":
        break
os.system("pause")
