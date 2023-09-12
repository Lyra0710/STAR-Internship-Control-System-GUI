from tkinter import *
from tkinter.ttk import *
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
        self.master.title("Abort")

        self.page_title = Label(self.master, anchor="center", text="Are you sure you want to abort?", font=("Open Sans", 20, "bold"))
        self.page_title.place(relx=0.5, rely=0.4, anchor=CENTER)

        self.master.title("Back to Home")
        self.link_label = Label(self.master, text="Back to Home", font=("Arial", 12))

        self.link_label.bind("<Button-1>", self.open_file)
        self.link_label.bind("<Enter>", lambda event: self.link_label.config(text="Back to Home", font=("Arial", 12, "underline")))
        self.link_label.bind("<Leave>", lambda event: self.link_label.config(text="Back to Home", font=("Arial", 12)))
        self.link_label.grid(row=2, column=3, pady=10)

        self.style = Style()
        self.style.map('D.TButton',
                       foreground=[('pressed', 'green'), ('active', 'green')],
                       background=[('pressed', '!disabled', 'black'), ('active', 'white')])

        self.btn_abort = Button(self.master, text="YES", style="D.TButton", command=self.abort)
        self.btn_abort.place(relx=0.4, rely=0.6, anchor=CENTER)

        self.btn_no_abort = Button(self.master, text="NO", style="D.TButton", command=self.no_abort)
        self.btn_no_abort.place(relx=0.6, rely=0.6, anchor=CENTER)

    def abort(self):
        self.page_title.config(text="Task Aborted")
        

    def no_abort(self):
        # if(py_version==2):
        #     os.system("python "+os.path.dirname(__file__)+"/Home_Page.py")
        # else:
        #     os.system("python3 "+os.path.dirname(__file__)+"/Home_Page.py")

        script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Home_Page.py")
        if py_version == 2:
            os.system("python \"" + script_path + "\"")
        else:
            os.system("python3 \"" + script_path + "\"")

    
    def open_file(self, event):
        root.destroy()

global root
root = Tk()
root.geometry("1340x750")

app = Application(master=root)

root.mainloop()
