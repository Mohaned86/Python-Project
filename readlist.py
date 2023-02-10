
import os



def openFile():
    with open('list.txt', 'r') as f:
        data = f.read()
        print(data)
        f.close()

fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
for x in fileList:
    if x.endswith('txt'):
        print(x)


if __name__ == "__main__":
    openFile()
