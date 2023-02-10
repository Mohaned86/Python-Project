


mySentance = ' loves the color '
color_list = ['red', 'blue', 'green', 'pink', 'teal', 'black']

def color_function(name):
    lst = []
    for i in color_list:
        msg = "{0}{1}{2}".format(name,mySentance,i)
        lst.append(msg)
    return lst





def get_name():
    go = True
    while go:
        name = input("What is your name? ")
        if name == '':
            print("You need to provide your name!")
        elif name == 'ALI':
            print("ALI you may not use this software")
        else:
            go = False
    lst = color_function(name)
    for i in lst:
        print(i)


get_name()


def getSum(num1,num2):
    answer = num1 + num2
    print("The answer is {}.".format(answer))
truth1 = True
print("The truth is always {}.".format(truth1))


