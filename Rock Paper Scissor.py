import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
uc =''
cc= ''
user_input=int(input('Enter your choice(0: Rock   1: Paper   2: Scissor )'))
print('You Chose: ')
if user_input == 0:
    print(rock)
    uc = 'rock'
elif user_input==1:
    print(paper)
    uc = 'paper'
else:
    print(scissor)
    uc = 'scissor'

comp= random.randint(1,27)
if comp>=1 and comp <=9:
    print(paper)
    cc= 'paper'
if comp>9 and comp <=18:
    print(rock)
    cc= 'rock'
if comp>18 and comp <=27:
    print(scissor)
    cc='scissor'

if uc == 'rock' and cc == 'scissor':
    print('You win!')
if uc == 'rock' and cc == 'paper':
    print('Computer wins!')
if uc == 'paper' and cc == 'scissor':
    print('Computer wins!')
if uc == 'paper' and cc == 'rock':
    print('You win!')
if uc == 'scissor' and cc == 'rock':
    print('Computer wins!')
if uc == 'scissor' and cc == 'paper':
    print('You win!')
if uc == 'scissor' and cc == 'scissor':
    print('Tie! Nobody wins')
if uc == 'paper' and cc == 'paper':
    print('Tie! Nobody wins')
if uc == 'rock' and cc == 'rock':
    print('Tie! Nobody wins')