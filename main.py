from random import randint

attemps=10

#Make Random 
answer_1 = randint(0,9) #OK

while(True):
  answer_2 = randint(0,9) 
  if (answer_2==answer_1):
    answer_2 = randint(0,9)
  else:
    break
    
while(True):
  answer_3 = randint(0,9)
  if (answer_3==answer_1) or (answer_3==answer_2):
    answer_3 = randint(0,9)
  else:
    break


while(True):
  #0. make answer and user input array
  print("print 777 to reveal answer.")
  
  answer = [answer_1,answer_2,answer_3]
  user_input = [0, 0, 0]
  
  #1. get 3 number from user
  while(True):
    user_input[0] = int(input("Type your first number:"))
    if(user_input[0] < 0 ) or (user_input[0] >= 10):
      print("your number has to be bigger than 0 and smaller than 10")
    else: #everything OK!!
      break
      
  
  while(True):
    user_input[1] = int(input("Type   your second number:"))
    if(user_input[1] < 0 ) or   (user_input[1] >= 10):
      print("your number has to be bigger than 0 and smaller than 10")
    else: #everything OK!!
      break
  
  
  while(True):
    user_input[2] = int(input("Type   your third number:"))
    if(user_input[2] < 0 ) or   (user_input[2] >= 10):
      print("your number has to be bigger than 0 and smaller than 10")
    else: #everything OK!!
      break
  
  print(user_input)
  
  #1. 777 is print answer
  if (user_input[0] == 7 and user_input[1] == 7 and user_input[2] == 7):
      print("answer is " + str(answer))
  #2. user input check!! -> if same number, error!!
  elif (user_input[0] == user_input[1]) or (user_input[1] == user_input[2]) or (
          user_input[2] == user_input[0]):
      print("you can't print the same number twice.")
  #3. Make base ball Algoruthm
  else:
      ball_count = 0
      strike_count = 0
  
      #JBSong's Algorithm
  
      #user_input[0] check
      if (user_input[0] == answer[0]):
          strike_count = strike_count + 1
      elif (user_input[0] == answer[1] or user_input[0] == answer[2]):
          ball_count = ball_count + 1
  
      #user_input[1] check
      if (user_input[1] == answer[1]):
          strike_count = strike_count + 1
      elif (user_input[1] == answer[0] or user_input[1] == answer[2]):
          ball_count = ball_count + 1
  
      #user_input[2] check
      if (user_input[2] == answer[2]):
          strike_count = strike_count + 1
      elif (user_input[2] == answer[0] or user_input[2] == answer[1]):
          ball_count = ball_count + 1
      '''
    #Danwoo's Algorithm
    if(user_input[0] ==answer[0] or user_input[0] == answer[1] or user_input[0]== answer[2]):
      ball_count = ball_count+1
  
    if(user_input[1] == answer[0] or user_input[1] == answer[1] or user_input[1]== answer[2]):
      ball_count = ball_count+1
      
    if(user_input[2] == answer[0] or   user_input[2] == answer[1] or user_input[2]== answer[2]):
      ball_count = ball_count+1
  
    if(user_input[0]) == answer[0]:
      strike_count=strike_count+1
      ball_count=ball_count-1
    
    if(user_input[1]) == answer[1]:
      strike_count=strike_count+1
      ball_count=ball_count-1
  
    if(user_input[2]) == answer[2]:
      strike_count=strike_count+1
      ball_count=ball_count-1
    '''
  
      print("ball:" + str(ball_count))
      print("strike:" + str(strike_count))
      attemps=attemps-1
    
      print("you got " + str(attemps)+ " amount of turns left")

      #Game Over Condition
      if (attemps==0):
        print("game over!")
        break

      #Su
      if (strike_count==3):  
        print("**** congragulation! you got the answer!****")
        break