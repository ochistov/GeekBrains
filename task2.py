'''
Let's create new variable (integer number)
it will be time in seconds, defined by user
----------------------------------------------
Создадим переменную (целое число)
Это будет время в секундах, задаваемое пользователем
'''

while True:
    try:
        time = int(input("Insert time in seconds: "))
    except:
        print(f"You are cheater! It's not a number! \nTry again")
        continue
    break
'''
Convert seconds into hours, minutes and seconds
-------------------------------------------------
Переведём секунды в часы, минуты и секунды
'''
hours = time//3600
minsec = time%3600
minutes = minsec//60
seconds = minsec%60

'''
Bring result to the required form (hh:mm:ss)
and display it at the screen
---------------------------------------------
Приведение результата к требуемому виду (чч:мм:сс)
и вывод на экран
'''
if len(str(hours)) < 2:
    hours = "0" + str(hours)
else:
    hours = str(hours)
if len(str(minutes)) < 2:
    minutes = "0" + str(minutes)
else:
    minutes = str(minutes)
if len(str(seconds)) < 2:
    seconds = "0" + str(seconds)
else:
    seconds = str(seconds)
print(f"{hours}:{minutes}:{seconds}")
# не до конца понял, зачем ссылку именно на pull-request, почему не на репозиторий:)