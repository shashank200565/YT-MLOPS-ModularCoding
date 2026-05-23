class chatbook:

    __user_id = 0

    def __init__(self):
        #static method
        self.id = chatbook.__user_id
        chatbook.__user_id += 1
        #this below one is a hidden attribute
        self.__confidential = "I hate MUJ"
        self.username = ""
        self.password = ""
        self.logged_in = False
        #self.menu()

    @staticmethod
    def get_id():
        return chatbook.__user_id
    
    @staticmethod
    def set_id(val):
        chatbook.__user_id = val
        return chatbook.__user_id

    #getter
    def get_name(self):
        return self.__confidential 
    
    #setter
    def set_name(self, value):
        self.__confidential = value


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
            self.post()
        elif user_input =="4":
            self.send_msg()
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

    def post(self):
        if self.logged_in == False:
            print("Please login first to write a post")
        else:
            pst = input("Enter your post here:")
            print(f"Your post has been published successfully -> {pst}")
        print("\n")
        self.menu()

    def send_msg(self):
        if self.logged_in == True:
            text = input("Enter your message:")
            frnd = input("Enter your friend's name:")
            print(f"Your mssage -> {text} \n has been sent to {frnd} successfully")
        else:
            print("Please login first to send a message")
        print("\n")
        self.menu()

 #obj = chatbook()