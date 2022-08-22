def run():
    my_list = [1, True, "hello", 3.2]
    my_dicc = { "firtsname": "yunior" , "Lastname":"Puentes"}
    
    super_list = [
        { "firtsname": "yunior" , "Lastname":"Puentes"},
        { "firtsname": "yunior" , "Lastname":"Puentes"},
        { "firtsname": "yunior" , "Lastname":"Puentes"},
        { "firtsname": "yunior" , "Lastname":"Puentes"},
        { "firtsname": "yunior" , "Lastname":"Puentes"},
        { "firtsname": "yunior" , "Lastname":"Puentes"},
    ]
    
    super_dict = {
     "natural_nums" : [1, 2, 3, 4, 5,],
     "integer_nums" : [-1, -2],
     "floating_num" : [1.1, 1.2, 1.3],   
    }

    for key, value in super_dict.items():
        print(key, "-", value)

if __name__ == '__main__':
    run()