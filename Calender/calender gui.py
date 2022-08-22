from tkinter import *
import calendar
from tkinter import ttk

def showCalender():
    gui = Tk()
    gui.config(background='grey')
    gui.title("Calender for the year")
    gui.geometry("550x600")
    year = int(year_field.get())
    gui_content=  calendar.calendar(year)
    calYear = Label(gui, text= gui_content, font= "Consolas 10 bold")
    calYear.grid(row=5, column=1,padx=20 , pady=20)
    gui.mainloop()

if __name__=='__main__':
    new = Tk()
##    new.config(background='red')
    new.title("Calender")
    new.geometry("300x300")
    cal = Label(new, text="Calender",font=("times", 45, "bold"))
    year = Label(new, text="Enter year",  font=("times", 18, "bold") )
    year_field=Entry(new)
    button = ttk.Button(new, text='Show Calender', command=showCalender)
    Exit = ttk.Button(new, text='Exit' ,   command=exit)
    cal.grid(row=1, column=1 )
    year.grid(row=2, column=1 , pady=20)
    year_field.grid(row=3, column=1)
    button.grid(row=4, column=1 ,pady=20)
    Exit.grid(row=6, column=1)
    new.mainloop()
