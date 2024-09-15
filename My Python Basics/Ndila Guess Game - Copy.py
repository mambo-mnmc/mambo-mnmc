import os
while True:
    import random
    number = random.randint(0+1, 100)
    name = input("Please enter your name: ")
    print("Hi", name.upper(), ", welcome to Ndila Guessing Game")
    print("INSTRUCTIONS:")
    print("""
    1. You are required to guess the number that i choose.
    """)
    print("""
    2. You have 5 attempts only, and 10 marks in total
    """)
    print("""
    3. For every wrong attempt, you loose 2 marks
    """)
    print('''.....................................................................
        ''')
    
    G_attempts = 0
    print("Lets Play", name.upper(), "i have chosen a number between 0 and 100")
    print()
    while G_attempts < 5:
        NGuessed = int(input("Guess the Number i chose: "))
        G_attempts += 1
        if NGuessed < number:
            print('''The number you chose is small, i chose a bigger number''')
        while NGuessed == number:
            points = Points
            print(""" You have scored,""" + str(Scores), """points""")
            break
        print('''..................................................................
            ''')
        if NGuessed > number:
            print('''The number you chose is big, i chose a smaller number''')
            print('''.................................................................
            ''')
        if NGuessed == number:
            break
    if NGuessed == number:
        print("You Guessed It Right, Yo", name, ", congratulations")
    else:
        print("you can do better, yo!... the number i guessed is," + str(number))
    if input("do you want to continue?(Yes/No)").upper() == "NO":
        break    
os.system("pause")
