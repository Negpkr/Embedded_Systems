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
    


def a():
    dot()
    dash()
    time.sleep(2)
    

def b():
    dash()
    dot()
    dot()
    dot()
    time.sleep(2)

def c():
    dash()
    dot()
    dash()
    dot()
    time.sleep(2)
    

def d():
    dash()
    dot()
    dot()
    dot()
    time.sleep(2)
    
def e():
    dot()
    time.sleep(2)
    

def f():
    dot()
    dot()
    dash()
    dot()
    time.sleep(2)
    
def g():
    dash()
    dash()
    dot()
    time.sleep(2)
    

def h():
    dot()
    dot()
    dot()
    dot()
    time.sleep(2)
    

def i():
    dot()
    dot()
    time.sleep(2)
    

def j():
    dot()
    dash()
    dash()
    dash()
    time.sleep(2)
    

def k():
    dash()
    dot()
    dash()
    time.sleep(2)
    

def l():
    dot()
    dash()
    dot()
    dot()
    time.sleep(2)
    
def m():
    dash()
    dash()
    time.sleep(2)
    

def n():
    dash()
    dot()
    time.sleep(2)
    
def o():
    dash()
    dash()
    dash()
    time.sleep(2)
    

def p():
    dot()
    dash()
    dash()
    dot()
    time.sleep(2)
    
def q():
    dash()
    dash()
    dot()
    dash()
    time.sleep(2)
    

def r():
    dot()
    dash()
    dot()
    time.sleep(2)
    
def s():
    dot()
    dot()
    dot()
    time.sleep(2)
    

def t():
    dash()
    time.sleep(2)
    
def u():
    dot()
    dot()
    dash()
    time.sleep(2)
    

def v():
    dot()
    dot()
    dot()
    dash()
    time.sleep(2)
    
def w():
    dot()
    dash()
    dash()
    time.sleep(2)
    

def x():
    dash()
    dot()
    dot()
    dash()
    time.sleep(2)
    
def y():
    dash()
    dot()
    dash()
    dash()
    time.sleep(2)
    

def z():
    dash()
    dash()
    dot()
    dot()
    time.sleep(2)
    


def choose_m(input_m):
  index=0
  print("The word: ")
  print (input_m)
  while index != len(input_m):
     if input_m[index] == "a":
          print(input_m[index])
          a()
     elif input_m[index] == "b":
          print(input_m[index])
          b()
     elif input_m[index] =="c":
          print(input_m[index])
          c()
     elif input_m[index] == "d":
          print(input_m[index])
          d()
     elif input_m[index] == "e":
          print(input_m[index])
          e()
     elif input_m[index] == "f":
          print(input_m[index])
          f()
     elif input_m[index] =="g":
          print(input_m[index])
          g()
     elif input_m[index] == "h":
          print(input_m[index])
          h()
     elif input_m[index] == "i":
          print(input_m[index])
          i()
     elif input_m[index] =="j":
          print(input_m[index])
          j()
     elif input_m[index] == "k":
          print(input_m[index])
          k()
     elif input_m[index] == "l":
          print(input_m[index])
          l()
     elif input_m[index] == "m":
          print(input_m[index])
          m()
     elif input_m[index] =="n":
          print(input_m[index])
          n()
     elif input_m[index] == "o":
          print(input_m[index])
          o()
     elif input_m[index] == "p":
          print(input_m[index])
          p()
     elif input_m[index] =="q":
          print(input_m[index])
          q()
     elif input_m[index] == "r":
          print(input_m[index])
          r()
     elif input_m[index] == "s":
          print(input_m[index])
          s()
     elif input_m[index] == "t":
          print(input_m[index])
          t()
     elif input_m[index] =="u":
          print(input_m[index])
          u()
     elif input_m[index] == "v":
          print(input_m[index])
          v()
     elif input_m[index] == "w":
          print(input_m[index])
          w()
     elif input_m[index] =="x":
          print(input_m[index])
          x()
     elif input_m[index] == "y":
          print(input_m[index])
          y()
     elif input_m[index] == "z":
          print(input_m[index])
          z()
     index=index+1
     
rt= tk.Tk()
entry = tk.Entry(rt) 
entry.pack() 
entry.focus_set()

def call():  
    input_m = entry.get()
    choose_m(input_m)
    return
    
    
button1 = tk.Button(text='Ok', width = 10, command=call)
button1.pack()


rt.mainloop()


  
