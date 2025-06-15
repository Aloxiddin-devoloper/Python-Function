#6. 📞 **Phone Number Validator**

#Vazifa: Telefon raqam 9 ta raqamdan iboratligini tekshiradi.
#Funksiya:  is_valid_phone_number(phone: str) → `True/False

def is_valid_phone_number(phone):
    if len(phone) == 9:
        return True
    else:
        return False
    
phone = input("phone = ")
print(is_valid_phone_number(phone))
    

    
