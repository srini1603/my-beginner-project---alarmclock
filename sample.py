from tkinter import *
import datetime
import time
import winsound



def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:",date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

def times():
    string = time.strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, times)

clock = Tk()
clock.title("DataFlair Alarm Clock")

clock.geometry("400x300")

clock.resizable(0,0)
lbl = Label(clock, font=('calibri', 40, 'bold'),
            background='purple',
            foreground='white')

time_format=Label(clock, text= "Enter time in 24 hour format!", fg="red",bg="black",font="Arial").place(x=60,y=200)

setYourAlarm = Label(clock,text = "When to alarm",fg="blue",relief = "solid",font=("Helevetica",11,"bold")).place(x=0, y=110)

# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "green",width = 15).place(x=110,y=110)
minTime= Entry(clock,textvariable = min,bg = "green",width = 15).place(x=150,y=110)
secTime= Entry(clock,textvariable = sec,bg = "green",width = 15).place(x=200,y=110)


lbl.pack(anchor='center')

times()

#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x =110,y=150)


clock.mainloop()
#Execution of the window.
