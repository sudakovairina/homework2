import numpy as np

def random_predict(number: int = 1) -> int:
    """Компьютер угадывает число

    Args: number - Загаданное число. Defaults to 1.

    Returns: count - Число попыток
    """
    count = 0
    st =1 # левое значение для рандома
    fin = 101 # правое значение для рандома
    
    while True:
        count += 1
        predict_number = np.random.randint(st, fin)  # предполагаемое число
        
        # регулируем правое значения для рандома
        if predict_number > number:
            fin = predict_number
        # регулируем левое значение для рандома
        if predict_number < number:
            st = predict_number
        
        if number == predict_number:
            break  # выход из цикла если угадали
        #print("number", number, "predict_number",predict_number, "st", st, "fin", fin)
    return count

#print(random_predict(9))

def score_game(random_predict) -> int:
    """Считаем среднее количество попыток, за которое компьютер угадывает число
    
    Args:  random_predict() - аргументом функция, угадывающая число   

    Return: score - среднее количество попыток для списка из 1000 чисел 
    """
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел, которые будем угадывать

    for number in random_array:
        # вызываем функцию угадывания числа для каждого сгенеренного
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)