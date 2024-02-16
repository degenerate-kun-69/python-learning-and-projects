choice = str(input("Do you know how many numbers you need to find an average of? (Y/N)"))
if(choice=="Y" or choice=="y"):
    count = int(input("how many numbers would you like to find average of?"))
    sum =0
    count2=count
    while(count2>0):
        sum += int(input("Enter number"))
        count2 = count2-1
    print("The Average is:",(sum/count))
else:
    sum =0
    count = 0
    choice2= "y"
    while(choice2 =="Y" or choice2=="y"):
        sum+=int(input("enter a number"))
        count =count+1
        choice2=str(input("Would you like to enter another number? (Y/N)"))
    print("The Average is: ",(sum/count))
