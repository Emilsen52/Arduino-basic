import machine, neopixel, time

n = 24
p = 5

np = neopixel.NeoPixel(machine.Pin(p), n)

#Defining clear mode:

def clear():
  for i in range(n):
    np[i] = (0, 0, 0)
    np.write()

#bootup sekvens

wait=40

np[0] = (255, 0, 0)
np.write()
time.sleep_ms(wait)

np[1] = (200, 55, 0)
np.write()
time.sleep_ms(wait)

np[2] = (150, 105, 0)
np.write()
time.sleep_ms(wait)

np[3] = (100, 155, 0)
np.write()
time.sleep_ms(wait)

np[4] = (50, 205, 0)
np.write()
time.sleep_ms(wait)

np[5] = (0, 255, 0)
np.write()
time.sleep_ms(wait)

np[6] = (0, 205, 55)
np.write()
time.sleep_ms(wait)

np[7] = (0, 155, 105)
np.write()
time.sleep_ms(wait)

np[8] = (0, 105, 155)
np.write()
time.sleep_ms(wait)

np[9] = (0, 55, 205)
np.write()
time.sleep_ms(wait)

np[10] = (0, 0, 255)
np.write()
time.sleep_ms(wait)

np[11] = (0, 55, 205)
np.write()
time.sleep_ms(wait)

np[12] = (0, 105, 155)
np.write()
time.sleep_ms(wait)

np[13] = (0, 155, 105)
np.write()
time.sleep_ms(wait)

np[14] = (0, 205, 55)
np.write()
time.sleep_ms(wait)

np[15] = (0, 255, 0)
np.write()
time.sleep_ms(wait)

np[16] = (50, 205, 0)
np.write()
time.sleep_ms(wait)

np[17] = (100, 155, 0)
np.write()
time.sleep_ms(wait)

np[18] = (150, 105, 0)
np.write()
time.sleep_ms(wait)

np[19] = (200, 55, 0)
np.write()
time.sleep_ms(wait)

np[20] = (255, 0, 0)
np.write()
time.sleep_ms(wait)

np[21] = (200, 0, 55)
np.write()
time.sleep_ms(wait)

np[22] = (150, 0, 105)
np.write()
time.sleep_ms(wait)

np[23] = (150, 0, 150)
np.write()
time.sleep_ms(wait)

time.sleep_ms(200)
clear()

time.sleep_ms(200)

#definerede farve+tal
def farve1 (r, g, b):
    def farve2 (r, g, b):
        def farve3 (r, g, b):
            def farve4 (r, g, b):
                def farve5 (r, g, b):
                    def farve6 (r, g, b):
                        def farve7 (r, g, b):
                            def farve8 (r, g, b):
                                def farve9 (r, g, b):
                                    def farve10 (r, g, b):
                                        def farve11 (r, g, b):
                                            def farve12 (r, g, b):
                                                def farve13 (r, g, b):
                                                    def farve14 (r, g, b):
                                                        def farve15 (r, g, b):
                                                            def farve16 (r, g, b):
                                                                def farve17 (r, g, b):
                                                                    def farve18 (r, g, b):
                                                                        def farve19 (r, g, b):
                                                                            def farve20 (r, g, b):
    
#Definerede farver
                                                                                farve1 (220, 20, 20) #rød
                                                                                farve2 (220, 120, 20) #orange
                                                                                farve3 (220, 220, 20) #gul
                                                                                farve4 (160, 220, 20) #lime grøn
                                                                                farve5 (50, 220, 20) #grøn
                                                                                farve6 (20, 220, 130) #tyrkis
                                                                                farve7 (20, 220, 217) #lyseblå
                                                                                farve8 (20, 73, 220) #blå
                                                                                farve9 (150, 20, 220) #lilla
                                                                                farve10 (220, 20, 173) #pink
                                                                                farve11 (220, 20, 20) #rød
                                                                                farve12 (220, 120, 20) #orange
                                                                                farve13 (220, 220, 20) #gul
                                                                                farve14 (160, 220, 20) #lime grøn
                                                                                farve15 (50, 220, 20) #grøn
                                                                                farve16 (20, 220, 130) #tyrkis
                                                                                farve17 (20, 220, 217) #lyseblå
                                                                                farve18 (20, 73, 220) #blå
                                                                                farve19 (150, 20, 220) #lilla
                                                                                farve20 (220, 20, 173) #pink

#hvad klokken er:


#Potentiometer script (skal define et tal fra 1-20 og trykket ned eller ikke 0-1 eller og om det er press and hold eller press)

while True:
    #solopgang feture (Sat til kl. 5:20 og tager ca. 10 min.)
    
    if klokken=
        
        r1=8
        g1=1
        b1=0

        r2=1
        g2=0
        b2=0

        r3=255
        g3=0
        b3=0

        def set_color1(r1, g1, b1):
              for i in range(11, 19):
                np[i] = (r1, g1, b1)
              np.write()
              
        def set_color2(r2, g2, b2):
              for i in range(-5, 11):
                np[i] = (r2, g2, b2)
              np.write()

        def set_color3(r3, g3, b3):
              for i in range(n):
                np[i] = (r3, g3, b3)
              np.write()
              

        def clear():
          for i in range(n):
            np[i] = (0, 0, 0)
            np.write()

        time.sleep_ms(50)

        while r1<255:
            time.sleep_ms(100)  

            r1+=255/600
            g1+=32/600
            b1=0
            set_color1(int(r1), int(g1), int(b1))
            
            r2+=50/600
            g2=0
            b2=0
            set_color2(int(r2), int(g2), int(b2))

        while (r3+g3+b3)<765:
            time.sleep_ms(50)
            g3+=1
            b3+=1
            set_color3(r3, g3, b3)
            
        time.sleep(10)

        clear()
    
    
    #farve1-20 commanden fra potentiometeret skal konverteres til en farve og om den skal sættes på lampen eller sendes:
    #press and hold=sæt lampens farve til 1-20
    #Press=send farve 1-20
    
        val = pin34.read_analog()
        display.scroll(str(val))
    
    #if array (hvis det er morgen=solopgang, vis besked hvis besked) 
    
    
    
    #Main rainbow effekt/menu:
    
        wait=10
    
        def wheel(pos):
          if pos < 0 or pos > 255:
            return (0, 0, 0)
          if pos < 85:
            return (255 - pos * 3, pos * 3, 0)
          if pos < 170:
            pos -= 85
            return (0, 255 - pos * 3, pos * 3)
          pos -= 170
          return (pos * 3, 0, 255 - pos * 3)
    
        def rainbow_cycle(wait):
          for j in range(255):
            for i in range(n):
              rc_index = (i * 256 // n) + j
              np[i] = wheel(rc_index & 255)
            np.write()
    
    
    