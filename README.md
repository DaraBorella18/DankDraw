# Dank Draw
A project to auxiliate people with Alzheimer's disease to remember things

### What is that?
Dank draw is a project idealized by Dara Karoliny de Oliveira and me in the college with the purpose of people with Alzheimer's disease can remember important things.
This consist of a cube where some things about the people, your family and anything can be remember using media players to display images and play audio tracks that help in a process to remember.

> This is a prototype and will be improved, 
[here is a picture of the prototype](readme_image.jpeg)

### Things needed
1. Display LCD 3.5" for Raspberry Pi
   - Amazon link: https://amzn.to/2Y7dDAa
   - Mercado Livre link: http://bit.ly/2KxPlMI

2. Raspberry Pi Model 3 B+
    - Amazon Link: http://bit.ly/2ZI1MsR
    - Mercado Livre link: http://bit.ly/2N5VaTy

3. A Sounb Box that will not use anymore

4. A PowerBank or (if you want) 2 Li-ion battery's 4,2V
   - I used a 2 batterys 18650 here's the link: http://bit.ly/31Op9mv

5. A lot of cables to connect then

## Step 1
- Copy the audio and images files to a new folder named: dank in **/home/pi/** on your raspbian system.
- Put the audio and images file in folder named 1,2,3 on **/home/pi/dank** and put main.py in the main folder.

## Step 2
 ! use that only if you need to start it before start the system if not, use: [this link and use the autostart method](https://learn.sparkfun.com/tutorials/how-to-run-a-raspberry-pi-program-on-startup#method-1-rclocal)
- modify rc.local using the terminal command:
  > sudo nano /etc/rc.local
- edit just before the exit 0 line adding the line
  > python /home/pi/dank/main.py

## Step 3
Connect the push buttons in the GPIO entrances  GPIO0 ,GPIO1 and GPIO5
and connect the sound box and the display.
if all works then:

## Step 4
- Open Terminal and type the commands

```
sudo rm -rf LCD-show

git clone https://github.com/goodtft/LCD-show.git

chmod -R 755 LCD-show

cd LCD-show/

sudo ./LCD35-show
```
- Restart the system and will be able to use the LCD display

>### In this docs you can search a [3D model to  the cube made in solid works](Piece.SLDPRT), in the future i put a circuit model and a step to recreate the cube
>### ! That's a college project and will be improve and better explained in the future !

*Programmed and auxiliate by [William Fabre](https://twitter.com/VaiSeF_Will)*
