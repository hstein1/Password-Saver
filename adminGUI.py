from tkinter import *
from tkinter import messagebox
import interfaceGUI

import admin

class AdminGUI:
  def __init__(self):
    self.__window = Tk()
    self.__window.title("Admin")

    self.__username_label_su = Label(self.__window, text='Username: ')
    self.__password_label_su = Label(self.__window, text='Password: ')

    self.__username_label_su.grid(row=0)
    self.__password_label_su.grid(row=1)

    self.__username_entry_su = Entry(self.__window)
    self.__password_entry_su = Entry(self.__window, show='*')

    self.__username_entry_su.grid(row=0, column=1)
    self.__password_entry_su.grid(row=1, column=1)

    self.__signup_button = Button(self.__window, text='SIGN UP',\
                                 command=self.sign_up)
    self.__signup_button.grid(row=2)

    self.__username_label_li = Label(self.__window, text='Username: ')
    self.__password_label_li = Label(self.__window, text='Password: ')

    self.__username_label_li.grid(row=0, column=3)
    self.__password_label_li.grid(row=1, column=3)

    self.__username_entry_li = Entry(self.__window)
    self.__password_entry_li = Entry(self.__window, show='*')

    self.__username_entry_li.grid(row=0, column=4)
    self.__password_entry_li.grid(row=1, column=4)

    self.__login_button = Button(self.__window, text='LOGIN',\
                                 command=self.login)
    self.__login_button.grid(row=2, column=3)

    self.__admin = admin.Admin()

    mainloop()

  def valid_input_su(self):
    return bool(self.__username_entry_su.get()) and\
           bool(self.__password_entry_su.get())

  def valid_input_li(self):
    return bool(self.__username_entry_li.get()) and\
           bool(self.__password_entry_li.get())

  def sign_up(self):
    if self.valid_input_su():
      username = self.__username_entry_su.get()
      password = self.__password_entry_su.get()
      if self.__admin.is_account(username):
        messagebox.showerror("Error", "Username taken. Try again")
        print('Signup attempt failed. Already an account.')
        self.__username_entry_su.delete(0, END)
        self.__password_entry_su.delete(0, END)
      else:
        self.__admin.new_account(username, password)
        print('New account created')
        self.__username_entry_su.delete(0, END)
        self.__password_entry_su.delete(0, END)
    else:
      print('Invalid input')
      messagebox.showerror("Invalid Input", "Invalid input. Please try again.")
      self.__username_entry_su.delete(0, END)
      self.__password_entry_su.delete(0, END)

  def login(self):
    if self.valid_input_li():
      username = self.__username_entry_li.get()
      password = self.__password_entry_li.get()
      if self.__admin.is_account(username) and\
         self.__admin.correct_password(username, password):
        print('Login successful')
        self.__username_entry_li.delete(0, END)
        self.__password_entry_li.delete(0, END)
        interfaceGUI.InterfaceGUI(username, password)
      elif self.__admin.is_account(username) and\
           not self.__admin.correct_password(username, password):
        print('Unsuccessful Login')
        self.__username_entry_li.delete(0, END)
        self.__password_entry_li.delete(0, END)
        messagebox.showwarning("Fail", "Login Failed")
      elif self.__admin.admin_login(username, password):
        self.__admin.print_accounts()
        self.__username_entry_li.delete(0, END)
        self.__password_entry_li.delete(0, END)
      else:
        print('No account found')
        self.__username_entry_li.delete(0, END)
        self.__password_entry_li.delete(0, END)
        messagebox.showwarning("No Account", "No account found")
    else:
      print('Invalid input')
      messagebox.showerror("Invalid Input", "Invalid input. Please try again.")
      self.__username_entry_li.delete(0, END)
      self.__password_entry_li.delete(0, END)

AdminGUI()
      
      

  
      
    
