import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageFilter, ImageEnhance, ImageOps

# Initialize the main window
root = tk.Tk()
root.title("Photo Effect App")

# Functions to open an image file
def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
    if file_path:
        global img
        img = Image.open(file_path)
        img.show()
    else:
        messagebox.showwarning("Open Image", "Failed to open image!")

# Functions to apply effects
def apply_blur():
    if img:
        blurred_img = img.filter(ImageFilter.BLUR)
        blurred_img.show()

def apply_sharpen():
    if img:
        sharpened_img = img.filter(ImageFilter.SHARPEN)
        sharpened_img.show()

def apply_grayscale():
    if img:
        grayscale_img = ImageOps.grayscale(img)
        grayscale_img.show()

def apply_brightness():
    if img:
        enhancer = ImageEnhance.Brightness(img)
        bright_img = enhancer.enhance(1.5)
        bright_img.show()

def save_image():
    if img:
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")])
        if file_path:
            img.save(file_path)
            messagebox.showinfo("Save Image", "Image saved successfully!")
        else:
            messagebox.showwarning("Save Image", "Failed to save image!")

# Create buttons to trigger functions
open_button = tk.Button(root, text="Open Image", command=open_image)
blur_button = tk.Button(root, text="Apply Blur", command=apply_blur)
sharpen_button = tk.Button(root, text="Apply Sharpen", command=apply_sharpen)
grayscale_button = tk.Button(root, text="Apply Grayscale", command=apply_grayscale)
brightness_button = tk.Button(root, text="Apply Brightness", command=apply_brightness)
save_button = tk.Button(root, text="Save Image", command=save_image)

# Layout the buttons
open_button.pack(pady=5)
blur_button.pack(pady=5)
sharpen_button.pack(pady=5)
grayscale_button.pack(pady=5)
brightness_button.pack(pady=5)
save_button.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
