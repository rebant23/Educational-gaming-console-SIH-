from time import sleep
from machine import Pin
from gpio_lcd import GpioLcd
from rotary_irq_rp2 import RotaryIRQ

# Create the LCD object
lcd = GpioLcd(rs_pin=Pin(13),
              enable_pin=Pin(12),
              d4_pin=Pin(4),
              d5_pin=Pin(2),
              d6_pin=Pin(1),
              d7_pin=Pin(0),
              num_lines=4, num_columns=20)
# Rotary encoder pins
clk1 = Pin(8, Pin.IN, Pin.PULL_UP)
dt1 = Pin(7, Pin.IN, Pin.PULL_UP)
clk2 = Pin(9, Pin.IN, Pin.PULL_UP)
dt2 = Pin(11, Pin.IN, Pin.PULL_UP)
sw2=Pin(10,Pin.IN,Pin.PULL_UP)
sw1=Pin(6,Pin.IN,Pin.PULL_UP)
lcd.clear
# Variables
alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
counter = 0
last_state = clk1.value()
last_state2=clk2.value()
# Display the initial letter on the LCD
# lcd.move_to(0,0)
# lcd.putstr("What is the capital")
# lcd.move_to(0,1)
# lcd.putstr("of USA:")
# lcd.move_to(0, 3)
# lcd.putstr(alphabet[counter])
# pos=0
str=""
pos = 0
counter=0
string="123456789"
# def rotary_interrupt(pin):
#     """Interrupt handler for rotary encoder"""
#     global pos
#     global counter
#     counter=0
#     if dt1.value():  # If DT is high, rotation is clockwise
#         pos += 1
#     else:           # If DT is low, rotation is counterclockwise
#         if pos>=1:
#             pos -= 1
# def rotary_interrupt1(pin):
#     """Interrupt handler for rotary encoder"""
#     global counter
#     if counter<0:
#         counter=26
#     if dt2.value():  # If DT is high, rotation is clockwise
#         if counter>=1:
#             counter -= 1
#     else:           # If DT is low, rotation is counterclockwise
#         counter += 1
r1 = RotaryIRQ(pin_num_clk=8,
              pin_num_dt=7,
              min_val=0,
              max_val=100,
              reverse=False,
              range_mode=RotaryIRQ.RANGE_WRAP)
r2 = RotaryIRQ(pin_num_clk=9,
              pin_num_dt=11,
              min_val=0,
              max_val=100,
              reverse=False,
              range_mode=RotaryIRQ.RANGE_WRAP)

def sw1_interrupt(pin):
    global counter
    global pos
    global n
    global answer
    global stri
    global flag
    global flag1
    global menu
    global game1
    global game2
    global game3
    global setting
    global ascr
    if menu==1:
        if (r1.value())%4==0:
            menu=0
            game1=1
            game2=0
            game3=0
            setting=0
            lcd.clear()
            sleep(0.05)
        if (r1.value())%4==1:
            menu=0
            game1=0
            game2=1
            game3=0
            setting=0
            lcd.clear()
            sleep(0.05)
        if (r1.value())%4==2:
            menu=0
            game1=0
            game2=0
            game3=1
            setting=0
            lcd.clear()
            sleep(0.05)
        if (r1.value())%4==3:
            menu=0
            game1=0
            game2=0
            game3=0
            setting=1
            lcd.clear()
            sleep(0.05)
            
    if game1==1:
        flag=1        
        stri_list = list(stri)  # Convert stri to a list
        stri_list[n] = alphabet[(r2.value()) % 26]  # Modify the list
        stri = ''.join(stri_list)  # Convert the list back to a string
            
        if flag1==1:
            l=0
            right=0
            while l<len(stri):
                if stri[l]!=answer[l]:
                    right=1
                l=l+1
            if right==0:
                lcd.clear()
                lcd.putstr("Correct Answer",0,0)
                ascr=1
                flag1=0
            else :
                lcd.clear()
                lcd.putstr("Wrong Answer",0,0)
                ascr=1
                flag1=0
            
        
    if game2==1:
        if (r2.value())%5==2:
            lcd.clear()
            lcd.putstr("Correct answer",0,0)
            ascr=1
        else:
            lcd.clear()
            lcd.putstr("Wrong answer",0,0)
            ascr=1
            
def sw2_interrupt(pin):
    global counter
    global pos
    global game1
    global menu
    global game2
    global game3
    global setting
    global ascr
    if game1==1:
        if ascr==0:
            menu=1
            game1=0
    if game2==1:
        if ascr==0:
            menu=1
            game2=0
        else:
            ascr=0
    if game3==1:
        menu=1
        game3=0
    if setting==1:
        setting=0
        menu=1

# Attach interrupt to CLK pin
# clk1.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=rotary_interrupt)
# clk2.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=rotary_interrupt1)
sw1.irq(trigger=Pin.IRQ_FALLING,handler=sw1_interrupt)
sw2.irq(trigger=Pin.IRQ_FALLING,handler=sw2_interrupt)

flag1=0
menu=1
game1=0
game2=0
game3=0
setting=0
ascr=0
flag=0
string=""
stri="De_l_"
answer="Dehli"
# r1->pos
# r2-> counter
while True:
    if menu==1:
        pos=0
        counter=0
        lcd.clear()
        lcd.putstr("One word answers",1,0)
        lcd.putstr("MCQ",1,1)
        lcd.putstr("Game 3",1,2)
        lcd.putstr("Settings",1,3)
        pos=0
        while menu!=0:
            lcd.putstr(" ",0,0)
            lcd.putstr(" ",0,1)
            lcd.putstr(" ",0,2)
            lcd.putstr(" ",0,3)
            lcd.putstr(">",0,(r1.value())%4)
            sleep(0.2)
        
    if game1==1 and ascr==0:
#         lcd.clear()
        lcd.putstr("What is the capital",0,0)
        lcd.putstr("of India:",0,1)
        stri="DE_H_"
        answer="DELHI"
        n=0
        lcd.putstr(stri,0,3)
        while n<len(stri):
            if stri[n]=="_":
                while flag!=1:
                    pos = n
                    lcd.putstr(alphabet[(r2.value())%26],pos%20,3)
            n=n+1
            flag=0
        flag1=1

    if game2==1 and ascr==0:
#         lcd.clear()
        pos=0
        counter=0
        lcd.putstr("Capital of India?",0,0)
        lcd.putstr("A:Mumbai",0,1)
        lcd.putstr("B:Delhi",10,1)
        lcd.putstr("C:Chennai",0,2)
        lcd.putstr("D:Kolkata",10,2)
        while game2!=0:
            lcd.putstr(alphabet[(r2.value())%5],0,3)
            
            
    

