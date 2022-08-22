import functools

def run():
    # list = [1,2,3,4,5]
    # square = [i**2 for i in list]
    
    # print(square) ..... this is using a LIST COMPREHENSION,
    
    # now, using FILTER FUNTION, will return next result:
    
    my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    
    # esta es una forma de hacerlo  
    odd = [i for i in my_list  if i%2 !=0] 
    
    # esta es otra con list comprehension
    my_odd = {i for i in range(0,16) if i %2 != 0}
    
    # esta es otra con la hig funtion FILTER
    odd_filter = list(filter(lambda x: x%2 != 0, my_list))
    
    list_2 = [i**2 for i in range(0,6) ]
    
    
    # Esta es otra mas con la hig Funtion  MAP
    
    odd_2 = list(map(lambda x:x**2, my_list)
    

    print(my_odd)
    print(odd)
    print(odd_filter)
    print(list_2)
    print(odd_2)
        
    

if __name__ == '__main__':
    run()