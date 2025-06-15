#Bonus 2: Password Strength Checker**

#Vazifa: Parolni kiritadi, kuchli yoki kuchsizligini tekshiradi (masalan, uzunligi 8 dan katta bo‘lsa kuchli).
#Funksiya: is_strong_password(password: str) -> bool`
#Bu yerda `len()` funksiyasini ishlatish mumkin, lekin **list** ishlatilmaydi.


def is_strong_password(password):
    if len(password) >= 8:
        return "kuchli parol"
    else:
        return "kuchsiz parol"

password = input("Paswordni kiring :")
print(is_strong_password(password))