import I2C_LCD_driver
from time import *
import utime

from machine import Pin, PWM
import random

from utime import sleep, sleep_ms

# This will set the default number of dice being rolled to 1 when the program initially starts.
dice_quantity = 1
# These values represent the various polyhedrals that you can roll.

# Note that there are certain limitations on certain dice types due to the character restriction on the I2C LCD display.

# With only 16 characters per line on 2 lines we can not, for instance, roll 10d10 and have it display properly, as having
# double-digit numbers on 5 dice per line may exceed the number of available characters and therefore may not display correctly.

dice_4 = 4
dice_6 = 6
dice_8 = 8
dice_10 = 10
dice_12 = 12
dice_20 = 20
dice_100 = 100

# When the program runs, it defaults to a D4 as the selected dice. This can be changed by pressing the "Right" button to
# cycle through the various options.

dice_type = dice_4
mylcd = I2C_LCD_driver.lcd()
mylcd.lcd_display_string("Dice Roller!    ", 1)
mylcd.lcd_display_string("Choose: <D" + str(dice_type) + ">    ", 2)

# These boolean values are in place to change the state of the program accordingly so you can cycle through various options such as
# the type and number of dice.

# These values will also be used to cycle through the program once you have rolled your dice so you may start over without cutting power
# to the unit or re-running the program manually.
dice_type_selected = False
dice_number_selected = False
dice_rolled = False
speaker = PWM(Pin(15))

# The following section is where we lay out the functions for the songs this program uses.

# More information can be found in the Document "Python Songs Template" in this repository, including a few example songs as well
# as the various frequencies used and what note they correlate to.


# FF7 Victory theme:
def play_ff7_song():
    mylcd.lcd_display_string("  CRITICAL!!!!  ", 2)
    speaker.freq(1319)
    speaker.duty_u16(15000);
    sleep_ms(150);
    speaker.duty_u16(0);
    sleep_ms(50);

    mylcd.lcd_display_string("                ", 2)
    speaker.freq(1319)
    speaker.duty_u16(15000);
    sleep_ms(150);
    speaker.duty_u16(0);
    sleep_ms(50);
    
    mylcd.lcd_display_string("  CRITICAL!!!!  ", 2)
    speaker.freq(1319)
    speaker.duty_u16(15000);
    sleep_ms(150);
    speaker.duty_u16(0);
    sleep_ms(50);

    mylcd.lcd_display_string("                ", 2)
    speaker.freq(1319)
    speaker.duty_u16(15000);
    sleep_ms(600);
    speaker.duty_u16(0);

    mylcd.lcd_display_string("  CRITICAL!!!!  ", 2)
    speaker.freq(1047)
    speaker.duty_u16(15000);
    sleep_ms(600);
    speaker.duty_u16(0);

    mylcd.lcd_display_string("                ", 2)
    speaker.freq(1175)
    speaker.duty_u16(15000);
    sleep_ms(600);
    speaker.duty_u16(0);

    mylcd.lcd_display_string("  CRITICAL!!!!  ", 2)
    speaker.freq(1319)
    speaker.duty_u16(15000);
    sleep_ms(400);    
    speaker.duty_u16(0);

    mylcd.lcd_display_string("                ", 2)
    speaker.freq(1175)
    speaker.duty_u16(15000);
    sleep_ms(200);
    speaker.duty_u16(0);

    mylcd.lcd_display_string("  CRITICAL!!!!  ", 2)
    speaker.freq(1319)
    speaker.duty_u16(15000);
    sleep_ms(600);
    speaker.duty_u16(0);

# Link opening a chest sound:
def play_link_song():
    mylcd.lcd_display_string("  CRITICAL!!!!  ", 2)
    speaker.freq(880)
    speaker.duty_u16(15000);
    sleep_ms(600);

    mylcd.lcd_display_string("                ", 2)
    speaker.freq(932)
    speaker.duty_u16(15000);
    sleep_ms(600);

    mylcd.lcd_display_string("  CRITICAL!!!!  ", 2)
    speaker.freq(988)
    speaker.duty_u16(15000);
    sleep_ms(600);

    mylcd.lcd_display_string("                ", 2)
    speaker.freq(1047)
    speaker.duty_u16(15000);
    sleep_ms(600);

    mylcd.lcd_display_string("  CRITICAL!!!!  ", 2)
    speaker.duty_u16(15000);
    sleep_ms(600);

    speaker.duty_u16(0);



# Chrono Trigger Victory song:
def play_chrono_song():
    mylcd.lcd_display_string("  CRITICAL!!!!  ", 2)
    speaker.freq(740)
    speaker.duty_u16(15000);
    sleep_ms(350);

    mylcd.lcd_display_string("                ", 2)
    speaker.freq(740)
    speaker.duty_u16(0);
    sleep_ms(50);

    mylcd.lcd_display_string("  CRITICAL!!!!  ", 2)
    speaker.freq(740)
    speaker.duty_u16(15000);
    sleep_ms(150);

    mylcd.lcd_display_string("                ", 2)
    speaker.freq(740)
    speaker.duty_u16(0);
    sleep_ms(50);

    mylcd.lcd_display_string("  CRITICAL!!!!  ", 2)
    speaker.freq(740)
    speaker.duty_u16(15000);
    sleep_ms(150);

    mylcd.lcd_display_string("                ", 2)
    speaker.freq(740)
    speaker.duty_u16(0);
    sleep_ms(50);

    mylcd.lcd_display_string("  CRITICAL!!!!  ", 2)
    speaker.freq(659)
    speaker.duty_u16(15000);
    sleep_ms(150);

    mylcd.lcd_display_string("                ", 2)
    speaker.freq(659)
    speaker.duty_u16(0);
    sleep_ms(50);

    mylcd.lcd_display_string("  CRITICAL!!!!  ", 2)
    speaker.freq(740)
    speaker.duty_u16(15000);
    sleep_ms(150);

    mylcd.lcd_display_string("                ", 2)
    speaker.freq(740)
    speaker.duty_u16(0);
    sleep_ms(50);

    mylcd.lcd_display_string("  CRITICAL!!!!  ", 2)
    speaker.freq(784)
    speaker.duty_u16(15000);
    sleep_ms(350);

    mylcd.lcd_display_string("                ", 2)
    speaker.freq(784)
    speaker.duty_u16(0);
    sleep_ms(50);

    mylcd.lcd_display_string("  CRITICAL!!!!  ", 2)
    speaker.freq(784)
    speaker.duty_u16(15000);
    sleep_ms(150);

    mylcd.lcd_display_string("                ", 2)
    speaker.freq(784)
    speaker.duty_u16(0);
    sleep_ms(50);

    mylcd.lcd_display_string("  CRITICAL!!!!  ", 2)
    speaker.freq(784)
    speaker.duty_u16(15000);
    sleep_ms(150);

    mylcd.lcd_display_string("                ", 2)
    speaker.freq(784)
    speaker.duty_u16(0);
    sleep_ms(50);

    mylcd.lcd_display_string("  CRITICAL!!!!  ", 2)
    speaker.freq(740)
    speaker.duty_u16(15000);
    sleep_ms(150);

    mylcd.lcd_display_string("                ", 2)
    speaker.freq(740)
    speaker.duty_u16(0);
    sleep_ms(50);

    mylcd.lcd_display_string("  CRITICAL!!!!  ", 2)
    speaker.freq(784)
    speaker.duty_u16(15000);
    sleep_ms(150);

    mylcd.lcd_display_string("                ", 2)
    speaker.freq(784)
    speaker.duty_u16(0);
    sleep_ms(50);

    mylcd.lcd_display_string("  CRITICAL!!!!  ", 2)
    speaker.freq(880)
    speaker.duty_u16(15000);
    sleep_ms(350);

    mylcd.lcd_display_string("                ", 2)
    speaker.freq(880)
    speaker.duty_u16(0);
    sleep_ms(50);

    mylcd.lcd_display_string("  CRITICAL!!!!  ", 2)
    speaker.freq(1175)
    speaker.duty_u16(15000);
    sleep_ms(150);

    mylcd.lcd_display_string("                ", 2)
    speaker.freq(1175)
    speaker.duty_u16(0);
    sleep_ms(50);

    mylcd.lcd_display_string("  CRITICAL!!!!  ", 2)
    speaker.freq(1175)
    speaker.duty_u16(15000);
    sleep_ms(850);

    mylcd.lcd_display_string("                ", 2)
    speaker.freq(1175)
    speaker.duty_u16(0);
    sleep_ms(50);

    mylcd.lcd_display_string("  CRITICAL!!!!  ", 2)
    speaker.freq(1047)
    speaker.duty_u16(15000);
    sleep_ms(150);

    mylcd.lcd_display_string("                ", 2)
    speaker.freq(1047)
    speaker.duty_u16(0);
    sleep_ms(50);

    mylcd.lcd_display_string("  CRITICAL!!!!  ", 2)
    speaker.freq(1047)
    speaker.duty_u16(15000);
    sleep_ms(150);

    mylcd.lcd_display_string("                ", 2)
    speaker.freq(1047)
    speaker.duty_u16(0);
    sleep_ms(50);

    mylcd.lcd_display_string("  CRITICAL!!!!  ", 2)
    speaker.freq(1047)
    speaker.duty_u16(15000);
    sleep_ms(150);

    mylcd.lcd_display_string("                ", 2)
    speaker.freq(1047)
    speaker.duty_u16(0);
    sleep_ms(50);

    mylcd.lcd_display_string("  CRITICAL!!!!  ", 2)
    speaker.freq(1175)
    speaker.duty_u16(15000);
    sleep_ms(900);
    
    speaker.freq(1175)
    speaker.duty_u16(0);
    sleep_ms(900);

# Failure song from "The Price Is Right":
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
    
# Kill Bill "Ironside Siren" sound:
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

    speaker.freq(784)
    speaker.duty_u16(15000);
    sleep_ms(550);

    speaker.freq(784)
    speaker.duty_u16(0);
    sleep_ms(50);

    speaker.freq(932)
    speaker.duty_u16(15000);
    sleep_ms(250);

    speaker.freq(932)
    speaker.duty_u16(0);
    sleep_ms(50);

    speaker.freq(880)
    speaker.duty_u16(15000);
    sleep_ms(550);

    speaker.freq(880)
    speaker.duty_u16(0);
    sleep_ms(50);

    speaker.freq(698)
    speaker.duty_u16(15000);
    sleep_ms(250);

    speaker.freq(698)
    speaker.duty_u16(0);
    sleep_ms(50);

    speaker.freq(784)
    speaker.duty_u16(15000);
    sleep_ms(250);

    speaker.freq(784)
    speaker.duty_u16(0);
    sleep_ms(350);
        
    speaker.freq(880)
    speaker.duty_u16(15000);
    sleep_ms(950);

    speaker.freq(880)
    speaker.duty_u16(0);
    sleep_ms(50);
    
# Dramatic sound:
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
    
# "Hallelujah!" song:
def play_hallelujah_song():
    speaker.freq(1245)
    speaker.duty_u16(15000);
    sleep_ms(850);
    
    speaker.freq(1245)
    speaker.duty_u16(0);
    sleep_ms(50);

    speaker.freq(932)
    speaker.duty_u16(15000);
    sleep_ms(250);
    
    speaker.freq(932)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(1047)
    speaker.duty_u16(15000);
    sleep_ms(250);
    
    speaker.freq(1047)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(932)
    speaker.duty_u16(15000);
    sleep_ms(250);
    
    speaker.freq(932)
    speaker.duty_u16(0);
    sleep_ms(650);

    speaker.freq(1245)
    speaker.duty_u16(15000);
    sleep_ms(850);
    
    speaker.freq(1245)
    speaker.duty_u16(0);
    sleep_ms(50);

    speaker.freq(932)
    speaker.duty_u16(15000);
    sleep_ms(250);
    
    speaker.freq(932)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(1047)
    speaker.duty_u16(15000);
    sleep_ms(250);
    
    speaker.freq(1047)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(932)
    speaker.duty_u16(15000);
    sleep_ms(250);
    
    speaker.freq(932)
    speaker.duty_u16(0);
    sleep_ms(350);
    
    speaker.freq(932)
    speaker.duty_u16(15000);
    sleep_ms(100);
    
    speaker.freq(932)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(932)
    speaker.duty_u16(15000);
    sleep_ms(100);
    
    speaker.freq(932)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(1047)
    speaker.duty_u16(15000);
    sleep_ms(250);
    
    speaker.freq(1047)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(932)
    speaker.duty_u16(15000);
    sleep_ms(250);
    
    speaker.freq(932)
    speaker.duty_u16(0);
    sleep_ms(350);
    
    speaker.freq(932)
    speaker.duty_u16(15000);
    sleep_ms(100);
    
    speaker.freq(932)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(932)
    speaker.duty_u16(15000);
    sleep_ms(100);
    
    speaker.freq(932)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(1047)
    speaker.duty_u16(15000);
    sleep_ms(250);
    
    speaker.freq(1047)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(932)
    speaker.duty_u16(15000);
    sleep_ms(250);
    
    speaker.freq(932)
    speaker.duty_u16(0);
    sleep_ms(350);
    
    speaker.freq(932)
    speaker.duty_u16(15000);
    sleep_ms(100);
    
    speaker.freq(932)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(932)
    speaker.duty_u16(15000);
    sleep_ms(100);
    
    speaker.freq(932)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(1047)
    speaker.duty_u16(15000);
    sleep_ms(250);
    
    speaker.freq(1047)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(932)
    speaker.duty_u16(15000);
    sleep_ms(250);
    
    speaker.freq(932)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(831)
    speaker.duty_u16(15000);
    sleep_ms(550);
    
    speaker.freq(831)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(784)
    speaker.duty_u16(15000);
    sleep_ms(750);

    speaker.freq(784)
    speaker.duty_u16(0);
    sleep_ms(50);
    
# Intro to Beethoven's 5th Symphony:
def play_beethoven_song():
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
    
    speaker.freq(784)
    speaker.duty_u16(15000);
    sleep_ms(150);
    
    speaker.freq(784)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(622)
    speaker.duty_u16(15000);
    sleep_ms(2500);
    
    speaker.freq(622)
    speaker.duty_u16(0);
    sleep_ms(1000);
    
    speaker.freq(698)
    speaker.duty_u16(15000);
    sleep_ms(150);
    
    speaker.freq(698)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(698)
    speaker.duty_u16(15000);
    sleep_ms(150);
    
    speaker.freq(698)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(698)
    speaker.duty_u16(15000);
    sleep_ms(150);
    
    speaker.freq(698)
    speaker.duty_u16(0);
    sleep_ms(50);
    
    speaker.freq(587)
    speaker.duty_u16(15000);
    sleep_ms(2500);
    
    speaker.freq(587)
    speaker.duty_u16(0);
    sleep_ms(1000);

# Here is where we will define the button values for both the Enter and Right buttons.

# Note that the Enter button is typically used to confirm a selection, and the Right button is typically used to cycle through the
# various options.

# Either button can be used to re-run the program from the beginning, once the dice have been selected and rolled.

button_enter = machine.Pin(10, Pin.OUT, Pin.PULL_DOWN)
button_enter.value(0)
button_right = machine.Pin(11, Pin.OUT, Pin.PULL_DOWN)
button_right.value(0)

# These functions represent the rolling of several different quantities of dice.

def roll_10d():
    d1 = random.randint(1,dice_type)
    d2 = random.randint(1,dice_type)
    d3 = random.randint(1,dice_type)
    d4 = random.randint(1,dice_type)
    d5 = random.randint(1,dice_type)
    d6 = random.randint(1,dice_type)
    d7 = random.randint(1,dice_type)
    d8 = random.randint(1,dice_type)
    d9 = random.randint(1,dice_type)
    d10 = random.randint(1,dice_type)
    mylcd.lcd_display_string("[" + str(d1) + "][" + str(d2) + "][" + str(d3) + "][" + str(d4) + "][" + str(d5) + "] ", 1)
    mylcd.lcd_display_string("[" + str(d6) + "][" + str(d7) + "][" + str(d8) + "][" + str(d9) + "][" + str(d10) + "] ", 2)

def roll_9d():
    d1 = random.randint(1,dice_type)
    d2 = random.randint(1,dice_type)
    d3 = random.randint(1,dice_type)
    d4 = random.randint(1,dice_type)
    d5 = random.randint(1,dice_type)
    d6 = random.randint(1,dice_type)
    d7 = random.randint(1,dice_type)
    d8 = random.randint(1,dice_type)
    d9 = random.randint(1,dice_type)
    mylcd.lcd_display_string("[" + str(d1) + "][" + str(d2) + "][" + str(d3) + "][" + str(d4) + "][" + str(d5) + "] ", 1)
    mylcd.lcd_display_string("[" + str(d6) + "][" + str(d7) + "][" + str(d8) + "][" + str(d9) + "]    ", 2)

def roll_8d():
    d1 = random.randint(1,dice_type)
    d2 = random.randint(1,dice_type)
    d3 = random.randint(1,dice_type)
    d4 = random.randint(1,dice_type)
    d5 = random.randint(1,dice_type)
    d6 = random.randint(1,dice_type)
    d7 = random.randint(1,dice_type)
    d8 = random.randint(1,dice_type)
    mylcd.lcd_display_string("[" + str(d1) + "][" + str(d2) + "][" + str(d3) + "][" + str(d4) + "]    ", 1)
    mylcd.lcd_display_string("[" + str(d5) + "][" + str(d6) + "][" + str(d7) + "][" + str(d8) + "]    ", 2)

def roll_7d():
    d1 = random.randint(1,dice_type)
    d2 = random.randint(1,dice_type)
    d3 = random.randint(1,dice_type)
    d4 = random.randint(1,dice_type)
    d5 = random.randint(1,dice_type)
    d6 = random.randint(1,dice_type)
    d7 = random.randint(1,dice_type)
    mylcd.lcd_display_string("[" + str(d1) + "][" + str(d2) + "][" + str(d3) + "][" + str(d4) + "]    ", 1)
    mylcd.lcd_display_string("[" + str(d5) + "][" + str(d6) + "][" + str(d7) + "]        ", 2)

def roll_6d():
    d1 = random.randint(1,dice_type)
    d2 = random.randint(1,dice_type)
    d3 = random.randint(1,dice_type)
    d4 = random.randint(1,dice_type)
    d5 = random.randint(1,dice_type)
    d6 = random.randint(1,dice_type)
    mylcd.lcd_display_string("[" + str(d1) + "][" + str(d2) + "][" + str(d3) + "]       ", 1)
    mylcd.lcd_display_string("[" + str(d4) + "][" + str(d5) + "][" + str(d6) + "]       ", 2)

def roll_5d():
    d1 = random.randint(1,dice_type)
    d2 = random.randint(1,dice_type)
    d3 = random.randint(1,dice_type)
    d4 = random.randint(1,dice_type)
    d5 = random.randint(1,dice_type)
    mylcd.lcd_display_string("[" + str(d1) + "][" + str(d2) + "][" + str(d3) + "]       ", 1)
    mylcd.lcd_display_string("[" + str(d4) + "][" + str(d5) + "]          ", 2)

def roll_4d():
    d1 = random.randint(1,dice_type)
    d2 = random.randint(1,dice_type)
    d3 = random.randint(1,dice_type)
    d4 = random.randint(1,dice_type)
    mylcd.lcd_display_string("[" + str(d1) + "][" + str(d2) + "]          ", 1)
    mylcd.lcd_display_string("[" + str(d3) + "][" + str(d4) + "]          ", 2)

def roll_3d():
    d1 = random.randint(1,dice_type)
    d2 = random.randint(1,dice_type)
    d3 = random.randint(1,dice_type)
    mylcd.lcd_display_string("[" + str(d1) + "][" + str(d2) + "]          ", 1)
    mylcd.lcd_display_string("[" + str(d3) + "]             ", 2)

def roll_2d():
    d1 = random.randint(1,dice_type)
    d2 = random.randint(1,dice_type)
    mylcd.lcd_display_string("[" + str(d1) + "]             ", 1)
    mylcd.lcd_display_string("[" + str(d2) + "]             ", 2)

def roll_1d():
    d1 = random.randint(1,dice_type)
    mylcd.lcd_display_string("[" + str(d1) + "]             ", 1)
    mylcd.lcd_display_string("                ", 2)
    if d1 == 20 and dice_type == dice_20 and dice_quantity == 1:
# This would be a critical success, and is one of the cases where a song would play celebrating your good luck.
        x = random.randint(1,3)
        if x == 1:
            play_ff7_song()
        elif x == 2:
            play_link_song()
        elif x == 3:
            play_chrono_song()
    elif d1 == 1 and dice_type == dice_20 and dice_quantity == 1:
# This would be a critical fail, and is one of the cases where a song would play an ominous tune foreshadowing your misfortune.
        mylcd.lcd_display_string("   Oh s#!t...   ", 2)
        x = random.randint(1,3)
        if x == 1:
            play_critfail_song()
        elif x == 2:
            play_killbill_song()
        elif x == 3:
            play_dramatic_song()
    elif d1 == 100 and dice_type == dice_100 and dice_quantity == 1:
# If you happen to roll a 100 on a D100 (it's happened to our game group before!), it certainly warrants a song to celebrate!
        mylcd.lcd_display_string("IT'S A MIRACLE!!", 2)
        play_hallelujah_song()
    elif d1 == 1 and dice_type == dice_100 and dice_quantity == 1:
# On the flip-side, if you happen to roll a 1 on a D100, that's just rotten luck! Still deserves a song, though -- albeit a foreboding one!
        mylcd.lcd_display_string("You done f'ed up", 2)
        play_beethoven_song()
# This is the While loop that allows the program to run.

# Within this loop, we have several different screens to cycle through:
# - the Dice Type selection Screen (which allows you to choose between a D4, D6, etc. all the way up through a D100
# - the Dice Quantity selection Screen, which allows you to roll several dice at once, within the limitations we will see later in this code
# - the Dice Roll Screen, which displays the values of the various dice you have rolled
while True:
    
    if button_right.value() == 1 and dice_type_selected == False and dice_number_selected == False and dice_rolled == False:
        utime.sleep(.5)
        if dice_type == dice_4:
            dice_type = dice_6
            mylcd.lcd_display_string("Choose: <D" + str(dice_type) + ">    ", 2)
        elif dice_type == dice_6:
            dice_type = dice_8
            mylcd.lcd_display_string("Choose: <D" + str(dice_type) + ">    ", 2)
        elif dice_type == dice_8:
            dice_type = dice_10
            mylcd.lcd_display_string("Choose: <D" + str(dice_type) + ">    ", 2)
        elif dice_type == dice_10:
            dice_type = dice_12
            mylcd.lcd_display_string("Choose: <D" + str(dice_type) + ">    ", 2)
        elif dice_type == dice_12:
            dice_type = dice_20
            mylcd.lcd_display_string("Choose: <D" + str(dice_type) + ">    ", 2)
        elif dice_type == dice_20:
            dice_type = dice_100
            mylcd.lcd_display_string("Choose: <D" + str(dice_type) + ">    ", 2)
        elif dice_type == dice_100:
            dice_type = dice_4
            mylcd.lcd_display_string("Choose: <D" + str(dice_type) + ">    ", 2)
    elif button_enter.value() == 1 and dice_type_selected == False and dice_number_selected == False and dice_rolled == False:
        utime.sleep(.5)
        dice_type_selected = True
        mylcd.lcd_display_string(" How many Dice? ", 1)
        mylcd.lcd_display_string("       " + str(dice_quantity) + "        ", 2)
# What follows are the various limitations we need to implement to ensure the results display properly and also so that our
# songs will play under the right conditions.
# The limitations listed here are as follows:
# - if the dice is a D20, you can only roll 1 of them. This is by design as it allows us to play songs when either a 1 or a 20 is rolled
#   (this limitation may be lifted in a future iteration should we do a 3rd revision of this Dice Roller program.)
# - if the dice is a D100, you can only roll 1 of them. This is because there is a possibility of displaying 3 characters per dice roll, and
#   also to allow us to play a song on a result of either a 1 or a 100.
# - if the dice is either a D12 or a D10, you can only roll up to 8 of them. This is due to the aforementioned display restrictions combined
#   with the potential for having a result that is 2 digits.
# - lastly, if the dice is a D4, D6, or D8, you can only roll up to 10 of them. This is also due to the display restrictions.
    elif button_right.value() == 1 and dice_type_selected == True and dice_number_selected == False and dice_rolled == False:
        if dice_type == dice_20 and dice_quantity == 1:
            mylcd.lcd_display_string("       " + str(dice_quantity) + "        ", 2)
        elif dice_type == dice_100 and dice_quantity > 1:
            mylcd.lcd_display_string("       " + str(dice_quantity) + "        ", 2)
        elif dice_type == dice_12 and dice_quantity == 8:
            mylcd.lcd_display_string("       " + str(dice_quantity) + "        ", 2)
        elif dice_type == dice_12 and dice_quantity <= 7:
            dice_quantity = dice_quantity + 1
            utime.sleep(.5)
            mylcd.lcd_display_string("       " + str(dice_quantity) + "        ", 2)
        elif dice_type == dice_10 and dice_quantity == 8:   
            mylcd.lcd_display_string("       " + str(dice_quantity) + "        ", 2)
        elif dice_type == dice_10 and dice_quantity <= 7:
            dice_quantity = dice_quantity + 1
            utime.sleep(.5)
            mylcd.lcd_display_string("       " + str(dice_quantity) + "        ", 2)
        elif dice_type < 10 and dice_quantity == 10:
            mylcd.lcd_display_string("       " + str(dice_quantity) + "        ", 2)
        elif dice_quantity < 10 and dice_type < 10:
            dice_quantity = dice_quantity + 1
            utime.sleep(.5)
            mylcd.lcd_display_string(" How many Dice? ", 1)
            mylcd.lcd_display_string("       " + str(dice_quantity) + "        ", 2)
    elif button_enter.value() == 1 and dice_type_selected == True and dice_number_selected == False and dice_rolled == False:
        utime.sleep(.5)
        dice_number_selected = True
        dice_rolled = True
# This section is where a function runs based on the number and type of dice you have selected and displays the results accordingly.
        if dice_quantity == 1:
            roll_1d()
        elif dice_quantity == 2:
            roll_2d()
        elif dice_quantity == 3:
            roll_3d()
        elif dice_quantity == 4:
            roll_4d()
        elif dice_quantity == 5:
            roll_5d()
        elif dice_quantity == 6:
            roll_6d()
        elif dice_quantity == 7:
            roll_7d()
        elif dice_quantity == 8:
            roll_8d()
        elif dice_quantity == 9:
            roll_9d()
        elif dice_quantity == 10:
            roll_10d()
# The next two elif conditions are meant to reset the application to the beginning, regardless of whether you press the Enter
# button or the Right button.

# We accomplish this by resetting the boolean values for dice_type_selected and dice_number_selected to False, indicating that
# we must select both our dice type (D4, D6, etc.) as well as the number of dice we wish to roll.
    elif button_enter.value() == 1 and dice_type_selected == True and dice_number_selected == True and dice_rolled == True:
        utime.sleep(.5)
        dice_type_selected = False
        dice_number_selected = False
        dice_rolled = False
        dice_type = dice_4
        dice_quantity = 1
        mylcd.lcd_display_string("Dice Roller!    ", 1)
        mylcd.lcd_display_string("Choose: <D" + str(dice_type) + ">    ", 2)
    elif button_right.value() == 1 and dice_type_selected == True and dice_number_selected == True and dice_rolled == True:
        utime.sleep(.5)
        dice_type_selected = False
        dice_number_selected = False
        dice_rolled = False
        dice_type = dice_4
        dice_quantity = 1
        mylcd.lcd_display_string("Dice Roller!    ", 1)
        mylcd.lcd_display_string("Choose: <D" + str(dice_type) + ">     ", 2)
# This line simply allows the program to wait for you to press one of the buttons to begin the program.
    else:
        continue

            