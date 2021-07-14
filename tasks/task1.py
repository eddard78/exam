def func(date): 
    d_list = date.rsplit('.') 
    result = ((2021-int(d_list[2]))*365 + (5-int(d_list[1]))*30 + 7 + int(d_list[0]))/365 
    print(f'You are {    int(result)}     years old') 

  

func('15.01.1995') 
func('28.11.1195') 
func('21.04.2003')