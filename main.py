from tkinter import *
from tkinter import messagebox
import passwordgen
import json

def generatethepassword():
    my_generated_password = passwordgen.PasswordGen().generator()
    PasswordInput.delete(0,END)
    PasswordInput.clipboard_clear()
    PasswordInput.insert(0,my_generated_password)
    PasswordInput.clipboard_append(my_generated_password)

def save():
    website = WebsiteInput.get().title()
    email = EmailInput.get()
    password = PasswordInput.get()

    new_data = {
        website: {
            "Email": email,
            "Password": password
                }}

    if len(website)==0 or len(password)==0:
        messagebox.showwarning(title="Empty", message= "Please fill all the details.")

    else:
        try:
            with open("Password_Manager.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("Password_Manager.json", "w") as data_file:
                json.dump(new_data, data_file, indent= 4)
        
        else:
            data.update(new_data)
            with open("Password_Manager.json", "w") as data_file:
                json.dump(data, data_file, indent= 4)

        finally:
            WebsiteInput.delete(0, END)
            PasswordInput.delete(0, END)

def search():
    website = WebsiteInput.get().title()
    try:
        with open("Password_Manager.json", "r") as data_file:
            data = json.load(data_file)
    except:
        messagebox.showwarning("Error", "Please save some data first.")
    else:
        try:
            search_email= data[website]['Email']
        except KeyError as webs:
            messagebox.showwarning("404 Error", f"Don't have details with for\n{webs}")
        else:
            search_password = data[website]['Password']
            messagebox.showinfo(title="Details", message= f"Website: {website}\n Email: {search_email}\n Password: {search_password}"  )


window = Tk()
window.title("Password Manager")
window.config(pady = 25, padx= 25)

#CANVAS START
canvas = Canvas()
canvas.config(width=200, height=200, highlightthickness=0)
lock_img= PhotoImage(file="lock-6455615-5327002.png")
canvas.create_image(100,100, image =lock_img)
canvas.grid(row= 0, column=1, pady=5)
#CANVAS END


#WEBSITE START
WebsiteLabel= Label(text="Website")
WebsiteLabel.grid(row=1, column= 0)

WebsiteInput= Entry(width=24)
WebsiteInput.focus()
WebsiteInput.grid(row= 1, column=1)
SearchButton = Button(width=16 ,text="Search", command = search)
SearchButton.grid(row= 1,column= 2)
#WEBSITE END


#EMAIL START
EmailUsername= Label(text="Email/Username")
EmailUsername.grid(row=2, column= 0)
EmailInput= Entry(width=41)
EmailInput.insert(END,"Abdul Ahad Rauf")
EmailInput.grid(row= 2, column=1, columnspan= 2)
#EMAIL END


#PASSWORD START
PasswordText= Label(text="Password") 
PasswordText.grid(row=3, column= 0)

PasswordInput= Entry(width=24)
PasswordInput.grid(row= 3, column=1)

Gen_Password= Button(text="Generate Password", command=generatethepassword) 
Gen_Password.grid(row=3, column= 2)
#END

Add= Button(text="Add", width= 41, command=save)
Add.grid(row=4, column= 1, columnspan=2)

window.mainloop()