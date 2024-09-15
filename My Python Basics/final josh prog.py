import os
import platform

def subject_codes():
    print("Use the following numbers to select your subject:")
    print(""" 0:math \n 1:english \n 2:science \n 3:social studies \n 4:creative and technology studies \n 5:art \n 6:computer studies \n 7:business studies \n 8:history""")
    print("remember the hours you enter for each subject")
    print("...................................................")
    return
 
def restart_program():
    restart = input("\nWould you like to restart the program?/n Enter 'r' to restart or Enter 'a' to abort: ")
    if restart.lower() == 'r':
        if platform.system() == "Windows":
            print(os.system('cls')) 
        else:
            print(os.system('clear'))
        Study_Advisor()
        restart_program()
    else:
        quit(Abort)
		
global substd
substd=("math","english","science","social studies","creative and technology studies","art","computer studies","business studies","history")
global subject
subject=[]
global hps
hps=[]

def Study_Advisor():
    global Abort
    Abort="#########\nThank you for trusting Joshua Phiri. \n{}Study and Rest Advisor.{}\n"
    
    print(""" 
    %%%%%%....Study and Sleep Advisor....%%%%%%""")
    print("""
    >>>>>>>>>>>>>>>>Joshua Phiri<<<<<<<<<<<<<<<<
    """)
    print(""".................................................""")
    try:
        numhrs=int(input("Enter the total number of hours in a day: "))
    except TypeError:
        exit("\n Problem with your entry. Done decimal integers accepted.\n")
    else:
        print("\nThank you. the program proceeds...\n")
    
    ans = 1
    while ans == 1:
        subject_codes()
        subcode=int(input("Enter subject code: "))
        if subcode in substd:
            print("\nSubject already entered\n")
            break
        elif subcode not in substd:
            subject.append(substd[subcode])
            hps.append(int(input("\nEnter the number of hours you studied " + substd[subcode] +"(please remember the subject and hours): " )))
            print("\nAdded now.")
            print("...............................................")
        else:
            print("\nsubject code out of range \nRestarting process...")
            continue
        ans = int(input("\nDo you want to add another subject? 1. YES or 2. NO \n..Only write specified number: "))
        if ans == 1:
            continue
        elif ans != 1 and ans != 2:
            print("\nIt seems like you entered a wrong option. restarting curent process...")
            print("................................................")
            continue
        else:
            if ans == 2:
                print("proceeding ...")
                print("................................................")
                break
    wish=1
    while wish == 1:
        print("The subjects you studied are:", (subject))
        rem=1
        while rem ==1:
            rem=int(input("\nDo you want to remove a subject? Please use the specified number 1.YES or 2.NO: "))
            if rem==1:
                subject.remove(input("\nEnter the name of subject in full: "))
                print(subject)
                hps.remove(int(input("remove the exact number of hours you entered earlier for subect you removed: " )))
                print(hps)
                print("................................................")
                break
            elif rem == 2:
                print("proceeding ...")
                print("................................................")
                break
            else:
                if rem != 1 and rem != 2:
                    print("It seems like you entered a wrong option. Restarting current process...")
                    print("................................................")
                    continue
        add=1
        while add==1:
            add=int(input("\nDo you want to add a subject and study hours? 1.add or 2.Dont add: "))
            if add==1:
                subject.append(input("enter the name of subject in full: "))
                hps.append(int(input("Enter the number of hours you studied: " )))
                print("................................................")
                continue
            elif add == 2:
                print("proceeding ...")
                print("................................................")
                break
            else:
                if add != 1 and add != 2:
                    print("It seems like you entered a wrong option. Restarting current process")
                    print("................................................")
                    continue
        wish=int(input("Do you want to compute progress so far? if you do not wish to continue, the program will restart 1.YES or 2.NO: " ))
        if wish == 1:
            usedhrs = sum(hps)
            freetm=(numhrs/usedhrs)-2
            print("processing...")
            print("...")
            if usedhrs >= 6:
                print("................................................")
                print("You spent",usedhrs,"hours studying. you can take some rest for about",freetm,"hours.")
                break
            elif usedhrs <= 5:
                print("................................................")
                print("You spent",usedhrs,"hours studying. please take more time to read of about",freetm,"hours.")
                print("................................................")
                break
            else:
                print("................................................")
                print("unable to advise. discontinuing process...")
                print("................................................")
                break
        elif wish == 2:
            print("................................................")
            print("wrong option... please confirm entry again...")
            print("................................................")
            continue
        else:
            if wish != 1 and wish != 2:
                print("................................................")
                print("There is a problem retriving your data. Discontinuing process...")
                print("................................................")
                break

Study_Advisor()
restart_program()

os.system("pause")