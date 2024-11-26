import time

# User Class
class User:
  def __init__ (self, first_name, last_name, email, password, email_status = "inachieved"):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.password = password
    self.email_status = email_status

  def print_user_info(self):
    print(f"\n\nYour first Name: {self.first_name}")
    print(f"Your last Name: {self.last_name}")
    print(f"Your email: {self.email}")
    print(f"Your password: {self.password}\n\n")

def create_user():
  first_name = input("Enter your first name: ")
  last_name = input("Enter your last name: ")
  email = input("Enter your email: ")
  password = input("Enter your password: ")

  return User(first_name, last_name, email, password)

# User1_Info
user1 = create_user()
user1.print_user_info()

# User2_Info
user2 = create_user()
user2.print_user_info()
