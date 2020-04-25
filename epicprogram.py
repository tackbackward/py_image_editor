import PySimpleGUI as sg
import easygui
import sys
from PIL import Image

def rotateimage(fname):
    image = (fname)
    msg = "How do I edit this image?"
    choices = ["Rotate","Flip","Greyscale","Logo","Cancel"]
    reply = easygui.buttonbox(msg, image=image, choices=choices)
    if reply == "Cancel":
        start()

    if reply == "Rotate":
        image = Image.open(fname)
        rotatedimage = image.rotate(90, expand=True)
        rotatedimage.save(fname)
        rotateimage(fname)

    if reply == "Flip":
        image = Image.open(fname)
        flippedimage = image.transpose(Image.FLIP_LEFT_RIGHT)
        flippedimage.save(fname)
        rotateimage(fname)

    if reply == "Greyscale":
        image = Image.open(fname)
        greyimage = image.convert('L')
        greyimage.save(fname)
        rotateimage(fname)

    if reply == "Logo":
        image = Image.open(fname)
        if len(sys.argv) == 1:
            event, values = sg.Window('Rotator',
                            [[sg.Text('Logo to open')],
                            [sg.In(), sg.FileBrowse()],
                            [sg.Open(), sg.Cancel()]]).read(close=True)
            fname2 = values[0]
        else:
            fname2 = sys.argv[1]

        if not fname2:
            sg.popup("Ok", "No filename supplied")
            rotateimage(fname)


        else:
            logo = Image.open(fname2)
            image_copy = image.copy()
            position = ((image_copy.width - logo.width), (image_copy.height - logo.height))
            image_copy.paste(logo, position)
            image_copy.save(fname)
            rotateimage(fname)




def start():
    if len(sys.argv) == 1:
        event, values = sg.Window('Rotator',
        [[sg.Text('Image to open')],
        [sg.In(), sg.FileBrowse()],
        [sg.Open(), sg.Cancel()]]).read(close=True)
        fname = values[0]
    else:
        fname = sys.argv[1]

    if not fname:
        sg.popup("Ok", "No file")
        


    else:
        rotateimage(fname)

start()

