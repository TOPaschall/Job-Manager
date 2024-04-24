import tkinter as tk
import customtkinter as ctk
# Utils is where randome functions are called for OOD sakes

# Error message for when the user doesn't fill out all fields in Add Job
def show_error_message():
    error_message = ctk.CTkToplevel()
    error_message.title("Error")
    error_message.geometry("200x100")
    error_message.geometry("+%d+%d" % (error_message.winfo_screenwidth() // 2 - error_message.winfo_reqwidth() // 2, error_message.winfo_screenheight() // 2 - error_message.winfo_reqheight() // 2))
    error_label = ctk.CTkLabel(error_message, text="Please fill out all fields")
    error_label.pack()
    error_button = ctk.CTkButton(error_message, text="OK", command=error_message.destroy)
    error_button.pack()

# What pops up when 'About' is clicked in the menu bar
def display_info():
        info = ctk.CTkToplevel()
        info.title("About")
        info.geometry("800x400")
        info_label = ctk.CTkLabel(info, text="This is a job application tracker.\n It will help you keep track of the jobs you have applied to.\nNo Comments™️")
        info_label.pack()