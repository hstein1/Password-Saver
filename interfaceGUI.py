from tkinter import *
from tkinter import messagebox
import account
import user
import admin

class InterfaceGUI:
  def __init__(self, username, password):
    self.__username = username
    self.__password = password
    
    self.__window = Tk()
    self.__window.title("Password Saver: " + self.__username)

    self.__title_label_new = Label(self.__window, text='Title: ')
    self.__username_label_new = Label(self.__window, text='Username: ')
    self.__password_label_new = Label(self.__window, text='Password: ')

    self.__title_label_new.grid(row=0)
    self.__username_label_new.grid(row=1)
    self.__password_label_new.grid(row=2)

    self.__title_entry_new = Entry(self.__window)
    self.__username_entry_new = Entry(self.__window)
    self.__password_entry_new = Entry(self.__window, show='*')

    self.__title_entry_new.grid(row = 0, column = 1)
    self.__username_entry_new.grid(row = 1, column = 1)
    self.__password_entry_new.grid(row = 2, column = 1)

    self.__new_button = Button(self.__window, text='Create New Account',\
                                       command=self.new_account)
    self.__new_button.grid(row = 3, column = 1)

    self.__title_label_delete = Label(self.__window, text='Title: ')
    self.__title_label_delete.grid(row=0, column=2)

    self.__title_entry_delete = Entry(self.__window)
    self.__title_entry_delete.grid(row=0, column=3)

    self.__delete_button = Button(self.__window, text='Delete Account',\
                                  command=self.delete_account)
    self.__delete_button.grid(row=3, column=3)

    self.__title_label_find = Label(self.__window, text='Title: ')
    self.__title_label_find.grid(row = 0, column = 4)

    self.__title_entry_find = Entry(self.__window)
    self.__title_entry_find.grid(row = 0, column = 5)

    self.__find_button = Button(self.__window, text='Find Account',\
                                command=self.find_account)
    self.__find_button.grid(row=3, column = 5)

    

    self.__user = user.User(username, password)

    mainloop()

  def valid_input_new(self):
    return(bool(self.__title_entry_new.get()) and\
           bool(self.__username_entry_new.get()) and\
           bool(self.__password_entry_new.get()))

  def valid_input_find(self):
    return bool(self.__title_entry_find.get())

  def valid_input_delete(self):
    return bool(self.__title_entry_delete.get())

  def new_account(self):
    if self.valid_input_new():
      if not self.__user.is_account(self.__title_entry_new.get()):
        self.__user.new_account(self.__title_entry_new.get(),\
                         self.__username_entry_new.get(),\
                         self.__password_entry_new.get())
        print('New Account Created')
        
        self.__title_entry_new.delete(0, END)
        self.__username_entry_new.delete(0, END)
        self.__password_entry_new.delete(0, END)
      else:
        print('Account already exists')
        messagebox.showerror("Error", "Account already exists")
    else:
      print('Invalid input')
      messagebox.showerror('Invalid Input', 'Invalid input. Please try again.')
      self.__title_entry_new.delete(0, END)
      self.__username_entry_new.delete(0, END)
      self.__password_entry_new.delete(0, END)

  def delete_account(self):
    if self.valid_input_delete():
      if self.__user.is_account(self.__title_entry_delete.get()):
        self.__user.delete_account(self.__title_entry_delete.get())
        print('Account deleted')
        self.__title_entry_delete.delete(0, END)
      else:
        print('Account does not exist')
        messagebox.showerror("Error", "Account does not exist")
        self.__title_entry_delete.delete(0, END)
    else:
      print('Invalid input')
      messagebox.showerror("Invalid Input", "Invalid input. Please try again.")
    

  def find_account(self):
    if self.valid_input_find():
      if self.__user.is_account(self.__title_entry_find.get()):
        account = self.__user.find_account(self.__title_entry_find.get())
        messagebox.showinfo(account.get_title(),\
                                           str(account))
        print('Account %s found' %self.__title_entry_find.get())
        self.__title_entry_find.delete(0, END)
      else:
        print('Account does not exist')
        messagebox.showerror("Error", "Account does not exist")
        self.__title_entry_find.delete(0, END)
    else:
      print('Invalid input')
      messagebox.showerror('Invalid Input', 'Invalid input. Please try again.')
      self.__title_entry_find.delete(0, END)

    
    
