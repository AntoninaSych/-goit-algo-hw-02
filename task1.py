import queue
import random
import time

# Створення черги заявок
request_queue = queue.Queue()

# Функція для генерації нових заявок
def generate_request():
    request_id = random.randint(1, 1000)
    request_queue.put(request_id)
    print(f"Заявка {request_id} додана до черги")

# Функція для обробки заявок
def process_request():
    if not request_queue.empty():
        request_id = request_queue.get()
        print(f"Заявка {request_id} оброблена")
    else:
        print("Черга порожня")

# Головний цикл програми
while True:
    # Генерація нових заявок
    generate_request()
    # Обробка заявок
    process_request()
    # Затримка перед наступною ітерацією
    time.sleep(1)
