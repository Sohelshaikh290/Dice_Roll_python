# Dice_Roll_python
Dice Rolling Simulator Python Project
The provided code is a Python program that creates a graphical user interface (GUI) application using the Tkinter library. This application simulates rolling a dice when a button is clicked. Here's a breakdown of its components:

Importing Libraries:

The tkinter library is imported to create the graphical interface.
The random module is imported to generate random dice numbers.
Creating the GUI:

The Tk() function is used to create the main window.
Defining Functions:

A function named roll() is defined. Inside this function:
A list called number is created, containing Unicode dice face characters.
The Label widget named label is configured to display a randomly chosen dice face character.
The label widget is packed to display it in the window.
Window Configuration:

The minsize() function sets the minimum dimensions of the window.
The maxsize() function sets the maximum dimensions of the window.
The title() function sets the title of the window.
Creating Widgets:

A Label widget named heading is created to display the heading "ROLL THE DICE" with a specified font and background color. It is packed to fill the horizontal space.
Button Creation:

A Button widget named button is created with the text "Roll" and a specified font. Its command is set to call the roll() function when clicked. The button is packed in the window.
Running the Application:

The mainloop() function is used to run the application and handle user interactions.
In summary, the code creates a simple GUI application that mimics rolling a dice. When the "Roll" button is clicked, a random dice face is displayed on the screen using Unicode characters. The application window has a fixed size, a title, and a button to initiate the dice roll.
