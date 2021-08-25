import sys
import tkinter as tk
from pathlib import Path
from typing import Union

from PIL import Image, ImageSequence, ImageTk  # type: ignore


def resource_path(relative_path: Union[str, Path]) -> Path:  #so when turning script into a exe, allows us to use other files, such as images
    """ Get absolute path to resource, works for dev and for PyInstaller """
    
    base_dir = Path(__file__).parent
    
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_dir = Path(sys._MEIPASS)  # pylint: disable=no-member

    return base_dir / relative_path


def intro_text() -> None:
    intro = tk.Label(
        text="H-hi there...\nDo you th-think I could have your\ncredit card information, p-please?",
        bg="#FFFFFF",
        fg="#000000",
        font=("Arial", 15),
        padx=0,
        pady=0
    )
    intro.grid(row=0, rowspan=1, column=1, columnspan=3)


def text_w_entrybox(root, text_label_sentence, text_row, text_rowspan, text_column, text_columnspan, entry_row, entry_rowspan, entry_column, entry_columnspan) -> None:
    text_label = tk.Label(
        root,
        text = text_label_sentence,
        bg="#FFFFFF",
        fg="#000000",
        font=("Arial", 15),
    )
    text_label.grid(row=text_row, rowspan=text_rowspan, column=text_column, columnspan=text_columnspan)

    entry_box = tk.Entry(root, width=35)
    entry_box.grid(
        row=entry_row,
        rowspan=entry_rowspan,
        column=entry_column,
        columnspan=entry_columnspan,
        sticky=tk.W
    )


class AnimatedGIF:
    def __init__(self, parent, file_path):
        self.parent = parent
        self.canvas = tk.Canvas(parent, width=278, height=286, bg="#FFFFFF") #size of image (500x286 is original gif size)
        self.canvas.grid(row=0, rowspan=5, column=0, columnspan=1)
        self.sequence = [
            ImageTk.PhotoImage(img)
            for img in ImageSequence.Iterator(
                Image.open(file_path)
            )
        ]

        self.frame = 0
        self.image = self.canvas.create_image(139, 143, image=self.sequence[self.frame]) # Make the number of this 0.5 the size of the image

        # self.animate()

    def increment_frame(self) -> None:
        self.frame = (self.frame + 1) % len(self.sequence)

    def animate(self) -> None:
        self.increment_frame()
        self.parent.after(140, self.animate) # The number represents frame delay, in this case 140 ms, or ~7 FPS
        self.canvas.itemconfig(self.image, image=self.sequence[self.frame])


def main() -> None:
    ### Resources
    root = tk.Tk()
    window_icon = resource_path(Path('data') / 'icon_ico.ico')
    tsukasa_gif_file = resource_path(Path('data') / 'tsukasa.gif')
    thx_button = resource_path(Path('data') / 'thanks_button.png')

    thanksbutton_image = tk.PhotoImage(file=thx_button)
    button_quit = tk.Button(
        root,
        image=thanksbutton_image,
        command=root.quit,
        bg="#FFFFFF",
        borderwidth=0
    )

    ### Window Info
    root.geometry('')
    root.title('Totally Not Malware')
    root.iconbitmap(window_icon)
    root.configure(background='#FFFFFF')
    root.resizable(0, 0) # Disables window resizing

    ### Main display stuff
    gif = AnimatedGIF(root, tsukasa_gif_file)
    gif.animate()
    intro_text()
    text_w_entrybox(root, "Card number:", 1, 1, 1, 1, 1, 1, 2, 2)
    text_w_entrybox(root, "Expiry date:", 2, 1, 1, 1, 2, 1, 2, 2)
    text_w_entrybox(root, "Security code:", 3, 1, 1, 1, 3, 1, 2, 2)
    button_quit.grid(row=4, column=2, sticky=tk.W)

    ### Main loop
    root.mainloop() #keeps the window open forever, till closed

if __name__ == '__main__':
    main()