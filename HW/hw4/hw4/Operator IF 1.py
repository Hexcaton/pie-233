login = print(input("Введите логин и нажмите Enter: "))
password = print(input("Введите пароль и нажмите Enter: "))
correct_login = "user"
correct_password = "qwerty"

if login == correct_login and password == correct_password:
    print("Authentication completed")
else:
    print("Invalid Login or Password")
