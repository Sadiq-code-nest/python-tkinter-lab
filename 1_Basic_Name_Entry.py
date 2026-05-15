# Using Tkinter to create a simple GUI for name entry
import tkinter
root=tkinter.Tk()
root.title("Name Entry")
root.geometry("300x150")

# Create a label and an entry widget
name_label=tkinter.Label(root, text="Enter your name:")
name_label.pack(pady=10)
name_entry_textbox=tkinter.Entry(root)
name_entry_textbox.pack(pady=5)

# Create a label and an entry widget for email
email_label=tkinter.Label(root, text="Enter your email:")
email_label.pack(pady=10)
email_entry_textbox=tkinter.Entry(root)
email_entry_textbox.pack(pady=5)
# Create a submit button
submit_button=tkinter.Button(root, text="Submit")
submit_button.pack(pady=10)

root.mainloop()

