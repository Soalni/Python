my_family = []
print("Start application")
my_family.append(input("What`s your name: ").title()) #Call name

select = input("Have you got family? (Y/N)").upper()  #Select family

if select == "Y":  #Start call name of family
    my_family.append(input("OK. What is the first member`s name of your family: ").title())
    select = input("Have you got any other member? (Y/N)").upper()
if select == "Y":
    my_family.append(input("OK. What is the second member`s name of your family: ").title())
    select = input("Have you got any other member? (Y/N)").upper()
if select == "Y":
    my_family.append(input("OK. What is the third member`s name of your family: ").title())
    select = input("Have you got any other member? (Y/N)").upper()
if select == "Y":
    my_family.append(input("OK. What is the fourth member`s name of your family: ").title())
    select = input("Have you got any other member? (Y/N)").upper()
else:
    print("Ok. That is your family: " + str(my_family))
    