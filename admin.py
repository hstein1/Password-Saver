import user

class Admin:
  def __init__(self):
    self.__accounts = {}

  def is_account(self, username):
    return username in self.__accounts

  def new_account(self, username, password):
    if not self.is_account(username):
      self.__accounts[username] = user.User(username, password)
      

  def correct_password(self, username, password):
    if self.is_account(username):
      return self.__accounts[username].get_password() == password

  def admin_login(self, username, password):
    return username == 'hankstein' and password == 'steiner'

  def print_accounts(self):
    print(self.__accounts)

  
