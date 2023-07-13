# pin.py

:--- --- --- --- --- --- --- --- --- ---:--- --- --- --- --- --- --- --- --- ---:

Window Pinning Script:

This Python script allows you to pin a selected application window to the foreground, ensuring it remains on top of other windows even if you click away. The script provides a numbered list of running applications, allowing you to easily select the desired window to pin. It utilizes the pygetwindow library to interact with windows and the tkinter library to create a hidden root window. The win32gui module from the pywin32 library is used to set the selected window's position to HWND_TOPMOST, ensuring it stays in the foreground. This script is helpful for scenarios where you want to keep a specific application visible at all times while working on other tasks.

:--- --- --- --- --- --- --- --- --- ---:--- --- --- --- --- --- --- --- --- ---:

Dependancies:

    pygetwindow: This library allows you to interact with windows on your system. You can install it by running pip install pygetwindow.

    tkinter: This library provides the necessary components for creating a hidden root window. It is usually available as a built-in library with Python, so no additional installation is required.

    pywin32: This library provides access to the Windows API, including window manipulation functionality. You can install it by running pip install pywin32.

Ensure that you have these dependencies installed in your Python environment.
