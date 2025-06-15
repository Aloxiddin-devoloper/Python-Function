#Bonus 1: Simple ATM Simulation**

#Vazifa**: Foydalanuvchining balansi bor. U `deposit`, `withdraw` yoki `check balance` qiladi.
#Funksiyalar:  deposit(balance, amount)
#              withdraw(balance, amount)
#              check_balance(balance)
#   Primetivlar: `int`, `float`, `str`, `bool`

def deposit(balance, amount):
    if amount > 0:
        balance += amount
        print(f"{amount} so'm muvaffaqiyatli qo'shildi.")
    else:
        print("yaroqsiz miqdor!")
        
    return balance

def withdraw(balance, amount):
    if balance > amount:
        print("pul muvaffaqiyatli yechildi.")
    elif amount <= 0:
        print("yaroqsiz miqdor")
    else:
        print("Hisobinggizda mablag' yetarli emas .")
    return balance
    
def check_balance(balance):
    print(f"Hozirgi balans {balance} so'm.")

def main():
    balance = 0.0
    
    while True:
        print("\n === ATM Menyus ===")
        print("1 - balansni ko'rish")
        print(" 2 - pul qo'shish (deposit)")
        print("3 - pul yechish (withdraw)")
        print("4 - Chiqish")
        
        tanlov = input("Amalni tanlang (1-4):")
        
        if tanlov == "1":
            check_balance(balance)
        elif tanlov == "2":
            amout = float(input("Qo'shilgan summani kiriting :"))
            balance = deposit(balance,amout)
        elif tanlov == "3":
            amout = float(input("yechilgan summani kiriting :"))
            balance = withdraw(balance,amout)
        elif tanlov == "4":
            print("Dasturdan chiqildi. Xayr!")
            break
        else:
            print("noto'g'ri tanlov ! iltimos qaytadan urinib ko'ring.")

main()