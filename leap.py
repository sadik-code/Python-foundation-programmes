n=int(input("enter a year"))
if n%400==0 and (n%4==0 or n%100 !=100) :
    print("its a leap year")
else:
    print("its not a leap year")