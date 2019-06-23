# import GPIO library
import gpiozero as gpio
# play musics and images
import pygame
from pygame.locals import *
# search of directorys
import os
import os.path as pathfinder
# thread import
from time import sleep

#
#   RPI buttons Connections
#
button1 = gpio.Button(0)
button2 = gpio.Button(1)
button3 = gpio.Button(5)

# GUI initial creation width, height(position x, position y)
window = pygame.display.set_mode((480,320), pygame.FULLSCREEN)

#
# function to go to initial screen is played first.
#
def startScn():
    # load image of initial screen
    image = pygame.image.load('/home/pi/dank/InitialScn.jpg')
    i = pygame.transform.scale(image, (480, 320))
    window.blit(i, (0,0))
    pygame.display.flip()
    pygame.display.update()
    return

#
# function what do the actions in button
#
def action(button):
    # 
    # files preparation in python OS library
    #

    mp3 = []
    jpg = []
    for dirname, subdir, filelist in os.walk('/home/pi/dank/'+button , topdown=False):
        print('Found directory: %s' %dirname)
        for file in filelist:
            if '.jpg' in file:
                jpg.append( pygame.image.load( pathfinder.join(dirname, file) ) )
            if '.mp3' in file:
                mp3.append( pathfinder.join(dirname, file) )

    #
    # Sound code in pygame
    #
    pygame.mixer.init() #start code
    pygame.mixer.music.load(mp3[0])
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1.0)
    
    # run while music is playing
    while pygame.mixer.music.get_busy() == True:
        for i in jpg:
            #
            # Image code in pygame
            # image tratment
            i = pygame.transform.scale(i, (480, 320))
            # blit parameters: (image, (position x, position y))
            window.blit(i, (0,0))
            # screen update
            pygame.display.flip()
            pygame.display.update()
                
            # if end the audi going to the start screen
            if pygame.mixer.music.get_busy() == 0:
                startScn()
                break
                break
            
            # wait 6s
            sleep(6)
    # end of while      
    
# end of function

startScn()

# always run to get the things
while True :

    # button actions
    if button1.is_pressed:
        print('button 1 is pressed')
        
        action('1')
    # end of button 1

    # buttons as the same thing
    if button2.is_pressed :
        print('button 2 is pressed')

        action('2')
    # end of button 2

    if button3.is_pressed :
        print('button 3 is pressed')
        
        action('3')
    # end of button 3

#end of while