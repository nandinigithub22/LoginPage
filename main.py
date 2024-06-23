from tkinter import *
from functools import partial

def validate_login(username, password):
    print("Username entered:", username.get())
    print("Password entered:", password.get())
    # Add further validation logic here
    return

# Create main window
tk_window = Tk()
tk_window.geometry('400x200')
tk_window.title('Login to Nandini\'s App - Hello Cuties')

# Create and place labels and entry boxes for username and password
Label(tk_window, text="Username").grid(row=0, column=0, padx=10, pady=10)
username = StringVar()
Entry(tk_window, textvariable=username).grid(row=0, column=1, padx=10, pady=10)

Label(tk_window, text="Password").grid(row=1, column=0, padx=10, pady=10)
password = StringVar()
Entry(tk_window, textvariable=password, show='*').grid(row=1, column=1, padx=10, pady=10)

# Create and place the login button
validate_login = partial(validate_login, username, password)
Button(tk_window, text="Login", command=validate_login).grid(row=2, column=1, pady=10)

# Start the main event loop
tk_window.mainloop()
