def getPword(attempt):
    if attempt == 1:
        password = input("Enter password:")
        if len(password) < 6 or len(password) > 8:
            print("Error.Password must be 6 to 8")

        return password

    elif attempt == 2:
        password = input("Re-enter password :")
        if len(password) < 6 or len(password) > 8:
            print("Error.Password must be 6 to 8. ")
            password = 'true'
        return password
def main():
   user_password = getPword(1)

   if len(user_password) < 6 or len(user_password) > 8:
     check_password = getPword(2)

     if  check_password == 'true':
       print("Password change is successful")
     else:
       print("Error.Passwords don't match")
   else:
    print("Password change is successful")
if __name__ == '__main__':
    main()
