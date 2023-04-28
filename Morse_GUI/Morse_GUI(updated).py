import tkinter as tk
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
#Blue pin = 8
GPIO.setup(8, GPIO.OUT)
GPIO.output(8, GPIO.LOW)

     
# Morse codes:
def dash():
    GPIO.output(8,GPIO.HIGH)
    time.sleep(3)
    GPIO.output(8, GPIO.LOW)  
    time.sleep(1)
    
    
def dot():
    GPIO.output(8,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(8, GPIO.LOW)  
    time.sleep(1)
    
M_codes = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 
              'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 
              'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 
              'y': '-.--', 'z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
              '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}


def choose_m(input_m):
    print("The word: ")
    print (input_m)
    for letter in input_m:
        print(letter)
        if letter.lower() in M_codes:
            morse_map = M_codes[letter.lower()]
            for status in morse_map:
                if status == '.':
                    dot()
                elif status == '_':
                    dash()
        time.sleep(2)
     
rt= tk.Tk()
entry = tk.Entry(rt) 
entry.pack() 
entry.focus_set()

def call():  
    input_m = entry.get()[:12]
    choose_m(input_m)
    return
    
    
button1 = tk.Button(text='Ok', width = 10, command=call)
button1.pack()


rt.mainloop()


  
