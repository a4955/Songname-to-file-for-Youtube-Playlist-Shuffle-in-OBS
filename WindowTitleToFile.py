import pygetwindow as gw
import tkinter as tk
from tkinter import ttk
import time
import threading
import win32gui

output_file = "selected_window_title.txt"

# Get all open windows
def get_window_titles():
    windows = gw.getAllWindows()
    window_titles = [(window.title, window._hWnd) for window in windows]
    return window_titles

# Truncate the title based on quotation marks, made specifically with YTPLR in mind
def truncate_title(title):
    first_quote_index = title.find('"')
    last_quote_index = title.rfind('"')

    # If both quotes are found, truncate accordingly
    if first_quote_index != -1 and last_quote_index != -1 and first_quote_index < last_quote_index:
        title = title[first_quote_index + 1:last_quote_index]
    
    return title

def write_to_file(title):
    with open(output_file, 'w') as file:
        file.write(title)

# Window tracking is based on HWND
def track_window(hwnd, label):
    current_title = None
    while True:
        active_title = win32gui.GetWindowText(hwnd)
        if active_title != current_title:
            if active_title:
                truncated_title = truncate_title(active_title)
                label.config(text=f"Current Window Title: {truncated_title}")
                write_to_file(truncated_title)
                print(f"Window title updated: {truncated_title}")
            current_title = active_title
        time.sleep(1)  # Check every second

def start_tracking(event, hwnd, label):
    # Tracking done in a separate thread
    tracking_thread = threading.Thread(target=track_window, args=(hwnd, label))
    tracking_thread.daemon = True
    tracking_thread.start()

def populate_dropdown(window_titles, dropdown, label):
    dropdown['values'] = [title for title, hwnd in window_titles] 
    def on_select(event):
        selected_title = dropdown.get()
        # Find HWND for the selected window
        selected_window = next(hwnd for title, hwnd in window_titles if title == selected_title)
        start_tracking(event, selected_window, label)
    dropdown.bind('<<ComboboxSelected>>', on_select)

root = tk.Tk()
root.title("Select Window to Track")
root.geometry("450x100")
root.configure(bg="#333333")
label = tk.Label(root, text="Select a window from the dropdown to track its title.", bg="#333333", fg="white")
label.pack(pady=10)
dropdown = ttk.Combobox(root, width=60)
dropdown.pack(pady=10)
style = ttk.Style()
style.theme_use('default')
style.configure("TCombobox", fieldbackground="#555555", background="#555555", foreground="white")

window_titles = get_window_titles()
populate_dropdown(window_titles, dropdown, label)

root.mainloop()
