import tkinter as tk
import utils as ut
import json
import homePage as hp

class viewJobs(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.view_job_page = tk.Frame(self)
        self.view_job_page.pack(fill="both", expand=True)

        # Create a canvas
        self.canvas = tk.Canvas(self.view_job_page)
        self.canvas.pack(side="left", fill="both", expand=True)

        # Create a scrollbar
        self.scrollbar = tk.Scrollbar(self.view_job_page, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        # Configure the canvas to use the scrollbar
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Create a frame inside the canvas
        self.scrollable_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Bind the scrollbar to the canvas
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Import job applications from JSON file
        try:
            with open('job_applications.json', 'r') as file:
                job_applications = json.load(file)
        except json.decoder.JSONDecodeError:
            job_applications = []

        # Display job applications in the frame
        for i, job in enumerate(job_applications):
            self.job_frame = tk.Frame(self.scrollable_frame, borderwidth=2, relief="solid")
            self.job_frame.pack(pady=10, anchor="center")

            self.job_label = tk.Label(self.job_frame, text=f"Job {i+1}: {job['position']}")
            self.job_label.pack(pady=5)

            self.company_label = tk.Label(self.job_frame, text=f"Company: {job['company']}")
            self.company_label.pack()

            self.date_applied_label = tk.Label(self.job_frame, text=f"Date Applied: {job['date_applied']}")
            self.date_applied_label.pack()

            self.status_label = tk.Label(self.job_frame, text=f"Status: {job['status']}")
            self.status_label.pack()

            # Add a remove button to each job frame
            self.remove_button = tk.Button(self.job_frame, text="Remove", command=lambda index=i: self.remove_job(index))
            self.remove_button.pack()

        self.back_button = tk.Button(self.view_job_page, text="Back to Home", command=lambda: controller.show_frame(hp.home_page), bg="red", fg="white", font=("Arial", 12, "bold"), relief="raised", bd=2)
        self.back_button.pack()
        self.back_button.place(relx=0.5, rely=0.5, anchor="center")

        self.reload_button = tk.Button(self.view_job_page, text="Reload", command=self.reload_frame, bg="green", fg="white", font=("Arial", 12, "bold"), relief="raised", bd=2)
        self.reload_button.pack()
        self.reload_button.place(relx=0.5, rely=0.6, anchor="center")

    def remove_job(self, index):
        # Import job applications from JSON file
        try:
            with open('job_applications.json', 'r') as file:
                job_applications = json.load(file)
        except json.decoder.JSONDecodeError:
            job_applications = []

        # Remove the selected job from the list
        if index < len(job_applications):
            job_applications.pop(index)

        # Save the updated job applications to the JSON file
        with open('job_applications.json', 'w') as file:
            json.dump(job_applications, file)

        # Reload the frame to reflect the changes
        self.reload_frame()

    def reload_frame(self):
        # Clear existing job frames
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        # Import job applications from JSON file
        try:
            with open('job_applications.json', 'r') as file:
                job_applications = json.load(file)
        except json.decoder.JSONDecodeError:
            job_applications = []

        # Display job applications in the frame
        for i, job in enumerate(job_applications):
            self.job_frame = tk.Frame(self.scrollable_frame, borderwidth=2, relief="solid")
            self.job_frame.pack(pady=10)

            self.job_label = tk.Label(self.job_frame, text=f"Job {i+1}: {job['position']}")
            self.job_label.pack(pady=5)

            self.company_label = tk.Label(self.job_frame, text=f"Company: {job['company']}")
            self.company_label.pack()

            self.date_applied_label = tk.Label(self.job_frame, text=f"Date Applied: {job['date_applied']}")
            self.date_applied_label.pack()

            self.status_label = tk.Label(self.job_frame, text=f"Status: {job['status']}")
            self.status_label.pack()

            # Add a remove button to each job frame
            self.remove_button = tk.Button(self.job_frame, text="Remove", command=lambda index=i: self.remove_job(index))
            self.remove_button.pack()
