'''
Create user-define variables a and b
--------------------------------------
Пользователь задает переменные (стартовый показатель и искомый)
'''
while True:
    try:
        a = float(input("Insert a (number): "))
        b = float(input("Insert b (number): "))
    except:
        print(f"You are cheater! It's not a number! \nTry again")
        continue
    break

'''
Solution
-----------
Решение
'''
i = 1 # № of day
while a < b:
    a = a * 1.1
    i += 1
    print(a)
print(f"Last day is {i}")
# не до конца понял, зачем ссылку именно на pull-request, почему не на репозиторий:)