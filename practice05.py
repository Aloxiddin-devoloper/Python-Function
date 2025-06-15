#5. 🎲 **Number Guessing Game (Random ishlatilmaydi)**

#Vazifa: Kompyuterda sirli son mavjud. Foydalanuvchi taxmin qiladi. To‘g‘ri yoki xato deyilgan bo‘ladi.
#Funksiya:check_guess(secret, guess)
#print_result(is_correct)

def check_guess(secret,guess):
    result = secret == guess
    return result

def print_result(is_correct):
    if is_correct:
        print("to'g'ri topdinggiz")
    else:
        print("topaolmadinggiz")

secret = 65
guess = int(input("Sirli sonni kiriting : "))

is_correct = check_guess(secret,guess)
print_result(is_correct)