import math


def run():
#     my_dict = {}
    
#     for i in range (0,100):
#         if i % 3 != 0:
#             my_dict[i] = (i**2)
            
#     print(my_dict)
# la diferencia con el list comprehension, es que en los diccionarios no se puede
# agregar con el .append, porque son inmutables debemos hacerlo con [i] para 
# agregar el item en el diccionario

#  tambien se puede hacer con el siguiente codigo:

    # my_dict = {i:(i**2) for i in range (0,100) if i % 3 !=0}

    # print(my_dict)

    # my_dict = {math.sqrt(i) for i in range (0,1000)} --->1  forma
    
    my_dict = {i: round(i**0.5,2) for i in range (0,1000)}

    print(my_dict)





if __name__ == '__main__':
    run()