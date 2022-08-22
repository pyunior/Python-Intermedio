def run():
    # squares = []
    # for i in range(1,101):
    #     squares.append(i**2)
        
    # print(squares)
    
    # cuadrado de los numeros que no son divisibles entre 3 
    # squares = []
    # for i in range(1,101):
    #     if i % 3 !=0:
    #         squares.append(i**2)
        
    # print(squares)
    
    # en este codigo la division entre 3 no debe ser exacta , ya que si 
    # da como resto un cero 0, quiere decir que es divisible entre 3 y es lo que no queremos.
    
    
    # otra forma de hacerlo en una sola linea de codigo, con list comprehention
    squares= [i**2 for i in range(0,100) if i % 3 != 0 ]
    
    print(squares)
    
    # [element for element in iterable if condition]
     
    



if __name__ == '__main__':
    run()