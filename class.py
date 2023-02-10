class player:
    # create new class and give it object
    Name = ''
    Email = ''
    Password = ''
    Age = ''
    Weigh = ''
    Length = ''
    # create method for player login
    
    def getLogin(self):
        Name = input("Enter your name: ")
        Email = input("Enter your email: ")
        Password = input("Enter your password: ")
        if (Email == self.email and Password == self.password):
            print("Welcome, {}!".format(Name))
        else:
            ("Incorrect email or password.")


class coach(player):
    # create child class that inherite from the player class and give it spicifice object
    language = ''
    salery = ''
    ID = ''
    
    # create method for coach login but istade of using password they use their ID
    def getLogin(self):
        Name = input("Enter your name: ")
        Email = input("Enter your email: ")
        ID = input("Enter your id: ")
        if (Email == self.email and Password == self.password):
            print("Welcome, {}!".format(Name))
        else:
            ("Incorrect email or id.")

    


class doctor(player):
    # create child class that inherite from the player class and give it spicifice object
    spicilize = ''
    performance = ''
    License_No = ''
    
    # create method for coach login but istade of using password they use their license
    def getLogin(self):
        Name = input("Enter your name: ")
        Email = input("Enter your email: ")
        License_No = input("Enter your license no: ")
        if (Email == self.email and Password == self.password):
            print("Welcome, {}!".format(Name))
        else:
            ("Incorrect email or license no.")
    
