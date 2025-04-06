#Password generator
"""The App is a password generator used to create strong and reliable paswords for the account. It follows the guildlines from Microsoft support
in creation of password. The passwords have at least one upper case, lower case, number and special character

This is Written and created by Alabi Olamide
"""

#import all necessary modules

import tkinter as tk
from tkinter import ttk
import random
import string
import re


#Function to call the application
def main():
    app = Application()
    app.mainloop()



class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Generator")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0,weight=1)

        frame = MainFrame(self)
        frame.grid(row=0,column=0, sticky="nsew",padx=5, pady=5)


class MainFrame(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        
        #create all necessary variables
        self.lower_case = tuple(string.ascii_lowercase)
        self.upper_case = tuple(string.ascii_uppercase)
        self.special_char = tuple("#$%&()*+,-./:;=?@[]_{|}~")
        self.number = tuple(string.digits)

        self.title_label = ttk.Label(self,text = "PASSWORD GENERATOR",font=("Helvetica", 15), anchor="center")
        self.title_label.grid(row=0, column=0,padx=5, pady=5)

        self.password_text = ttk.Entry(self,width=30)
        self.password_text.grid(row=1, column=0,padx=5, pady=5, columnspan=2, sticky="ew")

        self.slider = ttk.Scale(self, from_=9, to=25,length=200, orient=tk.HORIZONTAL, command=self.scaler)
        self.slider.grid(row=2, column=0)

        self.slider_text = ttk.Label(self, text="9")
        self.slider_text.grid(row=3, column=0)

        self.generate_button = ttk.Button(self, text="Generate New Password", command=self.generatePassword)
        self.generate_button.grid(row=4, column=0,padx=5, pady=5)


        self.quit_button =  ttk.Button(self, text="Quit", command=quit)
        self.quit_button.grid(row=6, column=0,padx=5, pady=5)

        self.end_label = ttk.Label(self,text = "Written By Banta")
        self.end_label.grid(row=7, column=0,padx=5, pady=5)
        
    #updates the label in real time with the slider widget
    def scaler(self,event):
        self.slider_text.config(text=f"{int(self.slider.get())}")
        

    def generatePassword(self):
        self.password_generated = self.passswordGenerator()
        self.password_text.delete(0,tk.END)
        self.password_text.insert(tk.END, self.password_generated)
        self.passwordStrengthIndicator()
    #Function to generate password and check if it fits the requirements
    def passwordStrengthIndicator(self):
        self.password_indicator = ttk.Label(self, text ="", )
        if self.password_indicator:
            self.password_indicator
        self.password_indicator.grid(row=5, column=0,padx=5, pady=5)
        length = self.slider.get()
        if  length > 16:
            self.password_strength = "Strong"
            self.password_indicator.config(text=self.password_strength, foreground="green")
        elif length >12:
            self.password_strength = "Good"
            self.password_indicator.config(text=self.password_strength, foreground="orange")
        else:
            self.password_strength = "Weak"
            self.password_indicator.config(text=self.password_strength, foreground="red")
        self.password_indicator.update()
        

    def passswordGenerator(self):
        new_password = ""
        len_of_passwords = int(self.slider.get())
        if len_of_passwords == False:
            len_of_passwords=9
        #The loop would run until all requirements for the password is met
        running = True
        while running:
            for i in range(0,len_of_passwords-1):
                word = random.randint(0,4)
                if word == 0:
                    letter = self.lower_case[random.randint(0,len(self.lower_case)-1)]
                elif word == 1:
                    letter = self.upper_case[random.randint(0,len(self.upper_case)-1)]
                elif word == 2:
                    letter = self.special_char[random.randint(0,len(self.special_char)-1)]
                else:
                    letter = self.number[random.randint(0,len(self.number)-1)]
                new_password += str(letter)
            lower_checker = re.compile(r"[a-z]").search(new_password)
            upper_checker = re.compile(r"[A-Z]").search(new_password)
            special_checker = re.compile(r"[#$%&()*+,-./:;=?@[]_{|}~]").search(new_password)
            number_checker = re.compile(r"[0-9]").search(new_password)
            if lower_checker and upper_checker and special_checker and number_checker:
                return new_password
                break
            else:
                new_password = ""
                
#The program would only run if its on main
if __name__ == "__main__":
    main()
