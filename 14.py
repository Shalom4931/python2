def calculate_sum_and_average():
    total_sum = 0
    count = 0
    
    while True:
        num = int(input("Enter a number (Input 0 to finish): "))
        
        if num == 0:
            break
        
        total_sum += num
        count += 1
    
    if count > 0:
        average = total_sum / count
        print(f"Sum: {total_sum}, Average: {average:.2f}")
    else:
        print("No numbers were entered.")

calculate_sum_and_average()