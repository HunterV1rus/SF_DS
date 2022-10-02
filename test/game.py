import numpy as np

number = np.random.randint(1, 101)

count = 0

while True:
    count += 1
    predict_number = int(input("Guess from 1 to 100: "))
    
    if predict_number > number:
        print("lower!")
        
    elif predict_number < number:
        print("higher!")
        
    else:
        print(f"Guessed! it's number = {number}. shots = {count}")
        break