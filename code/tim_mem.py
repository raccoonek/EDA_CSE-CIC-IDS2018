
import psutil

# Функция для замера использования ресурсов
def print_memory_usage():
    process = psutil.Process()
    mem_info = process.memory_info()

    print(f"Peak Memory Usage: {mem_info.vms / (1024 ** 2):.2f} MB")  # Пиковое использование памяти

def print_cpu_usage():
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")  # Процент использования CPU


