'''
Let's create new variable (integer number)
it will be define by user
----------------------------------------------
Создадим переменную (целое число)
Она будет задана пользователем
'''
while True:
    try:
        numb = int(input("Insert number: "))
    except:
        print(f"You are cheater! It's not a number! \nTry again")
        continue
    break

'''
Solution. Divide the number converted into a string by 
symbols, find the largest, display the result on the screen
------------------------------------------------------
Решение. Делим преобразованное в строку число на цифры, находим наибольшую, выводим результат на экран
'''

numb = str(numb)
max = 0
i = 0
while i <= len(numb) - 1: # перебираем счётчик, пока i не достигнет длины строки минус 1, т.к. нумерация начинается с 0
    if int(numb[i]) > max:
        max = int(numb[i])
        i += 1
    else:
        i += 1
print(f"Maximum digit in number is {max}")

'''
Вариант с циклом for :) но в задании вроде обязательно while

numb = str(numb)
max = 0
for i in range(len(numb)):
    if int(numb[i]) > max:
        max = int(numb[i])
print(max)
'''
# не до конца понял, зачем ссылку именно на pull-request, почему не на репозиторий:)