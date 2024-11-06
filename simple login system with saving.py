import os

task = input("Task: ")

if task == "register":
    user = input("Username: ")
    passw = input("Password: ")

    userandpassw = f";'{user}','{passw}'"

    with open("list.txt", "a") as userandpasswfile:
        userandpasswfile.write(userandpassw)

    print("Success!")

elif task == "login":
    user = input("Username: ")
    passw = input("Password: ")

    userandpassw = f"'{user}','{passw}'"


    with open("list.txt", "r") as userandpasswfile:
        userandpasswlist = userandpasswfile.read().split(";")

    if userandpassw in userandpasswlist:
        print("Success!")
    else:
        print("Incorrect username, password or account does not exist.")

else:
    print("Invalid task.")
    
    
