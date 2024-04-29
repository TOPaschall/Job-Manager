import tkinter as tk
import add_job as aj
import viewJobs as vj
import utils as ut
import main

class home_page(tk.Frame):
    def __init__(self, parent, controller):  
        tk.Frame.__init__(self, parent)  
        self.configure(bg="light blue")
        #Home page
        self.home_page = tk.Frame(self)
        self.home_page.pack(expand=True)
        self.home_page_label = tk.Label(self.home_page, text="Welcome to the Job Application Tracker", font=("Arial", 20), bg="light blue", width = 500)
        self.home_page_label.pack()

        #Logo
        self.logo = tk.PhotoImage(file="logo.png")
        self.logo_label = tk.Label(self.home_page, image=self.logo, height=500, width=500)
        self.logo_label.pack()

        self.view_jobs_button = tk.Button(self.home_page, text="View Current Jobs",  
                    command=lambda: controller.show_frame(vj.viewJobs),bg="green", fg="white", font=("Arial", 12, "bold"), relief="raised", bd=2)
        self.view_jobs_button.pack()

        self.add_job_button = tk.Button(self.home_page, text="Add Job",  
                    command=lambda: controller.show_frame(aj.AddJob),bg="red", fg="white", font=("Arial", 12, "bold"), relief="raised", bd=2)
        self.add_job_button.pack()
