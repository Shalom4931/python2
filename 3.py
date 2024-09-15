n = int(input("Input a dog's age in human years:"))
dog_age=0

for i in range(n):
    if i == 0 or i == 1 :
        dog_age +=10.5
    else:
        dog_age +=4
print ("The dog's age in dog's years is " , dog_age)
