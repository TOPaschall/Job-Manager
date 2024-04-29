import tkinter as tk
from tkinter import ttk
import add_job as aj
import utils
import viewJobs as vj
import homePage as hp

# Create the main application
class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Job Application Tracker")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        self.configure(bg="light blue")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Create instances of frames
        for F in (aj.AddJob, vj.viewJobs, hp.home_page):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(hp.home_page)

        # Create a menu bar
        menubar = tk.Menu(self)

        # Configure the menu bar
        self.config(menu=menubar)

        # Create a file menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="About", command=utils.display_info)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)

        # Add the file menu to the menu bar
        menubar.add_cascade(label="File", menu=file_menu)

        # Create a navigation menu
        nav_menu = tk.Menu(menubar, tearoff=0)
        nav_menu.add_command(label="Add Job", command=lambda: self.show_frame(aj.AddJob))
        nav_menu.add_command(label="View Jobs", command=lambda: self.show_frame(vj.viewJobs))

        # Add the navigation menu to the menu bar
        menubar.add_cascade(label="Navigate", menu=nav_menu)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
