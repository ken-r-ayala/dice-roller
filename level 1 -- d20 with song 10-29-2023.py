import I2C_LCD_driver
from time import *
import utime

from machine import Pin, PWM
import random

from utime import sleep, sleep_ms

speaker = PWM(Pin(15))

# FF7 Victory theme:
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






# Link opening a chest sound:
def play_link_song():

    speaker.freq(880)
    speaker.duty_u16(15000);
    sleep_ms(600);

    speaker.freq(932)
    speaker.duty_u16(15000);
    sleep_ms(600);

    speaker.freq(988)
    speaker.duty_u16(15000);
    sleep_ms(600);

    speaker.freq(1047)
    speaker.duty_u16(15000);
    sleep_ms(600);


    speaker.duty_u16(15000);
    sleep_ms(600);

    speaker.duty_u16(0);



# Chrono Trigger Victory song:
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
    
    speaker.freq(1175)
    speaker.duty_u16(0);
    sleep_ms(900);
    
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
    

button_enter = machine.Pin(10, Pin.OUT, Pin.PULL_DOWN)
button_enter.value(0)

d20 = random.randint(1,20)

mylcd = I2C_LCD_driver.lcd()
mylcd.lcd_display_string("D20 ROLLER      ", 1)
mylcd.lcd_display_string("PRESS BUTTON    ", 2)

while True:
    if button_enter.value() == 0:
        utime.sleep(.01)
        if button_enter.value() == 1:
            utime.sleep(.01)
            mylcd.lcd_display_string("     <" + str(d20) + ">      ", 1)
            mylcd.lcd_display_string("PRESS BUTTON    ", 2)
            if d20 == 20:
                x = random.randint(1,3)
                if x == 1:
                    play_ff7_song()
                elif x == 2:
                    play_link_song()
                elif x == 3:
                    play_chrono_song()
                else:
                    continue
            elif d20 == 1:
                play_critfail_song()
            else:
                continue
        else:
            continue
    else:
        continue