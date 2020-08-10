#Script Python --- 3. Decida por mim

#Importação do módulo random e choice
import random 
from random import choice 

#Criação de uma base de respostas 

answers = ['Sim', 'Não', 'Não sei', 'Acho que sim', 'Talvez', 'Pode-ser','Hoje não','Melhor não', 

'Totalmente sim', 'Impossível', 'É possível', 'Vai sim', 'Acho melhor deixar de lado', 'Acho', 

'melhor ir em frente', 'Boa sorte', 'Boa ideia', 'Esquece', 'Siga seu coração', 'Pode ser que sim ou pode ser que não', 'Continue tentando', 'Vai com tudo' ]

#print(f'Até o momento você definiu {len(answers)} respostas para as perguntas')

#definir uma função que gere repostas aleatórias para as perguntas

def generate_answers(lista):
    random_answers = random.choice(lista)
    print (random_answers)

#Tela inicial  do jogo

message_initial = 'BEM-VINDO(A) AO DECIDA POR MIM\n'
centralize = message_initial.center(115)

print (centralize)

starting = input('Para iniciar digite [i]\n'
           'Para sair digite [s]\n')
while starting == 'i':
    question = input('\nFaça me uma pergunta:\n')
    generate_answers(answers)
else:
    print ('Fim de jogo')

