from collections import deque

def is_palindrome(s):
    # Видалення всіх символів, які не є буквами чи цифрами та перетворення рядка у нижній регістр
    s = ''.join(ch.lower() for ch in s if ch.isalnum())
    # Створення двосторонньої черги та додавання символів рядка
    char_queue = deque(s)
    # Порівняння символів з обох кінців черги
    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False
    return True

# Приклад використання
input_string = input("Введіть рядок для перевірки на паліндром: ")
if is_palindrome(input_string):
    print("Рядок є паліндромом")
else:
    print("Рядок не є паліндромом")
