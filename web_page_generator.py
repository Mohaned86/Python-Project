


import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        self.cust_label = Label(text="Enter custom text or click the Default HTML page button")
        self.cust_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))
        #Creates Default HTML Page Button.
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        #Positions Default HTML Page button in GUI using tkinter grid()
        self.btn.grid(row=2, column=0, padx=(10, 10), pady=(10, 10))

        self.btn_cust = Button(self.master, text="Sumbit Custom Text", width=30, height=2, command=self.SubmitCustom)
        
        self.btn_cust.grid(row=2, column=1, padx=(10, 10), pady=(10, 10))
        self.custom = Entry(width=100)
        self.custom.grid(row=1, column=0, columnspan=5, padx=(10, 10), pady=(10, 10))
        


    #Creates function that will create an HTML document
    def defaultHTML(self):
        #Creates a variable to save the text we want to disply in the web page.
        htmlText = "Stay tuned for our amazing summer sale!"
        #Creates a new HTML file using open method.
        htmlFile = open("index.html", "w")
        #Creates the HTML page.
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        #.write to specified text will be inserted.
        htmlFile.write(htmlContent)
        #.close for close the file and free up any system resources.
        htmlFile.close()
        #.oper to create a new file.
        webbrowser.open_new_tab("index.html")


    #Creates function that will create an HTML document
    def SubmitCustom(self):
        #Creates a variable to save the text we want to disply in the web page.
        #Creates a new HTML file using open method.
        htmlFile = open("index.html", "w")
        #Creates the HTML page.
        htmlContent = "<html>\n<body>\n<h1>" + self.custom.get() + "</h1>\n</body>\n</html>"
        #.write to specified text will be inserted.
        htmlFile.write(htmlContent)
        #.close for close the file and free up any system resources.
        htmlFile.close()
        #.oper to create a new file.
        webbrowser.open_new_tab("index.html")
        


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
