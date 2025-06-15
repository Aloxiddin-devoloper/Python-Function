#Palindrome Checker (faqat str bilan)**

#Vazifa: So‘z kiritiladi → teskari o‘qiganda ham bir xilmi, yo‘qmi tekshiriladi.
#Funksiya: is_palindrome(text: str) -> bool`
#Bu yerda slicing (`[::-1]`) ishlatiladi, lekin list emas!

def is_palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False

text = input("Textni kiriting :")
print(is_palindrome(text))



