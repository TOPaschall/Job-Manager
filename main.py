import tkinter as tk

# Create the main application
class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Job Application Tracker")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")

        # Create a menu bar
        menubar = tk.Menu(self)
        
        # Create a file menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="About", command=self.display_info)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)
        
        # Add the file menu to the menu bar
        menubar.add_cascade(label="File", menu=file_menu)
        
        # Configure the menu bar
        self.config(menu=menubar)

    def display_info(self):
        info = tk.Toplevel(self)
        info.title("About")
        info.geometry("800x400")
        info_label = tk.Label(info, text="This is a job application tracker.\n It will help you keep track of the jobs you have applied to.\nNo Comments™️")
        info_label.pack()

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()