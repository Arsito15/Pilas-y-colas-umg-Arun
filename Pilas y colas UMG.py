import random
import time
import queue

def generate_numbers(num):
    numbers = []
    for i in range(num):
        numbers.append(random.randint(-10000000, 10000000))
    return numbers

def process_with_stack(numbers):
    start_time = time.time()
    stack = []
    for num in numbers:
        stack.append(num)
    while stack:
        num = stack.pop()
    end_time = time.time()
    return end_time - start_time

def process_with_queue(numbers):
    start_time = time.time()
    q = queue.Queue()
    for num in numbers:
        q.put(num)
    while not q.empty():
        num = q.get()
    end_time = time.time()
    return end_time - start_time

# Generar los numeros aleatorios
numbers = generate_numbers(1000000)

# Procesar usando una pila
print("Procesando con pila...")
stack_time = process_with_stack(numbers)
print("Tiempo de procesamiento con pila: {:.6f} segundos".format(stack_time))

# Procesar usando una cola
print("Procesando con cola...")
queue_time = process_with_queue(numbers)
print("Tiempo de procesamiento con cola: {:.6f} segundos".format(queue_time))
