import json
import tkinter as tk
import tkcalendar as tkc
import utils
import homePage as hp

# This is the page for the add_job button

class AddJob(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create a list to store job applications
        open_job_applications = []
        # Append text input to a json file
        def add_job_to_list(self):
            if(self.company_entry.get() == "" or self.job_title_entry.get() == "" or self.status_entry.get() == "" or self.date_applied_entry.get_date() == ""):
                utils.show_error_message()
                return
            
            with open('job_applications.json', 'r') as file:
                try:
                    job_applications = json.load(file)
                except json.decoder.JSONDecodeError:
                    job_applications = []
            # Create a dictionary to store the job application
            job_application = {
                "id": len(job_applications) + 1,
                "company": self.company_entry.get(),
                "position": self.job_title_entry.get(),
                "status": self.status_entry.get(),
                "date_applied": self.date_applied_entry.get_date()
            }
            if len(job_applications) != 0:
                with open('job_applications.json', 'w') as file:
                    for id in job_applications:
                        del id['id']

            open_job_applications.append(job_application)
            open_job_applications.extend(job_applications)
            # Write the job applications to a json file
            with open("job_applications.json", "w") as file:
                json.dump(open_job_applications, file)
            self.company_entry.delete(0, "end")
            self.job_title_entry.delete(0, "end")
            self.status_entry.delete(0, "end")
            self.date_applied_entry.selection_clear()
            self.pack_forget()

        self.add_job_page = tk.Frame(self)
        self.add_job_page.pack(fill="both", expand=True)

        self.job_title_label = tk.Label(self.add_job_page, text="Job Title", font=("Arial", 18, "bold"))
        self.job_title_label.pack()
        self.job_title_entry = tk.Entry(self.add_job_page)
        self.job_title_entry.pack()
        
        self.spacer = tk.Label(self.add_job_page, text="")
        self.spacer.pack()

        self.company_label = tk.Label(self.add_job_page, text="Company", font=("Arial", 18, "bold"))
        self.company_label.pack()
        self.company_entry = tk.Entry(self.add_job_page)
        self.company_entry.pack()
        self.spacer = tk.Label(self.add_job_page, text="")
        self.spacer.pack()

        self.date_applied_label = tk.Label(self.add_job_page, text="Date Applied", font=("Arial", 18, "bold"))
        self.date_applied_label.pack()
        self.date_applied_entry = tkc.Calendar(self.add_job_page)
        self.date_applied_entry.pack()
        self.spacer = tk.Label(self.add_job_page, text="")
        self.spacer.pack()

        self.status_label = tk.Label(self.add_job_page, text="Status", font=("Arial", 18, "bold"))
        self.status_label.pack()
        self.status_entry = tk.Entry(self.add_job_page)
        self.status_entry.pack()
        self.spacer = tk.Label(self.add_job_page, text="")
        self.spacer.pack()

        self.add_button = tk.Button(self.add_job_page, text="Add", command=lambda: add_job_to_list(self), bg="green", fg="white", font=("Arial", 12, "bold"), relief="raised", bd=2)


        self.add_button.pack()

        self.back_button = tk.Button(self.add_job_page, text="Back to Home", command=lambda: controller.show_frame(hp.home_page),bg="red", fg="white", font=("Arial", 12, "bold"), relief="raised", bd=2)
        self.back_button.pack()