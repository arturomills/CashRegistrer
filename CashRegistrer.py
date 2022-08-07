import numpy as np
import pandas as pd
import csv

start_menu = int(input('''Select One Option : '''))

look_prod = str(input("Enter a Product: "))


with open ('Database.csv', newline='\n', mode='r+') as db:
    Reader = csv.reader (db, delimiter=';')
    for rows in Reader:
        if look_prod == rows[0]:
            print(f'The Price of the Article Selected is {float(rows[3])}')

            


