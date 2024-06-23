# Nandini's App - Hello Cuties

This is a simple Tkinter-based login application. The application provides a user interface to enter a username and password and print these values to the console upon clicking the login button.

## Features

- User-friendly interface for login
- Password entry is masked
- Simple validation mechanism

## Prerequisites

- Python 3.x
- Tkinter library (usually included with Python standard library)

## How to Run

1. **Install Python**: Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Save the Script**: Save the provided Python script (e.g., `login_app.py`) to your local machine.

3. **Run the Script**: Open a terminal or command prompt, navigate to the directory where the script is saved, and run the script using the following command:

4. **Use the Application**: The application window will appear. Enter your username and password, and click the "Login" button. The entered values will be printed to the console.

## Code Explanation

- The script creates a simple GUI application using Tkinter.
- The `validate_login` function is defined to handle the login button click event.
- The main window (`tk_window`) is created with a title and size.
- Labels and entry boxes for the username and password are created and placed in a grid layout.
- The login button is created and linked to the `validate_login` function.
- The main event loop (`tk_window.mainloop()`) starts the application.

Feel free to modify and extend this application as needed!

## License

This project is open-source and available under the MIT License.
