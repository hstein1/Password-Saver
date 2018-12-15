import account

class User:
  def __init__(self, username, password):
    self.__username = username
    self.__password = password
    self.__accounts = {}


  def get_username(self):
    return self.__username

  def get_password(self):
    return self.__password

  def has_accounts(self):
    return bool(self.__accounts)

  def is_account(self, title):
    if self.has_accounts():
      return title in self.__accounts

  def find_account(self, title):
    if self.has_accounts():
      return self.__accounts[title]

  def new_account(self, title, username, password):
    if not self.is_account(title):
      self.__accounts[title] = account.Account(title, username, password)

  def delete_account(self, title):
    if self.is_account(title):
      del self.__accounts[title]
    else:
      print('Not an account')

  def __str__(self):
    return ('Username: %s\nPassword: %s\n' \
            %(self.get_username(), self.get_password()) + str(self.__accounts))
  

  
