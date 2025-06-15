#3. 🔢 **Even/Odd Number Checker**

# Vazifa Son kiritiladi, u **juft yoki toq**ligini aniqlaydi.
#Funksiya**: is_even(number)    → `True/False`

# print_even_message(number)

def is_even(number):
    if number %2 == 0:
        return True
    else:
        return False
    
number = int(input("number = "))
print(is_even(number))
        
        
        