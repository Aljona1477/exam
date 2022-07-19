# 2. Напишите функцию, которая проверяет: является ли слово палиндромом
# 3. Решите задачу

def palindrome(slovo):
    if len(slovo) <= 1:
        return True
    if slovo[0]!= slovo[-1]:
        return False
    else:
        return palindrome(slovo[1:-1])
print(palindrome('шабаш'))

