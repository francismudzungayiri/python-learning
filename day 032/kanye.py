import requests
from tkinter import * 


def get_quote():
    response = requests.get('https://api.kanye.rest')
    response.raise_for_status()

    data = response.json()
    print(data['quote'])



window = Tk()
window.title('kanye quotes')
window.geometry('600x500')


button = Button(window, text='NEXT QUOTE', command=get_quote)
button.pack(pady=100)

window.mainloop()

