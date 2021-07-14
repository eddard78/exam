def decorator(function_to_decorate): 
    def divide(a, b): 
        if type(a) == int and type(b)==int and b != 0: 
            return f'Ваш результат: {    function_to_decorate(a,b)}    ' 
        else: 
            print('Ошибка на ноль делить нельзя') 
    return divide 
@decorator 

  

def divide(a, b): 
    return a/b 

  

print(divide(5,2))