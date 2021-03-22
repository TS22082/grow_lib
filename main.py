from lib import DHT
from lib import LT

import inquirer
import sys

def main_menu():
  questions = [inquirer.List(
    'main_menu', 
    message="What would you like to do?", 
    choices=['Read from DHT22', 'Read from TSL2561', 'Show all Data', 'Exit'])]
  
  answer = inquirer.prompt(questions)

  if answer['main_menu'] == 'Read from DHT22': 
    DHT.display_data()
    main_menu()
  elif answer['main_menu'] == 'Read from TSL2561': 
    LT.display_data()
    main_menu()
  elif answer['main_menu'] == 'Show all Data':
    DHT.display_data() 
    LT.display_data()
    main_menu()
  elif answer['main_menu'] == 'Exit':
    print('Bye')
    sys.exit()
  else : print("unrecognized command"); main_menu()  

main_menu()


