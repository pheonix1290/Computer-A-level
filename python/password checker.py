def getPword(attempt):
    if attempt == 1:
        while True:
            password = input("Enter password:")
            if len(password) < 6 or len(password) > 8:
                print("Error.Password must be 6 to 8")
            else:
                break
        return password

    elif attempt == 2:
        while True:
            password = input("Re-enter password :")
            if len(password) < 6 or len(password) > 8:
                print("Error.Password must be 6 to 8. ")
            else:
                break
        return password
def main():
    while True:
        user_password = getPword(1)
        check_password = getPword(2)
        if user_password == check_password:
            print("Password change is successful")
            break
        else:
            print("Error.Passwords don't match. Please try again.")
if __name__ == '__main__':
    main()
