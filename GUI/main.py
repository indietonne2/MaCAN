# main.py
import tkinter as tk
from version import version, author
from version import app_name, version, author

class MaCANApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Debugging print statement
        print("Initializing MaCANApp")

        # Setting the window title with the app name and version number
        self.title(f"{app_name} - v{version}")
        # Call to create widgets for the GUI
        self.create_widgets()

    def create_widgets(self):
        # Debugging print statement
        print("Creating widgets")

        # Creating a menu bar
        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)

        # Creating a file menu with an exit option
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.quit)
        self.menu_bar.add_cascade(label="File", menu=file_menu)

        # Creating a status bar to display the author information
        self.status_bar = tk.Label(self, text=f"Developed by {__author__}", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Creating the main content area as a text widget
        self.main_content = tk.Text(self)
        self.main_content.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    # Debugging print statement
    print("Starting MaCANApp")

    app = MaCANApp()
    app.mainloop()
    print("Exiting MaCANApp")  # This line will execute after closing the window
