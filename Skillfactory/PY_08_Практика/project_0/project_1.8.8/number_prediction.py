"""Game: Guess the number
Computer sets number and guesses it buy itself
"""

import numpy as np
import statistics

def random_predict(number:int=np.random.randint(1, 101)) -> int:
    """Guessing random number

    Args:
        number (int, optional): Number to guess. Randomly the computer chooses from 1 to 100 

    Returns:
        int: number of tries 
    """
    print(f"Your number:{number}")
    count = 0
    lst_num = list(range(1, 101))

    while True:
      count += 1
      predict_number = int(np.mean(lst_num))
      half = round(int(len(lst_num))/2)
      if number == predict_number:
        break
      elif predict_number < number:
        lst_num = lst_num[half:]  
      else:
        lst_num = lst_num[:half]
      if len(lst_num) == 0:
        break

    return count

print(f"Amount of tries: {random_predict()}") 