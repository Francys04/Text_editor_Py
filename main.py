import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *


def change_color():
    """Opens a color selection dialog box using the colorchooser module. 
    It displays a title "pick a color..or else" in the dialog box. """
    color = colorchooser.askcolor(title="pick a color..or else")
    """Updates the configuration of a text_area component. It changes the foreground (text) color of 
    the text_area to the color selected by the user. color[1] contains the hexadecimal representation of the selected color."""
    text_area.config(fg=color[1])

""" Change the font of the text_area component."""
def change_font(*args):
    """uses the values retrieved from font_name and size_box 
    (which are expected to be variables or components in your GUI) to set the font name and size of the text in the text_area."""
    text_area.config(font=(font_name.get(), size_box.get()))

"""Intended for creating a new, untitled file within the GUI"""
def new_file():
    window.title("untitled")
    text_area.delete(1.0, END)

""" Used to open existing files"""
def open_file():
    file = askopenfilename(defaultextension=".txt",
                           file=[("All Files", "*.*"),
                                ("Text Documents", "*.txt")])
    """The code is wrapped in a try block, catching any exceptions that might occur during file operations. 
    If an exception occurs, it prints an error message"""
    try:
        window.title(os.path.basename(file)) # Open and read a selected file into the text_area
        text_area.delete(1.0, END) #Clears the contents of the text_area using text_area.delete(1.0, END).

        file = open(file, "r") #Opens the selected file in read mode ("r") using the open function.

        text_area.insert(1.0, file.read()) # Inserts the contents of the file into the text_area using text_area.insert(1.0, file.read()).

    except Exception:
        print('couldn`t read file')

    finally:
        file.close()

"""Func opens a file dialog using filedialog.asksaveasfilename to get the desired file name and location.
The dialog suggests the initial file name as "untitled.txt" and specifies that the file type should have the .txt extension."""
def save_file():
    file = filedialog.asksaveasfilename(initialfile="unititled.txt",
                                        defaultextension=".txt",
                                        filetypes=[("All Files", "*.*"),
                                        ("Text Documents", "*.txt")])

    if file is None:
        return

    else:
        try:
            window.title(os.path.basename(file)) # Sets the window title to the base name of the selected file.
            file = open(file, "w") # Opens the file in write mode ("w") using the open function.

            file.write(text_area.get(1.0, END)) # Writes the contents of the text_area to the file using file.write(text_area.get(1.0, END)).

        except Exception:
            print("couldn't save file")
            
            """The finally block ensures that the file is closed, even if an exception is raised."""
        finally:
            file.close()

"""This function seems to be used to perform a "Cut" action within the text_area"""
def cut():
    text_area.event_generate("<<Cut>>")

"""This function seems to be used to perform a "Copy" action within the text_area."""
def copy():
    text_area.event_generate("<<Copy>>")

"""This function seems to be used to perform a "Paste" action within the text_area."""
def paste():
    text_area.event_generate("<<Paste>>")

"""This function is meant to display an "About" message box for the program."""
def about():
    showinfo("About this program", "This is a program whriten by Francys04")

"""This function is used to close the application window."""
def quit():
    window.destroy()


window = Tk() # function is used to create the main window.
window.title("Text editor")
file = None

window_width = 500
window_height = 500

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

"""Calculates the position (x, y) to center the window on the screen."""
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

"""Sets the window size and position using the geometry method."""
window.geometry("{}x{}+{}+{}".format(window_height, window_width, x, y))

"""Creates a text area widget for text input and display."""
font_name = StringVar(window)
font_name.set("Arial")

font_size = StringVar(window)
font_size.set("25")

text_area = Text(window, font=(font_name.get(), font_size.get()))

"""Adds a scrollbar to the text area for vertical scrolling."""
scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

text_area.grid(sticky=N + E + S + W)

frame = Frame(window)
frame.grid()

color_button = Button(frame, text='color', command=change_color)
color_button.grid(row=0, column=0)

"""Uses OptionMenu for font selection and Spinbox for font size."""
font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)


size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font) # size of botton
size_box.grid(row=0, column=2)

"""Widget on the right side of the text area. The fill=Y argument allows the scrollbar to expand along the vertical direction."""
scroll_bar.pack(side=RIGHT, fill=Y)
"""Configure the yscrollcommand of the text area to synchronize it with the scrollbar. 
When the text content in the text area is too large to fit, this linkage enables scrolling the text using the scrollbar."""
text_area.config(yscrollcommand=scroll_bar.set)

"""Creates a new menu bar (menu_bar) associated with the main window (window)."""
menu_bar = Menu(window)
window.config(menu=menu_bar)

"""Creates a submenu for "File" in the menu_bar, with tearoff=0 preventing the submenu from being torn off."""
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='File', menu=file_menu)

file_menu.add_command(label="New", command=new_file) # Adds a "New" option to the "File" menu, linked to the new_file() function.
file_menu.add_command(label="Open", command=open_file) # Adds an "Open" option, linked to the open_file() function.
file_menu.add_command(label="Save", command=save_file) # Adds a "Save" option, linked to the save_file() function.
file_menu.add_separator() #  Adds a separator line in the "File" menu.
file_menu.add_command(label="Exit", command=quit) #  Adds an "Exit" option, linked to the quit() function.


edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label='Cut', command=cut) # Adds a "Cut" option, linked to the cut() function.
edit_menu.add_command(label='Copy', command=copy) # Adds a "Copy" option, linked to the copy() function.
edit_menu.add_command(label='Paste', command=paste) # Adds a "Paste" option, linked to the paste() function.

help_menu = Menu(menu_bar, tearoff=0) # Adds an "About" option, linked to the about() function.
menu_bar.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='About', command=about)

"""Starts the main event loop of the GUI application, which waits for user interactions and handles them accordingly."""
window.mainloop()
