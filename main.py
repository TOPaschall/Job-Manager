import tkinter as tk
from tkinter import ttk
import add_job as aj
import utils
import PIL.Image as pil

# Create the main application
class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Job Application Tracker")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")

        #Home page
        self.home_page = tk.Frame(self)
        self.home_page.pack(expand=True)
        self.home_page_label = tk.Label(self.home_page, text="Welcome to the Job Application Tracker", font=("Arial", 20))
        self.home_page_label.pack()

        #Logo
        self.logo = tk.PhotoImage(file="logo.png")
        self.logo_label = tk.Label(self.home_page, image=self.logo)
        self.logo_label.pack()

        #Add job page
        self.addJobFrame = aj.AddJob(self.home_page)

        #Home page button
        self.add_job_button = tk.Button(self.home_page, text="Add Job", command=self.addJobFrame.pack)
        self.add_job_button.pack()

        # Create a menu bar
        menubar = tk.Menu(self)

        # Configure the menu bar
        self.config(menu=menubar)

        # Create a file menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Home", command=self.go_to_home_page)
        file_menu.add_command(label="About", command=utils.display_info)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)

        # Add the file menu to the menu bar
        menubar.add_cascade(label="File", menu=file_menu)

    # Navigates to the home page
    def go_to_home_page(self):
        self.add_job_page.pack_forget()
        self.home_page.pack()

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()