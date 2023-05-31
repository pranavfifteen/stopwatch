import datetime
import tkinter as tk
import simpy
import threading

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = datetime.timedelta()

    def start(self):
        self.start_time = datetime.datetime.now()

    def stop(self):
        if self.start_time:
            end_time = datetime.datetime.now()
            self.elapsed_time += end_time - self.start_time
            self.start_time = None

    def reset(self):
        self.start_time = None
        self.elapsed_time = datetime.timedelta()

    def get_elapsed_time(self):
        if self.start_time:
            current_time = datetime.datetime.now()
            return self.elapsed_time + (current_time - self.start_time)
        else:
            return self.elapsed_time

def update_label(stopwatch, label):
    while True:
        elapsed_time = stopwatch.get_elapsed_time()
        label.config(text=str(elapsed_time))
        label.update()
        simpy.rt.sleep(0.01)

def show_date_time():
    now = datetime.datetime.now()
    print(f"Current Date and Time: {now}")

def main():
    root = tk.Tk()
    root.title("Stopwatch")

    stopwatch = Stopwatch()

    label = tk.Label(root, text="00:00:00.000", font=("Arial", 20))
    label.pack(pady=20)

    start_button = tk.Button(root, text="Start", command=stopwatch.start)
    start_button.pack()

    stop_button = tk.Button(root, text="Stop", command=stopwatch.stop)
    stop_button.pack()

    reset_button = tk.Button(root, text="Reset", command=stopwatch.reset)
    reset_button.pack()

    date_time_button = tk.Button(root, text="Show Date and Time", command=show_date_time)
    date_time_button.pack()

    thread = threading.Thread(target=update_label, args=(stopwatch, label))
    thread.daemon = True
    thread.start()

    root.mainloop()

if __name__ == "__main__":
    main()
