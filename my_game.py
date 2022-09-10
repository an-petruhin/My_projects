"""Игра Угадай число"""

import numpy as np


def prediction(number: int = 1) -> int:
    """Функция принимает загаданное число и возвращает количество попыток, которое ушло на то, чтобы отгадать его.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Количество попыток
    """
    
    # Зададим счетчик попыток (count), левую (left) и правую (right) границы диапазона поиска
    count, left, right = 0, 1, 100
    
    while True:
        predict_number = np.random.randint(left, right + 1) # предполагаемое число
        count += 1
    
        if predict_number == number: 
            return count    # функция возвращает количество попыток, если число угадано
    
        elif predict_number < number:
            left = predict_number   # если предпогалаемое число меньше загаданного, предполагаемое число становится левой границей диапазона поиска
    
        elif predict_number > number:
            right = predict_number  # если предпогалаемое число больше загаданного, предполагаемое число становится правой границей диапазона поиска


def mean_score(func, n: int = 1000) -> int:
    """Функция возвращает среднее количество попыток угадать число для n чисел

    Args:
        func (_type_): Функция угадывания числа.
        n (int, optional): Количество чисел. Defaults to 1000.

    Returns:
        int: Среднее количество попыток угадать число.
    """
    
    score_list = []
    
    random_list = np.random.randint(1, 101, size=(n)) # Загадываем спсок чисел от 1 до 100 из 1000 элементов
    
    for num in random_list:
        score_list.append(func(num))

    score = int(np.mean(score_list))
    print(f'Алгоритм угадывает число в среднем за {score} попыток')
    return score


if __name__ == "__main__":
    mean_score(prediction)
