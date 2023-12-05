import tkinter as tk
from version import app_name, version, author

def main():
    # Create the main window
    root = tk.Tk()
    root.title(f"{app_name} - Version {version}")

    # Header with version and additional information
    header_text = f"{app_name} - Version {version}\nDeveloped by {author}"
    header_label = tk.Label(root, text=header_text)
    header_label.pack()

    # Main content (add your widgets here)
    main_content_label = tk.Label(root, text="Hello, World!")
    main_content_label.pack()

    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()
