class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.logged_in = False
        self.menu()

    def menu(self):
        user_input = input("""Welcome to Chatbook , How would you like to proceed? 
                            1.Press 1 to signup
                            2.Press 2 to login
                            3.Press 3 to write a post
                            4.Press 4 to message a friend
                            5.Press any other key to exit \n""")
        if user_input =="1":
            self.signup()
        elif user_input =="2":
            self.signin()
        elif user_input =="3":
            pass
        elif user_input =="4":
            pass
        else:
            exit()


    def signup(self):
        email = input("Enter your email:")
        passw = input("Setup your password:")
        self.username = email
        self.password = passw
        print("You have Signed up successfully")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == "" and self.password == "":
            print("Please sign up first by pressing 1 in main menu")
        else:
            email = input("Enter your email:")
            passw = input("Enter your password:")
            if email == self.username and passw == self.password:
                print("You have logged in successfully")
                self.logged_in = True
            else:
                print("invalid credentials, please try again")
                self.logged_in = False
        print("\n")
        self.menu()


obj = chatbook()