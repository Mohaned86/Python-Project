


import app



def print_app2():
    name = (__name__)
    return name



if __name__ == "__main__":
    #The following is colling code within this script
    print("I am running code from {}".format(print_app2()))


    #The following is colling code from the imported app.py
    print("I am running code from {}".format(app.print_app()))
