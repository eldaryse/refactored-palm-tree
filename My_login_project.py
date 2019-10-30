email = input("Hi, enter your email adress !")

if email == "c@gmail.com":
    print("Hey, welcome c@gmail.com enter your password now !")
    x = input("Password")
else:
    print("Hey")


if not email == "c@gmail.com":
    print("I see a new user there !")
    new_user_name = input("So what's your name ?")
    print("Hey  " + new_user_name)
    new_password = input("So what's your password ?")
    confirm_user_name = input("So your user name is " + new_user_name + "   Is it ok ?")

if confirm_user_name == "no":
    new_new_username = input("So what is your new username ?")
    print("The change have been made, welcome   " + new_new_username)
    new_password = input("So what's your password ?")

if confirm_user_name == "yes":
    confirm_password = input("And your password is " + new_password + " Is it ok ?")
if confirm_password == "yes":
    print("So everything is ok welcome !")
if confirm_password == "no":
   new_new_password = input("So what's your new password")
   print("Your new password is  " + new_new_password)

if confirm_password == "yes" and confirm_user_name == "yes":
    input()

if x == "123":
    print("Welcome home !")


