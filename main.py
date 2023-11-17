# * Project-1 Snake, Water and Gun
import random
def game(com,user):
    if com=="s" and user=="w":
        print("computer choose : snake")
        print("you choose : water")
        print("you loose ")
    elif com=="s" and user=="g":
        print("computer choose : snake")
        print("you choose : gun ")
        print(" you win ")
    elif com=="s" and user=="s":
        print("computer choose : snake")
        print("you choose : snake ")
        print(" game draw ")
    elif com=="w" and user=="s":
        print("computer choose : water")
        print("you choose : snake ")
        print(" you win ")
    elif com=="w" and user=="g":
        print("computer choose : water")
        print("you choose : gun ")
        print(" you loose ")
    elif com=="w" and user=="w":
        print("computer choose : water")
        print("you choose : water ")
        print("match draw")
    elif com=="g" and user=="s":
        print("computer choose : gun")
        print("you choose : snake ")
        print("you loose")
    elif com=="g" and user=="w":
        print("computer choose : gun")
        print("you choose : water ")
        print("you win")
    elif com=="g" and user=="g":
        print("computer choose : gun")
        print("you choose : water ")
        print("match draw")

print("computer turn : sanke(s) water(w) or gun(g):")

com= random.randint(1,3)
if com==1:
    com='s'
elif com==2:
    com=='w'
elif com==3:
    com=='g'

user=input("Your turn : snake(s) water(w) or gun(g) : ")

game(com,user)