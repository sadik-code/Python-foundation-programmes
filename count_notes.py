amount = int(input("Enter the amount: "))

notes = 0

notes += amount // 2000
amount = amount % 2000
print(notes)
notes += amount // 500
amount = amount % 500
print(notes)
notes += amount// 200
amount = amount % 200
print(notes)
notes += amount // 100
amount = amount % 100
print(notes)
notes += amount // 50
amount = amount % 50
print(notes)
notes += amount // 20
amount = amount % 20
print(notes)
notes += amount // 10
amount = amount % 10
print(notes)