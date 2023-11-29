import os
import shutil
import tkinter as tk
from tkinter import filedialog

def recover_deleted_files(source_dir, destination_dir):
    try:
        for root, _, files in os.walk(source_dir):
            for file in files:
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination_dir, file)

                if not os.path.exists(destination_path):
                    shutil.copy2(source_path, destination_path)
        result_label.config(text="Recovery successful!")
    except Exception as e:
        result_label.config(text="Error: " + str(e))

def select_directories():
    source_dir = filedialog.askdirectory(title="Select Source Directory")
    destination_dir = filedialog.askdirectory(title="Select Destination Directory")

    if source_dir and destination_dir:
        recover_deleted_files(source_dir, destination_dir)

window = tk.Tk()
window.title("Basic Data Recovery Tool")

recover_button = tk.Button(window, text="Recover Deleted Files", command=select_directories)
result_label = tk.Label(window, text="")

recover_button.pack()
result_label.pack()

window.mainloop()
