# Моделирование работы сети кафе с несколькими столиками и потоком посетителей,
# прибывающих для заказа пищи и уходящих после завершения приема.
#
# Есть сеть кафе с несколькими столиками. Посетители приходят, заказывают еду,
# занимают столик, употребляют еду и уходят. Если столик свободен,
# новый посетитель принимается к обслуживанию, иначе он становится в очередь на ожидание.
#
# Создайте 3 класса:
#
# Table - класс для столов, который будет содержать следующие атрибуты:
# number(int) - номер стола, is_busy(bool) - занят стол или нет.
#
# Cafe - класс для симуляции процессов в кафе. Должен содержать следующие атрибуты и методы:
# 1. Атрибуты queue - очередь посетителей (создаётся внутри init), tables список столов (поступает из вне).
# 2. Метод customer_arrival(self) - моделирует приход посетителя(каждую секунду).
# 3. Метод serve_customer(self, customer) - моделирует обслуживание посетителя.
# Проверяет наличие свободных столов, в случае наличия стола - начинает обслуживание посетителя (запуск потока),
# в противном случае - посетитель поступает в очередь. Время обслуживания 5 секунд.
#
# Customer - класс (поток) посетителя. Запускается, если есть свободные столы.
#
# Так же должны выводиться текстовые сообщения соответствующие событиям:
# 1. Посетитель номер <номер посетителя> прибыл.
# 2. Посетитель номер <номер посетителя> сел за стол <номер стола>. (начало обслуживания)
# 3. Посетитель номер <номер посетителя> покушал и ушёл. (конец обслуживания)
# 4. Посетитель номер <номер посетителя> ожидает свободный стол. (помещение в очередь)


import threading
import time
import queue
from collections import defaultdict

class Table:

    def __init__(self, number: int):
        self.number = number
        self.is_busy = False

class Cafe:     # - класс для симуляции процессов в кафе.

    def __init__(self, tables):
        self.tables = tables
        self.queue = []
        #self.customer = customer

    def customer_arrival(self):    # - моделирует приход посетителя(каждую секунду).
        customer_num = 1
        for customer_num in range(1, 21):   # - кол-во посетителей
            print(f"Посетитель номер {customer_num} прибыл.")
            self.serve_customer(Customer(customer_num, self))
            customer_num += 1
            time.sleep(0.5)
        if customer_num >= 20:
            print("Все поели! Кафе закрывается!")

    def serve_customer(self, customer):     # - моделирует обслуживание посетителя.
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print(f"Посетитель номер {customer.number} сел за стол {table.number}.")
                time.sleep(0.5)
                print(f"Посетитель номер {customer.number} покушал и ушёл.")
                table.is_busy = True
                return
        self.queue.append(customer)
        print(f"Посетитель номер {customer.number} ожидает свободный стол.")


class Customer(threading.Thread):

    def __init__(self, number, cafe):
        threading.Thread.__init__(self)
        self.number = number
        self.cafe = cafe

    def run(self):
        self.cafe.serve_customer(self)




table1 = Table(1)     # Создаем столики в кафе
table2 = Table(2)
table3 = Table(3)
table4 = Table(4)
table5 = Table(5)
table6 = Table(6)
tables = [table1, table2, table3, table4, table5, table6]

cafe = Cafe(tables)      # Инициализируем кафе

customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)   # Запускаем поток для прибытия посетителей
customer_arrival_thread.start()

customer_arrival_thread.join()   # Ожидаем завершения работы прибытия посетителей



