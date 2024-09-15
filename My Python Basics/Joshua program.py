import os
#this program should be able to help the user know the amount of rest to take after studies and how long to continue if his has not had time to study.
numhrs=int(input("Enter the total number of hours in a day: \n"))
substd=("math","english","science","social studies","creative and technology studies","art","computer studies","business studies","history")
print("Use the following numbers to select your subject:")
print("""0:math 1:english 2:science 3:social studies 4:creative and technology studies 5:art 6:computer studies 7:business studies 8:history""")
#tuples are unchangable. why not use lists so the user can simply add to the list should it be the case that the course is not available e.g. substd= []
# substd.append()
#or if the program can ask the user to send a messag7e to the admin for a course to be added.
hps=[]
#hours spent on each entered subject in chronological order
while True:
   subcode=int(input("enter subject code: "))
   subject=substd[subcode]
   hps.append(int(input("Enter the number of hours you studied " + subject +": " )))
   #added the print(hps) to see if the list is adding or not. must be hidden from the user.
   print(hps)
   #should allow the user to choose if they still want to add another subject to the list of subjects they studied.
   if input("do you want to select another subject?(Yes/No)").upper() == "NO":
      break
usedhrs=sum(hps)
freetm=(numhrs/usedhrs)-2
if usedhrs >= 6:
   print("You spent",usedhrs,"hours studying. you can take some rest for about",freetm,"hours ")
elif usedhrs <= 5:
   print("You spent",usedhrs,"hours studying. please take more time to read of about",freetm,"hours ")
else:
   print("There is a problem retriving your data")
os.system("pause")