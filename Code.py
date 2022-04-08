import time,random

def slow_print(str):
  for char in str:
    print(char, end='',flush=True)
    time.sleep(0.01)

def read(file,mode,list):
  f = open(file,mode)
  for line in f:
    data = line.split()
    list.append(data)

def split_list(list,new_list):
  for i in range(len(list)):
    for words in list[i]:
      new_list.append(words)

def choice_split(list,new_list):
  word = random.choice(list)
  for char in word:
    new_list.append(char)

def check_word(input,list,blanks,list2,list3):
  j = []
  for char in input:
    j.append(char)

  for i in range(len(list)):
    if j[i] in list[i]:
      blanks[i] = j[i]
    if j[i] not in list2 and list:
      if j[i] not in list[i] and j[i] not in list:
        list2.append(j[i])
    if j[i] not in list3 and list: 
      if j[i] in list and j[i] not in list[i]:
        list3.append(j[i])
    if i > len(list):
      break

def game():
  a = []
  words = []
  word = []
  blanks = [' _ ',' _ ',' _ ',' _ ',' _ ']
  wrong_placement = []
  wrong_letter = []
  wrong_word = True
  numb_guess = 0
  read('Words.txt','r',a)
  split_list(a,words)
  choice_split(words,word)

  slow_print("Welcome to Word Game!\n")
  slow_print("1) Play Game\n")
  slow_print("2) Quit Game\n")

  start = input("Choose one please!: ")

  if "1" in start:
    slow_print("Welcome to Word Game, Here are the rules:\n1) Take a guess at what the word could be\n2) If a letter is to the side then it means that it belongs in a different spot\n3) If a letter is in the wrong placement section that doesnt mean that there is only one of that letter\n4) If the letter stays in the same spot then you got the placement right\n\n")
    slow_print(blanks)
    while wrong_word == True:
      Guess = input("What is your guess:")
      numb_guess += 1
      check_word(Guess,word,blanks,wrong_letter,wrong_placement)
      slow_print(blanks)
      slow_print('\n')
      slow_print('Wrong Placement: ')
      slow_print(wrong_placement)
      slow_print('\n')
      slow_print('Wrong Letters: ')
      slow_print(wrong_letter)
      slow_print('\n')
      if numb_guess > 5:
        wrong_word = False
        slow_print("Sorry You ran out of Guesses. Try again")
      if blanks == word:
        wrong_word = False
        slow_print('Congratualtions You beat Word Game! :)')

  if "2" in start:
    slow_print("Wow . . . Okay, Fine, Dont Play the game I put time and effort into. . . . . . Jerk :(\n")
game()
