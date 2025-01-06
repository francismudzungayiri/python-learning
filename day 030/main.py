from tkinter import *
from tkinter import messagebox
import json



####----------- SAVE FUNCTION---------------###
def save():
    
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    new_data = {
        website:{
            'email':email,
            'password':password
        },
    }

    is_ok = messagebox.askokcancel(title='Website', message= f'These are the details entered. \nEMAIL: {email} \nPassword: {password}'
                           f'\n\n Is it ok to save.')

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='OOOOOPS', message='some fields are empty')
        
    else:
        if is_ok:
            try:
                with open('data.json', 'r') as data_file:
                    #reading data from json
                    data = json.load(data_file)
                    
            except FileNotFoundError:
                with open('data.json', 'w') as data_file:        
                    #updating old data with the new data
                    json.dump(new_data, data_file, indent=4)
                    
            else:
                #saving updated data
                data.update(new_data)
                
                with open('data.json', 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)
                    
            finally:
                website_entry .delete(0, END)
                password_entry.delete(0, END)






#############           generate password                            ################ 

import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','j','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] 

numbers = ['1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','&','*','+','(',')']


password = []

for letter in range(random.randint(8, 10)):
    rand_letter = random.choice(letters)
    password.append(rand_letter)

for number in range(random.randint(2,4)):
    rand_number = random.choice(numbers)
    password.append(rand_number)

for symbol in range(random.randint(2,4)):
    rand_sysmbol = random.choice(symbols)
    password.append(rand_sysmbol)
    
    
#shuffling a password
random.shuffle(password)

final_pssword = ''.join(password)
print(final_pssword)



def get_password():
    password_entry.insert(0, final_pssword)
    
    
    
def find_password():
    website = website_entry.get()
    
    with open('data.json', 'r') as data_file:
        data = json.load(data_file)
        
        for i in data[website]:
            print(i)
            
            



root = Tk()
root.title('Password Manager')
root.minsize(width= 600, height=600)
root.config(padx=50, pady=50)



logo = Label(text='logo', font=('Arial', 40))
logo.config(text='MyPass Manager')
logo.grid(row=0, column=1)


#laebls
website_label = Label(text='Website ')
website_label.grid(row=1, column=0)

email_label = Label(text='Email/ Username ')
email_label.grid(row=2, column=0)

password_label = Label(text='Password ')
password_label.grid(row=3, column=0)


#all entrys
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'fmudzunga@gmail.com')

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

#buttons
generate_password = Button(text='Generate Password', command=get_password)
generate_password.grid(row=3, column=2)

add_button = Button(text='ADD', width=36, command=save)
add_button.grid(row=4, column=1)

search_button = Button(text='Search', width=10, command=find_password)
search_button.grid(column=2, row=1)



    



root.mainloop()
