import tkinter as tk


window = tk.Tk()
window.title('My first Ptyhon GUI App')
window.minsize(width=1000, height= 800)


def btn_clicked():
    my_label.config(text= user_input.get())

#label
my_label = tk.Label(text='My first label', font=('Arial', 18))
my_label.config(text='Hello aRE YOU ENJOYING YOUR PYTHON JOURNEY SO FAR')
my_label.pack()

#BUTTONS
button = tk.Button(text='SUBMIT', command=btn_clicked)
button.pack()

#input 
user_input = tk.Entry(width=20)
user_input.pack()




window.mainloop()