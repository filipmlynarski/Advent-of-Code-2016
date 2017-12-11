import os
import time
from pymouse import PyMouse
m = PyMouse()
'''
m.position() #gets mouse current position coordinates
m.move(x,y)
m.click(x,y) #the third argument "1" represents the mouse button
m.press(x,y) #mouse button press
m.release(x,y) #mouse button release
'''
if not os.path.isfile('wymiary.txt'):
	file = open('wymiary.txt', 'w')
	raw_input('Po wcisnieciu Enter, najedz na przycisk ekwipunek/chat i czekaj ok 2s')
	time.sleep(3)
	chat = m.position()
	file.write('Chat\n' + chat + '\n')

os.system('rm wymiary.txt')