import os
def clear_screen():
    os.system('cls')


a = True

while a:
    jawab = input('Apakah ingin Lanjutkan? (y/n) :')
    if jawab == 'y' :
        print('Terimah Kasih')
        a = True
    elif jawab == 'n' :
        os.system('cls')
        print('Sampai Jumpa :D ')
        a = False
    else :
        print('Jangan Aneh Dehhh :))')
        a = True


