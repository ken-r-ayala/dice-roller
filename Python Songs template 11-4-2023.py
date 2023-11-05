from machine import Pin, PWM
import random

from utime import sleep, sleep_ms

speaker = PWM(Pin(15))

#A List of various notes and tones

# a = speaker.freq(440)
# a_sharp = speaker.freq(466)
# b = speaker.freq(494)
# c = speaker.freq(523)
# c_sharp = speaker.freq(554)
# d = speaker.freq(587)
# d_sharp = speaker.freq(622)
# e = speaker.freq(659) 
# f = speaker.freq(698)
# f_sharp = speaker.freq(740)
# g = speaker.freq(784)
# g_sharp = speaker.freq(831)
# a_high = speaker.freq(880)
# a_sharp_high = speaker.freq(932)
# b_high = speaker.freq(988)
# c_high = speaker.freq(1047)
# c_sharp_high = speaker.freq(1109)
# d_high = speaker.freq(1175)
# d_sharp_high = speaker.freq(1245)
# e_high = speaker.freq(1319)
# f_high = speaker.freq(1397)
# f_sharp_high = speaker.freq(1480)
# g_high = speaker.freq(1568)
# g_sharp_high = speaker.freq(1661)

#Chrono Trigger Victory Song
def play_chrono_song():
    speaker.freq(740)
    speaker.duty_u16(15000);
    sleep_ms(350);

    speaker.freq(740)
    speaker.duty_u16(0);
    sleep_ms(50);


    speaker.freq(740)
    speaker.duty_u16(15000);
    sleep_ms(150);

    speaker.freq(740)
    speaker.duty_u16(0);
    sleep_ms(50);


    speaker.freq(740)
    speaker.duty_u16(15000);
    sleep_ms(150);

    speaker.freq(740)
    speaker.duty_u16(0);
    sleep_ms(50);


    speaker.freq(659)
    speaker.duty_u16(15000);
    sleep_ms(150);

    speaker.freq(659)
    speaker.duty_u16(0);
    sleep_ms(50);


    speaker.freq(740)
    speaker.duty_u16(15000);
    sleep_ms(150);

    speaker.freq(740)
    speaker.duty_u16(0);
    sleep_ms(50);

    speaker.freq(784)
    speaker.duty_u16(15000);
    sleep_ms(350);

    speaker.freq(784)
    speaker.duty_u16(0);
    sleep_ms(50);

    speaker.freq(784)
    speaker.duty_u16(15000);
    sleep_ms(150);

    speaker.freq(784)
    speaker.duty_u16(0);
    sleep_ms(50);

    speaker.freq(784)
    speaker.duty_u16(15000);
    sleep_ms(150);

    speaker.freq(784)
    speaker.duty_u16(0);
    sleep_ms(50);

    speaker.freq(740)
    speaker.duty_u16(15000);
    sleep_ms(150);

    speaker.freq(740)
    speaker.duty_u16(0);
    sleep_ms(50);

    speaker.freq(784)
    speaker.duty_u16(15000);
    sleep_ms(150);

    speaker.freq(784)
    speaker.duty_u16(0);
    sleep_ms(50);

    speaker.freq(880)
    speaker.duty_u16(15000);
    sleep_ms(350);

    speaker.freq(880)
    speaker.duty_u16(0);
    sleep_ms(50);

    speaker.freq(1175)
    speaker.duty_u16(15000);
    sleep_ms(150);

    speaker.freq(1175)
    speaker.duty_u16(0);
    sleep_ms(50);

    speaker.freq(1175)
    speaker.duty_u16(15000);
    sleep_ms(850);

    speaker.freq(1175)
    speaker.duty_u16(0);
    sleep_ms(50);


    speaker.freq(1047)
    speaker.duty_u16(15000);
    sleep_ms(150);

    speaker.freq(1047)
    speaker.duty_u16(0);
    sleep_ms(50);


    speaker.freq(1047)
    speaker.duty_u16(15000);
    sleep_ms(150);

    speaker.freq(1047)
    speaker.duty_u16(0);
    sleep_ms(50);


    speaker.freq(1047)
    speaker.duty_u16(15000);
    sleep_ms(150);

    speaker.freq(1047)
    speaker.duty_u16(0);
    sleep_ms(50);

    speaker.freq(1175)
    speaker.duty_u16(15000);
    sleep_ms(900);

    speaker.duty_u16(0);
    sleep_ms(600)

#FF7 Victory theme
def play_ff7_song(): 
    speaker.freq(1319)
    speaker.duty_u16(15000);
    sleep_ms(150);
    speaker.duty_u16(0);
    sleep_ms(50);

        
    speaker.freq(1319)
    speaker.duty_u16(15000);
    sleep_ms(150);
    speaker.duty_u16(0);
    sleep_ms(50);

    speaker.freq(1319)
    speaker.duty_u16(15000);
    sleep_ms(150);
    speaker.duty_u16(0);
    sleep_ms(50);
        
    speaker.freq(1319)
    speaker.duty_u16(15000);
    sleep_ms(600);
    speaker.duty_u16(0);

    speaker.freq(1047)
    speaker.duty_u16(15000);
    sleep_ms(600);
    speaker.duty_u16(0);


    speaker.freq(1175)
    speaker.duty_u16(15000);
    sleep_ms(600);
    speaker.duty_u16(0);


    speaker.freq(1319)
    speaker.duty_u16(15000);
    sleep_ms(400);    
    speaker.duty_u16(0);
        
    speaker.freq(1175)
    speaker.duty_u16(15000);
    sleep_ms(200);
    speaker.duty_u16(0);

    speaker.freq(1319)
    speaker.duty_u16(15000);
    sleep_ms(600);
    speaker.duty_u16(0);

#Link opening a chest sound:
def play_link_song():

    speaker.freq(880)
    speaker.duty_u16(15000);
    sleep_ms(250);

    speaker.freq(932)
    speaker.duty_u16(15000);
    sleep_ms(250);

    speaker.freq(988)
    speaker.duty_u16(15000);
    sleep_ms(250);

    speaker.freq(1047)
    speaker.duty_u16(15000);
    sleep_ms(250);


    speaker.duty_u16(15000);
    sleep_ms(750);

    speaker.duty_u16(0);

def play_critfail_song():
    speaker.freq(988)
    speaker.duty_u16(15000);
    sleep_ms(300);

    speaker.freq(740)
    speaker.duty_u16(15000);
    sleep_ms(300);
    
    speaker.freq(494)
    speaker.duty_u16(15000);
    sleep_ms(150);
    
    speaker.freq(740)
    speaker.duty_u16(15000);
    sleep_ms(300);
    
    speaker.freq(1109)
    speaker.duty_u16(15000);
    sleep_ms(300);
    
    speaker.freq(1010)
    speaker.duty_u16(15000);
    sleep_ms(50);
    
    speaker.freq(980)
    speaker.duty_u16(15000);
    sleep_ms(50);
    
    speaker.freq(950)
    speaker.duty_u16(15000);
    sleep_ms(50);
    
    speaker.freq(920)
    speaker.duty_u16(15000);
    sleep_ms(50);
    
    speaker.freq(890)
    speaker.duty_u16(15000);
    sleep_ms(50);
    
    speaker.freq(860)
    speaker.duty_u16(15000);
    sleep_ms(50);
    
    speaker.freq(830)
    speaker.duty_u16(15000);
    sleep_ms(50);
    
    speaker.freq(800)
    speaker.duty_u16(15000);
    sleep_ms(50);
    
    speaker.freq(770)
    speaker.duty_u16(15000);
    sleep_ms(50);
    
    speaker.freq(740)
    speaker.duty_u16(15000);
    sleep_ms(50);
    
    speaker.freq(710)
    speaker.duty_u16(15000);
    sleep_ms(50);
    
    speaker.freq(680)
    speaker.duty_u16(15000);
    sleep_ms(50);
    
    speaker.freq(650)
    speaker.duty_u16(15000);
    sleep_ms(50);
    
    speaker.freq(620)
    speaker.duty_u16(15000);
    sleep_ms(50);
    
    speaker.freq(590)
    speaker.duty_u16(15000);
    sleep_ms(50);
    
    speaker.freq(560)
    speaker.duty_u16(15000);
    sleep_ms(50);
    
    speaker.freq(530)
    speaker.duty_u16(15000);
    sleep_ms(50);
    
    speaker.freq(500)
    speaker.duty_u16(15000);
    sleep_ms(50);
    
    speaker.freq(470)
    speaker.duty_u16(15000);
    sleep_ms(50);
    
    speaker.freq(440)
    speaker.duty_u16(15000);
    sleep_ms(50);
 
    speaker.freq(440)
    speaker.duty_u16(0);
    sleep_ms(300);

#Kill Bill "Danger!" song
def play_killbill_song():
    note_x = 784
    for i in range (1,420):
        speaker.freq(note_x)
        speaker.duty_u16(15000);
        sleep_ms(2);
        note_x = note_x + 2

    speaker.freq(note_x)
    speaker.duty_u16(0);
    sleep_ms(200);

    for i in range (1,420):
        speaker.freq(note_x)
        speaker.duty_u16(15000);
        sleep_ms(2);
        note_x = note_x - 2

    speaker.freq(note_x)
    speaker.duty_u16(0);
    sleep_ms(200);

    note_x = 784
    note_y = 1245

    for i in range (1,420):
        speaker.freq(note_x)
        speaker.duty_u16(15000);
        sleep_ms(2);
        note_x = note_x + 2

    speaker.freq(note_x)
    speaker.duty_u16(0);
    sleep_ms(200);

    for i in range (1,420):
        speaker.freq(note_x)
        speaker.duty_u16(15000);
        sleep_ms(2);
        note_x = note_x - 2

    speaker.freq(note_x)
    speaker.duty_u16(0);
    sleep_ms(250);

    speaker.freq(784)#G
    speaker.duty_u16(15000);
    sleep_ms(550);

    speaker.freq(784)#G
    speaker.duty_u16(0);
    sleep_ms(50);

    speaker.freq(932)#A-sharp
    speaker.duty_u16(15000);
    sleep_ms(250);

    speaker.freq(932)
    speaker.duty_u16(0);
    sleep_ms(50);

    speaker.freq(880)#A
    speaker.duty_u16(15000);
    sleep_ms(550);

    speaker.freq(880)
    speaker.duty_u16(0);
    sleep_ms(50);

    speaker.freq(698)#F
    speaker.duty_u16(15000);
    sleep_ms(250);

    speaker.freq(698)
    speaker.duty_u16(0);
    sleep_ms(50);

    speaker.freq(784)#G
    speaker.duty_u16(15000);
    sleep_ms(250);

    speaker.freq(784)
    speaker.duty_u16(0);
    sleep_ms(350);
        
    speaker.freq(880)#A
    speaker.duty_u16(15000);
    sleep_ms(950);

    speaker.freq(880)
    speaker.duty_u16(0);
    sleep_ms(50);

    speaker.freq(note_x)
    speaker.duty_u16(0);
    sleep_ms(5);

#Imperial March song
def play_vader_song():
    speaker.freq(784)
    speaker.duty_u16(15000);
    sleep_ms(750);
    
    speaker.freq(784)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(784)
    speaker.duty_u16(15000);
    sleep_ms(750);
    
    speaker.freq(784)
    speaker.duty_u16(0);
    sleep_ms(50);

    speaker.freq(784)
    speaker.duty_u16(15000);
    sleep_ms(750);
    
    speaker.freq(784)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(622)
    speaker.duty_u16(15000);
    sleep_ms(550);

    speaker.freq(622)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(932)
    speaker.duty_u16(15000);
    sleep_ms(150);

    speaker.freq(932)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(784)
    speaker.duty_u16(15000);
    sleep_ms(750);
    
    speaker.freq(784)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(622)
    speaker.duty_u16(15000);
    sleep_ms(550);

    speaker.freq(622)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(932)
    speaker.duty_u16(15000);
    sleep_ms(150);

    speaker.freq(932)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(784)
    speaker.duty_u16(15000);
    sleep_ms(950);
    
    speaker.freq(784)
    speaker.duty_u16(0);
    sleep_ms(50);

#Beethoven's 5th Symphony
def play_beethoven_song():
    speaker.freq(784)#G
    speaker.duty_u16(15000);
    sleep_ms(150);
    
    speaker.freq(784)#G
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(784)#G
    speaker.duty_u16(15000);
    sleep_ms(150);
    
    speaker.freq(784)#G
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(784)#G
    speaker.duty_u16(15000);
    sleep_ms(150);
    
    speaker.freq(784)#G
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(622)#D-sharp
    speaker.duty_u16(15000);
    sleep_ms(2500);
    
    speaker.freq(622)#D-sharp
    speaker.duty_u16(0);
    sleep_ms(1000);
    
    speaker.freq(698)#F
    speaker.duty_u16(15000);
    sleep_ms(150);
    
    speaker.freq(698)#F
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(698)#F
    speaker.duty_u16(15000);
    sleep_ms(150);
    
    speaker.freq(698)#F
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(698)#F
    speaker.duty_u16(15000);
    sleep_ms(150);
    
    speaker.freq(698)#F
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(587)#D
    speaker.duty_u16(15000);
    sleep_ms(2500);
    
    speaker.freq(587)#D
    speaker.duty_u16(0);
    sleep_ms(1000);
    

#Dramatic music
def play_dramatic_song():
    
    speaker.freq(1245)
    speaker.duty_u16(15000);
    sleep_ms(650);
    
    speaker.freq(1245)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    
    speaker.freq(1047)
    speaker.duty_u16(15000);
    sleep_ms(650);
    
    speaker.freq(1047)
    speaker.duty_u16(0);
    sleep_ms(50);

    note_x = 740
    note_y = 1480
    note_z = 1047
    for i in range (1,175):
        speaker.freq(note_x)
        speaker.duty_u16(15000);
        sleep_ms(6);
        speaker.freq(note_y)
        speaker.duty_u16(15000);
        sleep_ms(6);
        speaker.freq(note_z)
        speaker.duty_u16(15000);
        sleep_ms(6);
    speaker.freq(740)
    speaker.duty_u16(0);
    sleep_ms(50);
    


#Hallelujah song
def play_hallelujah_song():
    speaker.freq(1245)#E-flat
    speaker.duty_u16(15000);
    sleep_ms(850);
    
    speaker.freq(1245)
    speaker.duty_u16(0);
    sleep_ms(50);

    speaker.freq(932)#A-sharp
    speaker.duty_u16(15000);
    sleep_ms(250);
    
    speaker.freq(932)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(1047)#C
    speaker.duty_u16(15000);
    sleep_ms(250);
    
    speaker.freq(1047)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(932)#A-sharp
    speaker.duty_u16(15000);
    sleep_ms(250);
    
    speaker.freq(932)
    speaker.duty_u16(0);
    sleep_ms(650);

    speaker.freq(1245)#E-flat
    speaker.duty_u16(15000);
    sleep_ms(850);
    
    speaker.freq(1245)
    speaker.duty_u16(0);
    sleep_ms(50);

    speaker.freq(932)#A-sharp
    speaker.duty_u16(15000);
    sleep_ms(250);
    
    speaker.freq(932)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(1047)#C
    speaker.duty_u16(15000);
    sleep_ms(250);
    
    speaker.freq(1047)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(932)#A-sharp
    speaker.duty_u16(15000);
    sleep_ms(250);
    
    speaker.freq(932)
    speaker.duty_u16(0);
    sleep_ms(350);
    
    speaker.freq(932)#A-sharp
    speaker.duty_u16(15000);
    sleep_ms(100);
    
    speaker.freq(932)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(932)#A-sharp
    speaker.duty_u16(15000);
    sleep_ms(100);
    
    speaker.freq(932)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(1047)#C
    speaker.duty_u16(15000);
    sleep_ms(250);
    
    speaker.freq(1047)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(932)#A-sharp
    speaker.duty_u16(15000);
    sleep_ms(250);
    
    speaker.freq(932)
    speaker.duty_u16(0);
    sleep_ms(350);
    
    speaker.freq(932)#A-sharp
    speaker.duty_u16(15000);
    sleep_ms(100);
    
    speaker.freq(932)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(932)#A-sharp
    speaker.duty_u16(15000);
    sleep_ms(100);
    
    speaker.freq(932)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(1047)#C
    speaker.duty_u16(15000);
    sleep_ms(250);
    
    speaker.freq(1047)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(932)#A-sharp
    speaker.duty_u16(15000);
    sleep_ms(250);
    
    speaker.freq(932)
    speaker.duty_u16(0);
    sleep_ms(350);
    
    speaker.freq(932)#A-sharp
    speaker.duty_u16(15000);
    sleep_ms(100);
    
    speaker.freq(932)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(932)#A-sharp
    speaker.duty_u16(15000);
    sleep_ms(100);
    
    speaker.freq(932)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(1047)#C
    speaker.duty_u16(15000);
    sleep_ms(250);
    
    speaker.freq(1047)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(932)#A-sharp
    speaker.duty_u16(15000);
    sleep_ms(250);
    
    speaker.freq(932)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(831)#G-sharp
    speaker.duty_u16(15000);
    sleep_ms(550);
    
    speaker.freq(831)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(784)#G
    speaker.duty_u16(15000);
    sleep_ms(750);

    speaker.freq(784)#G
    speaker.duty_u16(0);
    sleep_ms(50);


x = 9      #insert number of desired song here

if x == 1:
    play_chrono_song()
elif x == 2:
    play_ff7_song()
elif x == 3:
    play_link_song()
elif x == 4:
    play_critfail_song()
elif x == 5:
    play_killbill_song()
elif x == 6:
    play_vader_song()
elif x == 7:
    play_beethoven_song()
elif x == 8:
    play_dramatic_song()
elif x == 9:
    play_hallelujah_song()

