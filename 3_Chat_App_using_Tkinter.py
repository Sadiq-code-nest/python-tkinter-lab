import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import datetime


# Main Window
root = tk.Tk()
root.title("Tkinter Chat App")
root.geometry("450x600")
root.configure(bg="#1e1e1e")

# Chat Frame (Scrollable)
chat_frame = tk.Frame(root, bg="#1e1e1e")
chat_frame.pack(fill="both", expand=True)

canvas = tk.Canvas(chat_frame, bg="#1e1e1e", highlightthickness=0)
scrollbar = ttk.Scrollbar(chat_frame, orient="vertical", command=canvas.yview)

scrollable_frame = tk.Frame(canvas, bg="#1e1e1e")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Message Function
def add_message(text, is_user=True, image=None):
    msg_frame = tk.Frame(scrollable_frame, bg="#1e1e1e")

    bg_color = "#4CAF50" if is_user else "#333333"
    anchor = "e" if is_user else "w"

    bubble = tk.Label(
        msg_frame,
        text=text,
        bg=bg_color,
        fg="white",
        wraplength=250,
        justify="left",
        padx=10,
        pady=5,
        font=("Arial", 10)
    )
    bubble.pack(anchor=anchor, pady=2, padx=5)

    # If image exists
    if image:
        img = Image.open(image)
        img = img.resize((200, 200))
        img = ImageTk.PhotoImage(img)

        img_label = tk.Label(msg_frame, image=img, bg="#1e1e1e")
        img_label.image = img  # keep reference
        img_label.pack(anchor=anchor, pady=5)

    msg_frame.pack(fill="both", anchor=anchor, pady=5)

    canvas.update_idletasks()
    canvas.yview_moveto(1.0)

# Send Text
def send_message():
    msg = entry.get()
    if msg.strip() == "":
        return

    add_message(msg, is_user=True)
    entry.delete(0, tk.END)

    # bot reply
    add_message("Got it 👍", is_user=False)

# Send Image
def send_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif")]
    )

    if file_path:
        add_message("📷 Image sent", is_user=True, image=file_path)
        add_message("Nice image!", is_user=False)

# Bottom Input Bar
bottom_frame = tk.Frame(root, bg="#2c2c2c")
bottom_frame.pack(fill="x", side="bottom")

entry = tk.Entry(bottom_frame, font=("Arial", 12))
entry.pack(side="left", fill="x", expand=True, padx=5, pady=10)

send_btn = tk.Button(
    bottom_frame,
    text="Send",
    bg="#4CAF50",
    fg="white",
    command=send_message
)
send_btn.pack(side="left", padx=5)

img_btn = tk.Button(
    bottom_frame,
    text="Image",
    bg="#2196F3",
    fg="white",
    command=send_image
)
img_btn.pack(side="left", padx=5)
# Run App

root.mainloop()