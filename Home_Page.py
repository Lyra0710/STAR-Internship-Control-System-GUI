import tkinter as tk
from tkinter.ttk import *
import os
import sys
from tkinter import messagebox
import matplotlib.pyplot as plt

# To check paths
# print(plt.__file__)
# print(sys.executable)

print(sys.version)
print(sys.executable)


class Application(Frame):
    global py_version
    py_version = sys.version_info[0]
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.master.title("Home")
        self.master_frame = tk.Frame(root, bg='#f8f8f2')
        self.page_title = tk.Label(self.master_frame, text="Rocket Motor Static Test Pad Control System", font=("Open Sans", 20, "bold"), bg='#f8f8f2')
        self.page_title.pack(side=tk.TOP)
        self.master_frame.pack(side=tk.TOP, pady=20)
        

        self.style = Style()
        self.style.map('D.TButton',
                       foreground=[('pressed', 'green'), ('active', 'green')],
                       background=[('pressed', '!disabled', 'black'), ('active', 'white')])
        
        
        def callback_Ig():
            script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Ignition_Sequence.py")
            if py_version == 2:
                os.system("python \"" + script_path + "\"")
            else:
                os.system("python3 \"" + script_path + "\"")

        def callback_D():
            script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Sensor_Data.py")
            if py_version == 2:
                os.system("python3 \"" + script_path + "\"")
            else:
                os.system("python \"" + script_path + "\"")

        # def callback_A():
        #     script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Abort.py")
        #     if py_version == 2:
        #         os.system("python \"" + script_path + "\"")
        #     else:
        #         os.system("python3 \"" + script_path + "\"")

        def callback_A():
            messagebox.showinfo("Abort", "Task Aborted")


        self.btn_frame = tk.Frame(root, bg='#f8f8f2')

        self.btn = Button(self.btn_frame, text="Ignition Sequence", style="D.TButton", command=callback_Ig, padding=10)
        self.btn.grid(row=1, column=1, padx=10, pady=10)

        self.btn = Button(self.btn_frame, text="Display Data", style="D.TButton", command=callback_D, padding=10)
        self.btn.grid(row=2, column=1, padx=10, pady=10)

        self.btn = Button(self.btn_frame, text="Abort", style="D.TButton", command=callback_A, padding=10)
        self.btn.grid(row=3, column=1, padx=10, pady=10)

        self.btn_frame.pack(side=tk.TOP, pady=200)




# frame= Frame(root, relief= 'sunken')
# frame.grid(sticky= "we") 

# frame.grid_rowconfigure(1, weight=1)
# frame.grid_columnconfigure(1, weight=1)

# frame.grid_rowconfigure(2, weight=1)
# frame.grid_columnconfigure(2, weight=1)

# frame.grid_rowconfigure(3, weight=1)
# frame.grid_columnconfigure(3, weight=1)

# # Make the window sticky for every case
# root.grid_rowconfigure(1, weight=1)
# root.grid_columnconfigure(1, weight=1)

# root.grid_rowconfigure(2, weight=1)
# root.grid_columnconfigure(2, weight=1)

# root.grid_rowconfigure(3, weight=1)
# root.grid_columnconfigure(3, weight=1)


if(__name__ == "__main__"):
    root = tk.Tk()
    root.geometry("1280x720")
    root.configure(bg='#f8f8f2')
    app = Application(master=root)

    # Center the buttons (trying to atleast)
    app.update_idletasks()
    window_width = root.winfo_width()
    column_offset = (window_width // 2) - 1
    app.grid_columnconfigure(0, minsize=column_offset)
    app.grid_columnconfigure(2, minsize=column_offset)

    app.mainloop()
