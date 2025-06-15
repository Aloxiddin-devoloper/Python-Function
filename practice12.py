#Bonus 4: BMI Calculator (Body Mass Index)

#Vazifa: Og‘irlik va bo‘y kiritiladi → BMI va uning holati (`normal`, `overweight`) chiqadi.
#Funksiya: calculate_bmi(weight: float, height: float) -> float`
#          bmi_status(bmi: float) -> str`


def calculate_bmi(weight: float, height: float):
    bmi = weight/pow(height,2)
    return bmi

def bmi_status(bmi):
    if 18.5 <= bmi <= 24.9:
        return "Normal"
    elif 25.0 <= bmi <= 29.9:
        return "overweight"
    
def main():
    try:
        weight = float(input("Vazninggizni kiriting : "))
        height = float(input("Bo'yinggizni kiriting : "))
        
        bmi = calculate_bmi(weight,height)
        status = bmi_status(bmi)
        
        print(f"Sizning bmi = {bmi:.2f}")
        print(f"sizning holatinggiz = {status}")
        
    except ValueError:
        print("iltimos raqamni to'g'ri kiriting!")

main()
        

