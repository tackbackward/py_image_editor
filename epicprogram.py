import PySimpleGUI as sg
import easygui
import sys
from PIL import Image

def rotateimage():
    image = (fname)
    msg = "How do I edit this image?"
    choices = ["Rotate","Flip","Greyscale"]
    reply = easygui.buttonbox(msg, image=image, choices=choices)
    if reply == "Rotate":
        image = Image.open(fname)
        rotatedimage = image.rotate(90, expand=True)
        rotatedimage.save(fname)
        rotateimage()

    if reply == "Flip":
        image = Image.open(fname)
        flippedimage = image.transpose(Image.FLIP_LEFT_RIGHT)
        flippedimage.save(fname)
        rotateimage()

    if reply == "Greyscale":
        image = Image.open(fname)
        greyimage = image.convert('L')
        greyimage.save(fname)
        rotateimage()




if len(sys.argv) == 1:
    event, values = sg.Window('Rotator',
                    [[sg.Text('Image to open')],
                    [sg.In(), sg.FileBrowse()],
                    [sg.Open(), sg.Cancel()]]).read(close=True)
    fname = values[0]
else:
    fname = sys.argv[1]

if not fname:
    sg.popup("Cancel", "No filename supplied")
    raise SystemExit("Cancelling: no filename supplied")
else:

    rotateimage()
