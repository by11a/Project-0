"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def smart_predict(number: int = 1) -> int:
    """Угадываем число методом бинарного поиска

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0  # счетчик попыток
    low = 1  # нижняя граница диапазона поиска
    high = 100  # верхняя граница диапазона поиска

    while True:
        count += 1  # увеличиваем счетчик попыток
        predict_number = (low + high) // 2  # выбираем середину диапазона
        if predict_number == number:
            break  # если угадали, выходим из цикла
        elif predict_number < number:
            low = predict_number + 1  # сдвигаем нижнюю границу вверх
        else:
            high = predict_number - 1  # сдвигаем верхнюю границу вниз
    return count  # возвращаем количество попыток


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict (function): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    # np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=1000)  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)