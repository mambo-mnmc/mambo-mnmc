gender=input("enter your gender")
if gender == "Male":
    bs=2000
    tax=15/100*bs
    ns=bs-tax
elif gender == "Female":
    bs=2200
    tax=15/100*bs
    ns=bs-tax
else:
    bs=0
    tax=15/100*bs
    ns=bs-tax

print(tax)
print(bs)
print(ns)
