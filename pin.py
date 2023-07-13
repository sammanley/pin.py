import pygetwindow as gw
import tkinter as tk
import win32gui
import win32con

def pin_window():
    root = tk.Tk()
    root.withdraw()

    windows = gw.getAllTitles()
    for index, window in enumerate(windows, start=1):
        print(f"{index}. {window}")

    if windows:
        try:
            choice = int(input("Enter the number of the window you want to pin: "))
            if 1 <= choice <= len(windows):
                window_to_pin = gw.getWindowsWithTitle(windows[choice - 1])
                hwnd = window_to_pin[0]._hWnd
                win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
                print(f"Successfully pinned '{window_to_pin[0].title}' to the foreground.")
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid input! Please enter a number.")
    else:
        print("No windows found!")

if __name__ == "__main__":
    pin_window()
