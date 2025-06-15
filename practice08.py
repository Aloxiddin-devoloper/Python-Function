#8. 🕹 **Temperature Converter**

#Vazifa: Celsius ↔ Fahrenheit aylantirish.
#Funksiya: c_to_f(celsius),   f_to_c(fahrenheit)


def c_to_f(celsius):
    
    return(celsius*9/5)+32


def f_to_c(fahrenheit) :
    
    return(fahrenheit-32)*5/9

c = float(input("celcius = "))
f = float(input("fahrenheit = "))

print(f"{c} C = {c_to_f(c)} F")
print(f"{c} F = {f_to_c(f)} C")
    
    