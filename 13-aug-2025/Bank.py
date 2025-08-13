#Encapsulation
class BankAccount:
  def __init__(self,name,balance,pin):
     self.name = name
     self.__balance = balance
     self.__pin=pin
  def __str__(self):
     return f"Account Holder's Name : {self.name}"
  def getBalance(self,pin):
    if pin==self.__pin:
      return f"Balance : {self.__balance}"
    return "Invalid pin or Account"
  def depositAmount(self,amt):
    if amt>=0:
      self.__balance += amt
      return "Amount Deposited"
    return "Deposition Failed"

print("Welcome To The Banking Facilities")

while True:
  print()
  print("Press 1 to Create Account\nPress 2 to Deposit Amount to your account\nPress 3 to Check Balance\nPress 4 to Exit")
  ch = int(input("Write your choice and press enter : "))
  if ch == 1:
    name = input("Enter Your Name :")
    pin = input("Enter your Pin  : ")
    balance = 0 
    b = BankAccount(name,balance,pin)
    print("Account Created")
  
  elif ch == 2:
    amt = int(input("Enter the Amount to be deposited :"))
    b.depositAmount(amt)

  elif ch == 3:
    p = input("Enter your pin : ")
    print(b.getBalance(pin))
  elif ch == 4:
    break;
  
  else:
    print("Service Not Available (for given choiced number)")
  