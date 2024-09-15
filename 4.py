def check_vowel_or_consonant(letter):
    vowels = 'aeiouAEIOU'
    
    if letter.isalpha() and len(letter) == 1:  
        if letter in vowels:
            print(f"{letter} is a vowel.")
        else:
            print(f"{letter} is a consonant.")
    else:
        print("Please input a valid single alphabet letter.")

letter = input("Input a letter of the alphabet: ")
check_vowel_or_consonant(letter)