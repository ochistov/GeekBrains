'''
Let's create new variable (integer number),
defined by user
-------------------------------------
Создадим переменную (целое число),
задаваемую пользователем
'''
while True:
    try:
        n = int(input("Input integer number: "))
    except:
        print("It's not a number! \nTry again")
        continue
    break
'''
Solution and display it on the screen
------------------------------------------
Решение и вывод результата на экран
'''

print(f"Answer is {int(str(n)) + int(str(n) * 2) + int(str(n) * 3)}")
