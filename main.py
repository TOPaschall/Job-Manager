import tkinter as tk
import customtkinter as ctk
import add_job as aj

# Create the main application
class MainApplication(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Job Application Tracker")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        self.create_widgets()

        #Home page
        self.home_page = ctk.CTkFrame(self)
        self.home_page.pack(fill="both", expand=True)
        self.home_page_label = ctk.CTkLabel(self.home_page, text="Welcome to the Job Application Tracker", font=("Arial", 20))
        self.home_page_label.pack()
        self.home_page_label.pack()

        self.logo = tk.PhotoImage(file="logo.png")
        self.logo_label = ctk.CTkLabel(self.home_page, image=self.logo)
        self.logo_label.pack()

        #Add job page
        self.addJobFrame = aj.AddJob(self.home_page)

        #Home page button
        self.add_job_button = ctk.CTkButton(self.home_page, text="Add Job", command=self.addJobFrame.pack)
        self.add_job_button.pack()

        # Create a menu bar
        menubar = tk.Menu(self)

        # Configure the menu bar
        self.config(menu=menubar)

        # Create a file menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Home", command=self.go_to_home_page)
        file_menu.add_separator()
        file_menu.add_command(label="About", command=self.display_info)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)

        # Add the file menu to the menu bar
        menubar.add_cascade(label="File", menu=file_menu)

    # This is what is displayed when 'About' is clicked
    def display_info(self):
        info = ctk.CTkToplevel(self)
        info.title("About")
        info.geometry("800x400")
        info_label = ctk.CTkLabel(info, text="This is a job application tracker.\n It will help you keep track of the jobs you have applied to.\nNo Comments™️")
        info_label.pack()

    # This is the Job Manager title at the top of the window
    def create_widgets(self):
        self.label = ctk.CTkLabel(self, text="Job Manager", font=("Arial", 30))
        self.label.pack()

    # Navigates to the home page
    def go_to_home_page(self):
        self.add_job_page.pack_forget()
        self.home_page.pack()

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()