import random
input('Press enter to begin')

p1Name = input('Human player 1, enter your name: ')
p2Name = input('Human player 2, enter your name: ')
playerNames = p1Name[:11].center(11) + '    ' + p2Name[:11].center(11)

print('''HERE ARE TWO BOXES: 
       __________      __________
      /         / |   /         /|
     +---------+  |  +---------+ |
     |   RED   |  |  |   GOLD  | |
     |   BOX   | /   |   BOX   | /
     +---------+/    +---------+/''')
 
print()
print(playerNames)
 
print()

print(p1Name+ ' you have a RED box in front of you.')
print(p2Name+ ' you have a gold box in front of you. ')
print()
print(p1Name +', you will get to look into your box.')
print(p2Name.upper() + ', close your eyes and don\'t look!!! ')
print('When '+p2Name+' has closed their eyes, press Enter....')
input()
print()

print(p1Name +' here is the inside of your box:')

if random.randint(1,2) ==1:
    carrotInFirstBox = True
else:
    carrotInFirstBox = False 

if carrotInFirstBox:
    print('''
          ___VV____
         |   VV    |
         |   VV    |
         |___||____|     __________
         /    ||   /|   /         /|
        +---------+ |  +---------+ |
        |   RED   | |  |   GOLD  | |
        |   BOX   | /  |   BOX   | /
        +---------+/   +---------+/
         (carrot!)''')
    print(playerNames)
else:
    print('''
     _________
    |         |
    |         |
    |_________|    __________
   /         /|   /         /|
  +---------+ |  +---------+ |
  |   RED   | |  |   GOLD  | |
  |   BOX   | /  |   BOX   | /
  +---------+/   +---------+/
  (no carrot!)''')
    print(playerNames)
input('Press enter to continue...')

print('\n'*100)
print(p1Name+ ', tell '+p2Name +'to open their eyes.' )
print(' 1) There is carrot in my box')
print(' 2) There is not a carrot in my box')
print()
input('Then press Enter to continue...')
print()

print(p2Name+' do you want to swap your box with '+p1Name+' Yes/No')
while True:
    response = input('> ').upper()
    if not(response.startswith('Y') or response.startswith('N')):
        print(p2Name+', please enter "Yes" or "No" ')
    else:
        break
firstBox = 'RED '
secondBox = 'GOLD'

if response.startswith('Y'):
    carrotInFirstBox = not carrotInFirstBox
    firstBox, secondBox = secondBox,firstBox
    
print(''' Here are the two boxes: 
   __________     __________
  /         /|   /         /|
 +---------+ |  +---------+ |
 |   {}  | |  |   {}  | |
 |   BOX   | /  |   BOX   | /
 +---------+/   +---------+/'''.format(firstBox, secondBox))
print(playerNames)
 
input('Press enter to reveal the winner')
print()

if carrotInFirstBox:
    print('''
    ___VV____      _________
   |   VV    |    |         |
   |   VV    |    |         |
   |___||____|    |_________|
  /    ||   /|   /         /|
 +---------+ |  +---------+ |
 |   {}  | |  |   {}  | |
 |   BOX   | /  |   BOX   | /
 +---------+/   +---------+/'''.format(firstBox, secondBox))   

else:
    print('''
    _________      ___VV____
   |         |    |   VV    |
   |         |    |   VV    |
   |_________|    |___||____|
  /         /|   /    ||   /|
 +---------+ |  +---------+ |
 |   {}  | |  |   {}  | |
 |   BOX   | /  |   BOX   | /
 +---------+/   +---------+/'''.format(firstBox, secondBox))
    
print(playerNames)
 
if carrotInFirstBox:
     print(p1Name +' is the winner!')
else:
     print(p2Name +' is the winner!' )
     
print('Thanks for playing')
