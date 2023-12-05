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
        print("creating menu bar")

        # Creating a file menu with an exit option
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.quit)
        self.menu_bar.add_cascade(label="File", menu=file_menu)
        print("creating file menu")

        # Creating a status bar to display the author information
        self.status_bar = tk.Label(self, text=f"Developed by {author}", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        print("creating status bar")
        # Creating the main content area as a text widget
        self.main_content = tk.Text(self)
        self.main_content.pack(fill=tk.BOTH, expand=True)
        print("status bar created")

if __name__ == "__main__":
    # Debugging print statement
    print("Starting MaCANApp")

    app = MaCANApp()
    app.mainloop()
    print("Exiting MaCANApp")  # Thi
    print("pycharm does not support using tk without a mainloop")
    # https://stackoverflow.com/questions/51253078/tkinter-isnt-working-with-pycharm" s line will execute after closing the window. Regular python shell and IDLE supports using tk without a mainloop. This is done by several hooks, installed when a tkapp object is being initialized, which handles Tk events while the shell is waiting for user input. However pycharm does not support this. So inorder to diplay your window using pycharm, you have to call
    import tkinter as tk

    root = tk.Tk()
    root.title("Test Window")
    label = tk.Label(root, text="Hello, Tkinter!")
    label.pack()
    root.mainloop()