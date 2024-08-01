
from scamp import *
s= Session()
piano = s.new_part('piano')
text = 'ffdggfggfhhfhbhfede ffdggfggfhhfhbhfede'
for char in text :
    if char=='':
        wait(0.1)
    else:
        wait(0.1)
        piano.play_note(ord(char) -30,0.8,0.2)
        wait(0.1)
        

'''
#-------------------------------------

 

from scamp import *
s=Session()
piano = s.new_part('piano')

def kb_listener (key, code):
    if len(key)==1:
        if key.isalnum():
            piano.play_note(ord(key)-20,6.8,0.06,blocking = False)
        else :
            piano.play_note(ord(key),6.0,0.06,blocking = False)

s.register_keyboard_listener(kb_listener)
s.wait_forever()

 '''
