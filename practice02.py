#2. Age Calculator

#Vazifa: Tug‘ilgan yilni kiritadi → hozirgi yildan yoshini hisoblab beradi.
# Funksiya calculate_age(birth_year, current_year)
# Qo‘shimcha: “Siz balog‘atga yetgansiz/yetmagansiz” degan javob chiqarsin.


def calculate_age(birth_year, current_year = 2025):
    #bu funksiya foydalanuvchi tugiilgan yilini kiritadi konpyuter unga voyaga yetgan 
                                               #     yetmaganligini chiqarib beradi
    result = current_year - birth_year
    
    if result < 18:
        return "Balog'atga yetmagan"
    else:
        return "Balog'otga yetgan" 
    
birth_year = int(input("tug'ilgan yilinggizni kiriting :"))    
print(calculate_age(birth_year))
    
    

    
    
    
     