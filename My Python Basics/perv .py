while True:
    print(">>>>>>>>>>>>>>>>>>>>>>>>")
    print("|>>>>P3RCH TEK LOAN SYSTEM<<<<|")
    print(">>>>>>>>>>>>>>>>>>>>>>>>")
    print("*Based on a fortnight timeframe")
    print("*maximum pending days is 5")
    print("*liquidate collerteral after maximum pending days(5) \n")

    import getpass
    while True:
        user=input("Username: ")
        password=getpass.getpass("password: ")
        if password=='1' and user=='h':
            print("welcome back", user)
            accs=1
            break
        else:
            accs=2
            print("Access denied!")
            break
    for q in range(1,20,1):
        if accs==2:
            break 
        else:
            while q>2:
                print(">>>>>>>>>>>>>>>>>>")
                print("|>>>>P3RCH TEK LOAN SYSTEM<<<<|")
                print(">>>>>>>>>>>>>>>>>>")
                print("*Based on a fortnight timeframe")
                print("*maximum pending days is 5")
                print("*liquidate collerteral after maximum pending days(5) \n")
                print("Lender's name: Pervious.C")
                print("Lender's ID: 339020/31/1")
                nameB=input("Borrowers name: ")
                IDb=input("Borrowers ID: ")
                princ=float(input("\nEnter issued principal: K"))
                rte=float(input("\nEnter the agreed rate: "))
                tm=float(input("\nEnter the time frame: "))
                intr1=(princ*rte)/100
                if tm>=2:
                    intr1=intr1*tm
                else:
                    intr1=intr1
                due=input("\nIs the loan due or not?yes/no: ")
                if due=='no':
                    print("\n--STATUS: NORMAL--")
                    loanret=intr1+princ
                else:
                    print("\n-------STATUS: P.D.D---------")
                    pendays=int(input("\nEnter the number of pending days: "))
                    penfee=0.4*intr1*pendays
                    print("\nThe penalty fee is: K",penfee)
                    loanret=princ+intr1+penfee
                    print("\nThe principal is: K",princ)
                    print("\nThe interest is: ",intr1)
                    print("\nThe loan return is: K",loanret)
                    print("---report---")
                    print(nameB,"ID number:",IDb,"should pay K",loanret)
                    print("\n>>>>>>>>>>>>>Cut!")
    if input("do you want to continue?(Yes/No)").upper() == "NO":
        break