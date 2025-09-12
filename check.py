stri="De_l_"
answer="Dehli"
n=0
while n<len(stri):
    if stri[n]=="_":
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        counter = 0
        last_state = clk1.value()
        last_state2= clk2.value()
        pos = n
        counter=0
        string="123456789"
        def rotary_interrupt1(pin):
            """Interrupt handler for rotary encoder"""
            global counter
            if counter<0:
                counter=24
            if dt2.value():  # If DT is high, rotation is clockwise
                counter += 1
            else:           # If DT is low, rotation is counterclockwise
                if counter>=1:
                    counter -= 1
        clk2.irq(trigger=Pin.IRQ_FALLING, handler=rotary_interrupt1)
        lcd.putstr(alphabet[counter%25],pos%20,3)
        
        if sw1==1:
            stri[n]=alphabet[counter%25]
            
        n++
l=0
right=0
while l<len(stri)
    if stri[l]!=answer[]:
        right=1
    if right==1
    print("congrats")
            
        