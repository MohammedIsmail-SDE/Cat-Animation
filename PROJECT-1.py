from PIL import Image, ImageTk
import tkinter as tk
import pygame 

root = tk.Tk()
root.title("Image Slideshow Viewer")
pygame.mixer.init()
pygame.mixer.music.load(r"D:\PYTHON PROJECT-1\cat.mp3.mpeg")
pygame.mixer.music.play(-1)


# List of image paths
image_paths = [
    r"D:\PYTHON PROJECT-1\⋆౨ৎ˚⟡˖ ࣪.jpg",
    r"D:\PYTHON PROJECT-1\download (1).jpg",
    r"D:\PYTHON PROJECT-1\download (2).jpg",
    r"D:\PYTHON PROJECT-1\download -5.jpg",
]

# Resize images and convert to RGB (fixes black screen)
image_size = (600, 600)
images = [Image.open(path).resize(image_size).convert("RGB") for path in image_paths]

label = tk.Label(root, bg="black")
label.pack()

current_index = 0
alpha = 0.0
fading_in = True

def fade():
    global current_index, alpha, fading_in

    img = images[current_index].copy()

    # Blend with black for fade effect
    black = Image.new("RGB", img.size, (0, 0, 0))
    blended = Image.blend(black, img, alpha)
    photo = ImageTk.PhotoImage(blended)

    label.config(image=photo)
    label.image = photo  # prevent garbage collection

    if fading_in:
        alpha += 0.05
        if alpha >= 1.0:
            alpha = 1.0
            fading_in = False
            root.after(2000, fade)  # hold for 2 seconds
        else:
            root.after(30, fade)
    else:
        alpha -= 0.05
        if alpha <= 0.0:
            alpha = 0.0
            current_index = (current_index + 1) % len(images)
            fading_in = True
        root.after(30, fade)

def start_slideshow():
    play_button.config(state="disabled")
    fade()

play_button = tk.Button(root, text="▶ Play Slideshow", command=start_slideshow)
play_button.pack(pady=10)

root.mainloop()
   



