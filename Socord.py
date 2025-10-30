import tkinter as tk
from tkinter import simpledialog, scrolledtext

root = tk.Tk()
root.title("Socord")
root.geometry("700x500")
root.configure(bg="#FFF200")

username = simpledialog.askstring("Login", "Enter your username:")
if not username: username = "Guest"

channels = {"general": [], "gaming": [], "music": []}
current_channel = "general"

def switch_channel(event):
    global current_channel
    current_channel = channel_list.get()
    update_chat()

def update_chat():
    chat_box.config(state='normal')
    chat_box.delete(1.0, tk.END)
    for msg in channels[current_channel]:
        chat_box.insert(tk.END, msg + "\n")
    chat_box.config(state='disabled')
    chat_box.yview(tk.END)

def send_msg(event=None):
    msg = msg_entry.get()
    if msg:
        channels[current_channel].append(f"{username}: {msg}")
        update_chat()
        msg_entry.delete(0, tk.END)

frame_left = tk.Frame(root, width=150, bg="#FFD400")
frame_left.pack(side=tk.LEFT, fill=tk.Y)

tk.Label(frame_left, text="Channels", bg="#FFD400", font=("Segoe UI",12,"bold")).pack(pady=5)
channel_list = tk.Listbox(frame_left)
for c in channels.keys(): channel_list.insert(tk.END, c)
channel_list.pack(fill=tk.Y, expand=True, padx=5, pady=5)
channel_list.bind("<<ListboxSelect>>", switch_channel)
channel_list.selection_set(0)

frame_right = tk.Frame(root, bg="#FFFFA0")
frame_right.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

chat_box = scrolledtext.ScrolledText(frame_right, state='disabled', bg="#FFFFA0")
chat_box.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

entry_frame = tk.Frame(frame_right, bg="#FFFFA0")
entry_frame.pack(fill=tk.X, padx=5, pady=5)

msg_entry = tk.Entry(entry_frame, width=50)
msg_entry.pack(side=tk.LEFT, padx=(0,5))
msg_entry.bind("<Return>", send_msg)

tk.Button(entry_frame, text="Send", command=send_msg, bg="#FFD400").pack(side=tk.LEFT)

update_chat()
root.mainloop()