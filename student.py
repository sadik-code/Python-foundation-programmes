Physics=int(input("physics marks"))
Chemistry=int(input("chemistry marks"))
Biology=int(input("biology marks"))
Mathematics=int(input("math mark"))
Computer=int(input("computer marks"))
avg= (Physics+ Chemistry+ Biology+ Mathematics+ Computer)/5
if avg>=90:
    print("grade A")
elif avg>=80:
    print("grade b")
elif avg>=70:
    print("grade c")
elif avg>=60:
    print("grade d")
elif avg>=50:
    print("grade e")
elif avg>=40:
    print("grade f")
else:
    print("fail")
print(avg)
