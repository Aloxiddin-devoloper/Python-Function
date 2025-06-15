#4.Simple Grading System**

#Vazifa: Foydalanuvchi ball kiritadi → `A`, `B`, `C`, `F` baho qaytadi.
# ball>=90  A     70<=ball<90 B   60<=ball<70  C  60>ball  F
#Funksiya: get_grade(score)
# Qo‘llaniladigan narsa:  `if-elif-else`, `str`, `int`

def get_grade(score):
    
    if score >= 90:
        return "A"
    elif 70 <= score <90:
        return "B"
    elif 60 <= score < 70:
        return "C"
    elif score < 60:
        return "F"

score = float(input("score = "))
print(get_grade(score))