def print_pattern_R():
    n = 7  
    for i in range(n):
        if i== 0 or i == 3: 
            print("****")
        elif i < 3:  
            print("*    *")
        elif i == 4:  
            print("* *")
        elif i == 5:  
            print("*   *")
        else : 
            print("*    *")

print_pattern_R() 