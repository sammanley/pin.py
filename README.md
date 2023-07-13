# pin.py

:--- --- --- --- --- --- --- --- --- ---:--- --- --- --- --- --- --- --- --- ---:

Window Pinning Script:

This Python script allows you to pin a selected application window to the foreground, ensuring it remains on top of other windows even if you click away. The script provides a numbered list of running applications, allowing you to easily select the desired window to pin. It utilizes the pygetwindow library to interact with windows and the tkinter library to create a hidden root window. The win32gui module from the pywin32 library is used to set the selected window's position to HWND_TOPMOST, ensuring it stays in the foreground. This script is helpful for scenarios where you want to keep a specific application visible at all times while working on other tasks.

:--- --- --- --- --- --- --- --- --- ---:--- --- --- --- --- --- --- --- --- ---:

Dependancies:
```
pip install pygetwindow
pip install pywin32
```
Ensure that you have these dependencies installed in your Python environment.
