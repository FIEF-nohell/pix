from tkinter import Tk, Label, Button, filedialog, Scale, HORIZONTAL, StringVar, OptionMenu
from pix import create_pixel_art, populate_dropdown_from_folder
from PIL import ImageTk, Image
import os

class PixelArtGUI:
    def __init__(self, master):
        self.master = master
        master.title("Pixel Art Creator")
        
        # Set window size to 600x300 pixels
        master.geometry("600x300")

        self.label = Label(master, text="Choose an image")
        self.label.pack()

        self.choose_button = Button(master, text="Choose Image", command=self.choose_image)
        self.choose_button.pack()

        # Add a slider for resolution
        self.resolution_slider = Scale(master, from_=1, to=25, orient=HORIZONTAL, tickinterval=1, label="Resolution", length=400)
        self.resolution_slider.pack()

        # Add a dropdown for folder content
        self.folder_var = StringVar(master)
        self.folder_var.set("Select an item")  # Default value
        dropdown_menu = OptionMenu(master, self.folder_var, [])
        dropdown_menu.pack()
        
        # Populate the dropdown with folder content
        populate_dropdown_from_folder(self.folder_var, dropdown_menu)

        self.execute_button = Button(master, text="Create Pixel Art", command=self.create_pixel_art)
        self.execute_button.pack()

        self.pixel_art_label = None  # Initialize as None

    def choose_image(self):
        global file_path
        file_path = filedialog.askopenfilename()
        # Load and display the image using PIL and ImageTk
        img = Image.open(file_path)
        img = ImageTk.PhotoImage(img)
        img_label = Label(image=img)
        img_label.image = img
        img_label.pack()

    def create_pixel_art(self):
        selected_resolution = self.resolution_slider.get()
        create_pixel_art(file_path, "outputs/pixel_art.png", selected_resolution, self.folder_var.get())
                # Update the label to display the created pixel art
        img = Image.open("outputs/pixel_art.png")
        img = ImageTk.PhotoImage(img)
        
        if self.pixel_art_label is None:
            self.pixel_art_label = Label(image=img)
            self.pixel_art_label.image = img
            self.pixel_art_label.pack()
        else:
            self.pixel_art_label.config(image=img)
            self.pixel_art_label.image = img
        pass

root = Tk()
app = PixelArtGUI(root)
root.mainloop()
