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

        #Home page
        self.home_page = tk.Frame(self)
        self.home_page.pack(fill="both", expand=True)
        self.home_page_label = tk.Label(self.home_page, text="Welcome to the Job Application Tracker", font=("Arial", 30))
        self.home_page_label.pack()

        self.logo = tk.PhotoImage(file="logo.png")
        self.logo_label = tk.Label(self.home_page, image=self.logo)
        self.logo_label.pack()

        #Home page button
        self.add_job_button = tk.Button(self.home_page, text="Add Job", command=self.add_job)
        self.add_job_button.pack()


    def display_info(self):
        info = tk.Toplevel(self)
        info.title("About")
        info.geometry("800x400")
        info_label = tk.Label(info, text="This is a job application tracker.\n It will help you keep track of the jobs you have applied to.\nNo Comments™️")
        info_label.pack()

    def add_job(self):
        self.home_page.pack_forget()
        self.add_job_page = tk.Frame(self)
        self.add_job_page.pack(fill="both", expand=True)
        self.add_job_label = tk.Label(self.add_job_page, text="Add a Job", font=("Arial", 30))
        self.add_job_label.pack()

        self.job_title_label = tk.Label(self.add_job_page, text="Job Title")
        self.job_title_label.pack()
        self.job_title_entry = tk.Entry(self.add_job_page)
        self.job_title_entry.pack()

        self.company_label = tk.Label(self.add_job_page, text="Company")
        self.company_label.pack()
        self.company_entry = tk.Entry(self.add_job_page)
        self.company_entry.pack()

        self.date_applied_label = tk.Label(self.add_job_page, text="Date Applied")
        self.date_applied_label.pack()
        self.date_applied_entry = tk.Entry(self.add_job_page)
        self.date_applied_entry.pack()

        self.status_label = tk.Label(self.add_job_page, text="Status")
        self.status_label.pack()
        self.status_entry = tk.Entry(self.add_job_page)
        self.status_entry.pack()

        self.add_button = tk.Button(self.add_job_page, text="Add", command=self.add_job_to_list)
        self.add_button.pack()

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()