from tkinter import *
from functools import partial

# Function to validate login credentials
def validate_login(username, password):
    user = username.get()
    pwd = password.get()
    # Add further validation logic here
    if user == "admin" and pwd == "password":  # Example credentials
        print("Login successful")
    else:
        print("Login failed")
    print("Username entered:", user)
    print("Password entered:", pwd)
    return

# Create main window
tk_window = Tk()
tk_window.geometry('400x200')
tk_window.title('Login to Nandini\'s App - Hello Cuties')

# Function to display message in a new window
def display_message(message):
    message_window = Toplevel(tk_window)
    message_window.title("Message")
    Label(message_window, text=message).pack(pady=20)
    Button(message_window, text="Close", command=message_window.destroy).pack(pady=10)

# Function to handle login button click
def on_login_click(username, password):
    user = username.get()
    pwd = password.get()
    if user == "admin" and pwd == "password":  # Example credentials
        display_message("Login successful")
    else:
        display_message("Login failed")

# Create and place labels and entry boxes for username and password
Label(tk_window, text="Username").grid(row=0, column=0, padx=10, pady=10)
username = StringVar()
Entry(tk_window, textvariable=username).grid(row=0, column=1, padx=10, pady=10)

Label(tk_window, text="Password").grid(row=1, column=0, padx=10, pady=10)
password = StringVar()
Entry(tk_window, textvariable=password, show='*').grid(row=1, column=1, padx=10, pady=10)

# Create and place the login button
validate_login = partial(on_login_click, username, password)
Button(tk_window, text="Login", command=validate_login).grid(row=2, column=1, pady=10)

# Start the main event loop
tk_window.mainloop()
