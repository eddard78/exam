month = 1 

  

def calculator(deposit, densired_amount, annual_percentage, month): 
    result = annual_percentage/12 * deposit + deposit 
    if densired_amount <= result: 
        return f'Для накопления вам нужно вложиться на {    month}     месяц(а)' 
    elif densired_amount != result: 
        deposit = result  
        month += 1 
        return calculator(deposit, densired_amount, annual_percentage, month) 

  

print(calculator(860, 1500, 0.12, month))