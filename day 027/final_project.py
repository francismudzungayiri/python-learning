from tkinter import *




def calculate():
    #1mile = 1.60934km
    km = 1.60934 * float(miles_input.get())
    miles_converted.config(text = round(km, 3))



window = Tk()
window.title('Miles to killometers')
window.minsize(width=500, height= 500)
window.config(padx=100, pady=100)

#text input
miles_input = Entry(width=20)
miles_input.grid(column=1, row=0)


equal_to_label = Label(text='equal-to-label', font=('Arial', 18))
equal_to_label.config(text='Equal to')
equal_to_label.grid(column=0, row=1)

miles_converted = Label(text='My first label', font=('Arial', 18))
miles_converted.config(text='0')
miles_converted.grid(column=1, row=1)

miles_label = Label(text='My first label', font=('Arial', 18))
miles_label.config(text='killometer')
miles_label.grid(column=2, row=1)


#button
button = Button(text='SUBMIT', command=calculate)
button.grid(column=1, row=2)


window.mainloop()

