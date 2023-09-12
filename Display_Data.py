from tkinter import *
import os
import sys

class Application(Frame):
    global py_version
    py_version = sys.version_info[0]
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.master.title("Data Display")

        # Create Labels to display source names
        label1 = Label(self.master, text="Temperature:")
        label2 = Label(self.master, text="Pressure:")
        label3 = Label(self.master, text="Burn Rate:")
        label4 = Label(self.master, text="Thrust:")
        label5 = Label(self.master, text="Vibration:")

        # Create Text widgets to display data from each source
        text1 = Text(self.master, width=20, height=10)
        text2 = Text(self.master, width=20, height=10)
        text3 = Text(self.master, width=20, height=10)
        text4 = Text(self.master, width=20, height=10)
        text5 = Text(self.master, width=20, height=10)

        # Position the widgets using grid layout
        label1.grid(row=1, column=0, sticky="nsew")
        label2.grid(row=1, column=1, sticky="nsew")
        label3.grid(row=1, column=2, sticky="nsew")
        label4.grid(row=1, column=3, sticky="nsew")
        label5.grid(row=1, column=4, sticky="nsew")

        text1.grid(row=2, column=0, sticky="nsew")
        text2.grid(row=2, column=1, sticky="nsew")
        text3.grid(row=2, column=2, sticky="nsew")
        text4.grid(row=2, column=3, sticky="nsew")
        text5.grid(row=2, column=4, sticky="nsew")

        # Example data for demonstration
        data1 = "Data from Source 1"
        data2 = "Data from Source 2"
        data3 = "Data from Source 3"
        data4 = "Data from Source 4"
        data5 = "Data from Source 5"

        # Insert data into the Text widgets
        text1.insert(END, data1)
        text2.insert(END, data2)
        text3.insert(END, data3)
        text4.insert(END, data4)
        text5.insert(END, data5)

        # Configure grid weights to make the widgets expand and fill the window
        self.master.grid_rowconfigure(2, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_columnconfigure(2, weight=1)
        self.master.grid_columnconfigure(3, weight=1)
        self.master.grid_columnconfigure(4, weight=1)

        # Create "Back to Home" link
        self.link_label = Label(self.master, text="Back to Home", font=("Arial", 12))
        self.link_label.grid(row=0, column=0, sticky="nw", columnspan=5)
        self.link_label.bind("<Button-1>", self.open_file)

    def open_file(self, event):
        root.destroy()

global root
root = Tk()
root.geometry("1340x750")
app = Application(master=root)
app.mainloop()
