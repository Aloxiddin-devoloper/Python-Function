#Calculator (Kalkulyator)**

#* **Vazifa**: Foydalanuvchi son va amalni kiritadi: `+`, `-`, `*`, `/`
#* **Funksiyalar**:
#* **Qamrab oladi**: funksiya, `if`, `input/output`, `return`, primitive types

def add(a, b):
    result = a + b
    return result

def subtract(a, b):
    resut = a - b
    return resut

def multiply(a, b):
    result = a * b
    return result

def divide(a, b):
    result = a / b
    return result


print(add(3,4))

def main():
    a = int(input("a = "))
    op = input("(+,-,*,/) = ")
    b = int(input("b = "))
    
    if op == "+":
        print(add(a,b))
    elif op == "-":
        print(subtract(a,b))
    elif op == "*":
        print(multiply(a,b))
    elif op == "/":
        print(divide(a,b))
    else:
        print("error")
        
main()