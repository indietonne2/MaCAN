
import tkinter as tk

def main():
    # Create the main window
    root = tk.Tk()
    root.title("My Cross-Platform GUI")

    # Add widgets here
    label = tk.Label(root, text="Hello, World!")
    label.pack()

    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()
