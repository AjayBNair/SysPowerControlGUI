import os
import tkinter as tk
from tkinter import ttk

def perform_action(action):
    actions = {
        "restart": "/r /t 1",
        "restart_time": "/r /t 20",
        "log_out": "-1",
        "shutdown": "/s /t 1"
    }
    os.system("shutdown " + actions.get(action, ""))

def create_button(parent, label, action):
    button = ttk.Button(parent, text=label, command=lambda: perform_action(action))
    button.place(x=50, y=50 + len(parent.winfo_children()) * 70, height=50, width=300)

def main():
    st = tk.Tk()
    st.title("Power Control")
    st.geometry("400x400")
    st.config(bg="#f0f0f0")  # Background color

    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 12, "bold"), foreground="black", background="#3498db")
    style.map("TButton", background=[("active", "#2980b9")])  # Hover effect

    buttons = [
        ("Restart", "restart"),
        ("Restart with Delay", "restart_time"),
        ("Log Out", "log_out"),
        ("Shutdown", "shutdown"),
    ]

    for label, action in buttons:
        create_button(st, label, action)

    st.mainloop()

if __name__ == "__main__":
    main()
