#Bonus 3: Tax Calculator**

#Vazifa: Maoshni kiritadi → soliqni hisoblab beradi.
#Funksiya:
#`calculate_tax(salary: float) -> float`
#`calculate_net_salary(salary: float) -> float`

#Moslashuvchan `if` bilan soliq stavkasi o‘zgarishi mumkin
#(masalan, >5mln bo‘lsa 20%, boshqacha 13%).


def calculate_tax(salary):
    if salary >= 5000000:
        tax = (salary*20)/100
        print(f"20 foiz soliq qo'lllanildi.")
    else:
        tax = (salary*13)/100
        print(f"13 foiz soliq qo'llanildi.")
        
    return tax
        

def calculate_net_salary(salary):
    tax = calculate_tax(salary)
    net_salary = salary - tax
    
    return net_salary
    
    

def main():
    try:
        salary = float(input("Maoshinggizni kiriting (so'mda): "))
        net = calculate_net_salary(salary)
        print(f"Sof maoshinggiz:{net} so'm") 
    except ValueError:
        print("Iltimos raqam kiriting!")
        
main()