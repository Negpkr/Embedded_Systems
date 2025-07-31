import RPi.GPIO as GPIO
import time
import tkinter as tk
  
rt=tk.Tk()
var=tk.IntVar()
tk.Label(rt, 
        text="""Please choose an option:""",
        justify = tk.LEFT,
        padx = 20).pack()

op1 = tk.Radiobutton(rt, 
               text="Blue light",
               padx = 20, 
               variable=var, 
               value=1,
               command=rt.destroy).pack(anchor=tk.W)

op2 = tk.Radiobutton(rt, 
               text="Red light",
               padx = 20, 
               variable=var, 
               value=2,
               command=rt.destroy).pack(anchor=tk.W)
    
op3 = tk.Radiobutton(rt, 
               text="Green Light",
               padx = 20, 
               variable=var, 
               value=3,
               command=rt.destroy).pack(anchor=tk.W)
               
op4 = tk.Radiobutton(rt, 
               text="Exit",
               padx = 20, 
               variable=var, 
               value=4,
               command=rt.destroy).pack(anchor=tk.W)
               
rt.mainloop()


GPIO.setmode(GPIO.BOARD)
#Blue pin = 8
GPIO.setup(8, GPIO.OUT)
#Red pin = 10
GPIO.setup(10, GPIO.OUT)
#Green pin = 12
GPIO.setup(12, GPIO.OUT)

GPIO.output(8, GPIO.LOW)
GPIO.output(10, GPIO.LOW)
GPIO.output(12, GPIO.LOW)

if var.get() == 1:
    try:
        while 1:
          GPIO.output(8,GPIO.HIGH)
          time.sleep(0.25)
          GPIO.output(8, GPIO.LOW)
          time.sleep(0.25)
    except KeyboardInterrupt: 
        GPIO.cleanup()
        
elif var.get() == 2:
    try:
        while 1:
          GPIO.output(10,GPIO.HIGH)
          time.sleep(0.25)
          GPIO.output(10, GPIO.LOW)
          time.sleep(0.25)
    except KeyboardInterrupt: 
        GPIO.cleanup()
        
elif var.get() == 3:
    try:
        while 1:
          GPIO.output(12,GPIO.HIGH)
          time.sleep(0.25)
          GPIO.output(12, GPIO.LOW)
          time.sleep(0.25)
    except KeyboardInterrupt: 
        GPIO.cleanup()
	
