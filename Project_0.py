import random
import numpy as np
def game_core_v2(number):
    
    '''задаём счетчик и загадываем рандомное число и ряда 1 - 100'''
    count = 1      
    predict = np.random.randint(1,101)  
    '''задаём переменные для границ, тк будем их изменять дальше'''
    border1 = 1      
    border2 = 101
    
    '''алгоритм поиска, где числа при попытке угадать, 
        становятся верхней и нижней границей, при неудаче.
        диапазон сужается
    '''
    while predict != number:
        count+=1
        if number > predict:
            border1 = predict # фиксируется нижняя граница
            
        elif number < predict: 
            border2 = predict # фиксируется верхняя граница
        predict = int(np.random.randint(border1,border2)) #генерируем число для следующей попытки нового цикла
    
    return(count) # выход из цикла, если угадали


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    
    return(score)

score_game(game_core_v2)