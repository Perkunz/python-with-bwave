#create a password

password = input("create a password")

confirm = input("confirm password")

attempts = 1

while password != confirm:
    if attempts == 3:
        print("attempt reached")
        break
    print('password does not match, try again')
    confirm = input("confirm password")
    attempts += 1
else:
    print("login successful")
    

