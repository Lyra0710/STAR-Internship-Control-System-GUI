from tkinter import *
import tkinter as tk
from tkinter.ttk import *
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import threading

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.master.title("Data Display")
        self.page_title = Label(self.master, anchor=CENTER, text="Sensor Data", font=("Open Sans", 20, "bold"))
        self.page_title.place(relx=0.5, rely=0.1, anchor=CENTER)

        def update_graph(fig, ax, canvas, y_range):
            x_data = []
            y_values = []

            while True:
                # Generate random data within a particular range
                x = len(x_data) + 1
                y = random.uniform(*y_range)

                # Add new data points
                x_data.append(x)
                y_values.append(y)

                # Update the graph
                ax.clear()
                ax.plot(x_data, y_values)
                canvas.draw()

                # Delay between updates
                self.master.after(1000)  # 1000 milliseconds = 1 second

        def open_sensor_graph(sensor_name, y_range):
            sensor_window = Toplevel(self.master)
            sensor_window.title(f"{sensor_name} Graph")
            fig = plt.Figure(figsize=(8, 4))
            ax = fig.add_subplot(111)
            canvas = FigureCanvasTkAgg(fig, master=sensor_window)
            canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)
            canvas.draw()

            # Start updating the graph in a separate thread
            thread = threading.Thread(target=update_graph, args=(fig, ax, canvas, y_range))
            thread.start()

        style = Style()
        style.configure('TButton', font=("Arial", 12), width=15, height=2)

        # Create buttons for each sensor
        button_temp = Button(self.master, text="Temperature", style='TButton', command=lambda: open_sensor_graph("Temperature", (25, 35)))
        button_temp.place(relx=0.5, rely=0.35, anchor=CENTER)

        button_pressure = Button(self.master, text="Pressure", style='TButton', command=lambda: open_sensor_graph("Pressure", (95, 105)))
        button_pressure.place(relx=0.5, rely=0.45, anchor=CENTER)

        button_burn_rate = Button(self.master, text="Burn Rate", style='TButton', command=lambda: open_sensor_graph("Burn Rate", (0.2, 0.6)))
        button_burn_rate.place(relx=0.5, rely=0.55, anchor=CENTER)

        button_thrust = Button(self.master, text="Thrust", style='TButton', command=lambda: open_sensor_graph("Thrust", (400, 600)))
        button_thrust.place(relx=0.5, rely=0.65, anchor=CENTER)

        button_vibration = Button(self.master, text="Vibration", style='TButton', command=lambda: open_sensor_graph("Vibration", (0.08, 0.15)))
        button_vibration.place(relx=0.5, rely=0.75, anchor=CENTER)

        # Create "Back to Home" link
        self.link_label = Label(self.master, text="Back to Home", font=("Arial", 12))
        
        self.link_label.bind("<Button-1>", self.open_file)
        self.link_label.grid(row=2, column=3, pady=10)

    def open_file(self, event):
        root.destroy()


root = Tk()
root.geometry("1340x750")
app = Application(master=root)
app.mainloop()
