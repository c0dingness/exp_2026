from colorama import Fore, Back, Style

print('....')
print(Fore.RED + 'some red text')
print(Back.BLACK + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

import random
print(random.random(1,1000))