def get_integer():
    while True:
        try:
            n = int(input("Введите целое число: "))
            return n
        except ValueError:
            print("Ошибка: пожалуйста, введите корректное целое число.")

def is_even(n):
    return n % 2 == 0

def even_product(n):
    product = 1
    for i in range(2, n + 1, 2):  # шаг 2 — только четные числа
        product *= i
    return product

def print_multiplication_table(n):
    print(f"\nТаблица умножения для {n}:")
    for i in range(1, 11):
        print(f"{n} × {i} = {n * i}")

def main():
    n = get_integer()

    print("\nПроверка на четность:")
    if is_even(n):
        print(f"Число {n} является чётным.")
    else:
        print(f"Число {n} является нечётным.")

    print("\nПроизведение всех чётных чисел от 1 до", n if is_even(n) else n - 1)
    product = even_product(n if is_even(n) else n - 1)
    print("Результат:", product)

    print_multiplication_table(n)

if __name__ == "__main__":
    main()
