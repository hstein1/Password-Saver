class Account:
  def __init__(self, title, username, password):
    self.__title = title
    self.__username = username
    self.__password = password

  def get_title(self):
    return self.__title

  def get_username(self):
    return self.__username

  def get_password(self):
    return self.__password

  def change_username(self, username):
    self.__username = username

  def change_password(self, password):
    self.__password = passwords

  def __str__(self):
    return ('Title: %s\nUsername: %s\nPassword: %s' \
            %(self.get_title(), self.get_username(), self.get_password()))
    
