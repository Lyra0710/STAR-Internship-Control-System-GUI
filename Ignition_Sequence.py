from tkinter import *
from tkinter.ttk import *
import threading
import time
import os

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.master.title("Ignition")

        self.page_title = Label(self.master, anchor=CENTER, text="Countdown", font=("Open Sans", 20, "bold"))
        # self.page_title.grid(row=1, column=3, pady=10, sticky="NSW")
        self.page_title.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.master.title("Back to Home")
        self.link_label = Label(self.master, text="Back to Home", font=("Arial", 12))

        self.link_label.bind("<Button-1>", self.open_file)
        self.link_label.bind("<Enter>", lambda event: self.link_label.config(text="Back to Home", font=("Arial", 12, "underline")))
        self.link_label.bind("<Leave>", lambda event: self.link_label.config(text="Back to Home", font=("Arial", 12)))
        self.link_label.grid(row=2, column=3, pady=10)

        self.countdown_label = Label(self.master, text="", font=("Helvetica", 28))
        self.countdown_label.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.abort_button = Button(self.master, text="Emergency Abort", command=self.abort_countdown)
        # self.abort_button.grid(row=2, column=3, pady=10)
        self.abort_button.place(relx=0.5, rely=0.6, anchor=CENTER)

        self.is_aborted = False

        # Start the countdown in a separate thread
        countdown_thread = threading.Thread(target=self.start_countdown)
        countdown_thread.start()

    def start_countdown(self):
        countdown_time = 10

        while countdown_time > 0 and not self.is_aborted:
            self.countdown_label.config(text=str(countdown_time))
            self.master.update()
            countdown_time -= 1
            time.sleep(1)

        if self.is_aborted:
            self.countdown_label.config(text="Task Aborted")
        else:
            self.countdown_label.config(text="Started Ignition")

    def abort_countdown(self):
        self.is_aborted = True

    def open_file(self, event):
        root.destroy()

if(__name__=="__main__"):
    global root
    root = Tk()
    root.geometry("1340x750")
    app = Application(master=root)
    root.mainloop()
