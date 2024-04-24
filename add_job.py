import json
import tkinter as tk
import customtkinter as ctk
import tkcalendar as tkc
import utils

# This is the page for the add_job button

class AddJob(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        # self.pack(fill="both", expand=True)
        # self.home_page = master

        # Create a list to store job applications
        open_job_applications = []
        # Append text input to a json file
        def add_job_to_list(self):
            if(self.company_entry.get() == "" or self.job_title_entry.get() == "" or self.status_entry.get() == "" or self.date_applied_entry.get() == ""):
                utils.show_error_message()
                return
            # Create a dictionary to store the job application
            job_application = {
                "company": self.company_entry.get(),
                "position": self.job_title_entry.get(),
                "status": self.status_entry.get(),
                "date_applied": self.date_applied_entry.get_date()
            }
            open_job_applications.append(job_application)
            # Write the job applications to a json file
            with open("job_applications.json", "w") as file:
                json.dump(open_job_applications, file)
            self.company_entry.delete(0, "end")
            self.job_title_entry.delete(0, "end")
            self.status_entry.delete(0, "end")
            self.date_applied_entry.delete(0, "end")
            self.pack_forget()

        self.add_job_page = ctk.CTkFrame(self)
        self.add_job_page.pack(fill="both", expand=True)

        self.job_title_label = ctk.CTkLabel(self.add_job_page, text="Job Title")
        self.job_title_label.pack()
        self.job_title_entry = ctk.CTkEntry(self.add_job_page)
        self.job_title_entry.pack()

        self.company_label = ctk.CTkLabel(self.add_job_page, text="Company")
        self.company_label.pack()
        self.company_entry = ctk.CTkEntry(self.add_job_page)
        self.company_entry.pack()

        self.date_applied_label = ctk.CTkLabel(self.add_job_page, text="Date Applied")
        self.date_applied_label.pack()
        self.date_applied_entry = tkc.Calendar(self.add_job_page)
        self.date_applied_entry.pack()

        self.status_label = ctk.CTkLabel(self.add_job_page, text="Status")
        self.status_label.pack()
        self.status_entry = ctk.CTkEntry(self.add_job_page)
        self.status_entry.pack()

        self.add_button = ctk.CTkButton(self.add_job_page, text="Add", command=lambda: add_job_to_list(self))

        self.add_button.pack()