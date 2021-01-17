# revenue - выручка
# costs - издержки
'''
User defines revenue and costs
---------------------------------
Пользователь задаёт значения выручки и издержек
'''

while True:
    try:
        revenue = float(input("Insert revenue: "))
        costs = float(input("Insert costs: "))
    except:
        print(f"You are cheater! It's not a number! \nTry again")
        continue
    break
'''
Checking ratio of revenue and costs to find out the profitability 
of the company, then display the result on the screen. 
If the company is profitability we get the number 
of employees (set by the user), display on the screen company's profit per employee
-----------------------------------------------------------------------------------
Проверяем соотношение выручки и издержек для выяснения прибыльности фирмы, 
выводим результат. Если фирма прибыльная, выводим рентабельность, получаем количество 
сотрудников (задаётся пользователем), выводим прибыль 
фирмы в расчёте на одного сотрудника
'''

if revenue > costs:
    profit_sign = True
    print(f"The company is profitable!\nRentability of the company is {round((((revenue - costs) / revenue) * 100), 2)}%")
    staff_cnt = int(input("Insert the number of employees: "))
    print(f"Profit of the company per employee is {(revenue - costs) / staff_cnt}")
    
else:
    profit_sign = False
    print(f"The company is unprofitable!")
    # не до конца понял, зачем ссылку именно на pull-request, почему не на репозиторий:)