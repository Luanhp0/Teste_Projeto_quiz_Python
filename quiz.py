print("Seja muito bem vindo ao quiz do luan!")
answer_user = input("Quer comecar? (S/N)")


if answer_user != "S":
    quit()


score = 0


print("comecando...")
print("Quem desenvolvel o jogo Grand Theft Auto (GTA)? \n (A) Rockstar Games \n (B) Ubisoft \n (C) Activision \n (D) EA \n ")
anwser_1 = input("Resposta: ")

if anwser_1 == "A":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")    

print("Qual o nome do protagonista do jogo GTA San Andreas? \n (A) Carlos John \n (B) Carl Jonhson \n (C) Carl Jaqueline \n (D) Carlos Jonhson \n ")
anwser_1 = input("Resposta: ")

if anwser_1 == "B":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!") 

print(f"Quiz acabou... Pontuacao: {score}/2")