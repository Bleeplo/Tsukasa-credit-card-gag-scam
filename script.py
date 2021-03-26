import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageSequence, ImageTk
import tkinter
def resource_path(relative_path):   #so when turning script into a exe, allows us to use other files, such as images
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
def intro_text():
    text01= Label(text="H-hi there...\nDo you th-think I could have your\ncredit card information, p-please?",
    bg="white",
    fg="black",
    font="none 15",
    padx=0,
    pady=0)
    text01.grid(row=0, rowspan=1, column=1, columnspan=3)
def text_w_entrybox(text_label_sentence, text_row, text_rowspan, text_column, text_columnspan, entry_row, entry_rowspan, entry_column, entry_columnspan):
    text_label = Label(root, text=text_label_sentence,
    bg="white",
    fg="black",
    font="none 15").grid(row=text_row, rowspan=text_rowspan, column=text_column, columnspan=text_columnspan,)
    entry_box = Entry(root, width=35).grid(row=entry_row, rowspan=entry_rowspan, column=entry_column, columnspan=entry_columnspan, sticky=W)

### Resources
root = tkinter.Tk()
window_icon = resource_path('icon_ico.ico');tsukasa_gif_file = resource_path('gif.gif');thx_button = resource_path('thanks_button.png')        #just our resource paths
tsuksa_gif = ImageTk.PhotoImage(Image.open(tsukasa_gif_file))
thanksbutton_image = PhotoImage(file=thx_button)
button_quit = Button(root, image=thanksbutton_image, command=root.quit, bg="white", borderwidth=0)                    #button (rounded version)
#button_quit = Button(root, text="Th-thanks", command=root.quit, bg="white")                    #button (text version)

class animated_gif:                                                                            #makes gif play, rather than being stiff image
    def __init__(self, parent):
        self.parent = parent
        self.canvas = tkinter.Canvas(parent, width=278, height=286, bg="white")                   #size of image (500x286 is original gif size)
        self.canvas.grid(row=0, rowspan=5, column=0, columnspan=1)                                #columnspan & rowspan is best friend
        self.sequence = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                                    Image.open(
                                    tsukasa_gif_file))]                               #file location/name, if you were not using a variable, it would be r'image.gif'
        self.image = self.canvas.create_image(139,143, image=self.sequence[0])        #make the number of this 0.5 the size of the image
        self.animate(1)
    def animate(self, counter):
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        self.parent.after(140, lambda: self.animate((counter+1) % len(self.sequence))) #the number changes the time/how fast the gif goes. Higher = longer wait, shorter = faster

### Window Info
root.geometry('') #width & height of window
root.title('Totally Not Malware') #title of window
root.iconbitmap(window_icon)       #icon of image
root.configure(background='white') #makes background white
root.resizable(0,0)                #makes window unmovable

### Main display stuff
gif = animated_gif(root) #animated gif
intro_text()
text_w_entrybox("Card number:", 1, 1, 1, 1, 1, 1, 2, 2)
text_w_entrybox("Expiry date:", 2, 1, 1, 1, 2, 1, 2, 2)
text_w_entrybox("Security code:", 3, 1, 1, 1, 3, 1, 2, 2)
button_quit.grid(row=4, column=2, sticky=W)

### Main loop
root.mainloop() #keeps the window open forever, till closed
