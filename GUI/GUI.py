import warnings
warnings.filterwarnings("ignore")
from dejavu import Dejavu
from dejavu.recognize import FileRecognizer, MicrophoneRecognizer
from Tkinter import *
from ttk import *

root = Tk()
root.title('Name that Song!')

root.resizable(width=False, height=False)
root.geometry('349x349')
config = {
        "database": {
                "host": "127.0.0.1",
                "user": "root",
                "passwd": "tamotsu",
                "db": "dejavu",
                }
}


def start(event):
    if __name__ == '__main__':

        djv = Dejavu(config)

    secs = 8
    song = djv.recognize(MicrophoneRecognizer, seconds=secs)
    if song is None:
        print "Nothing recognized -- did you play the song out loud so your mic could hear it?"
    else:
        print "From mic with %d seconds we recognized: %s\n" % (secs, song)


status = Label(root, text="Ready to listen.........", relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)
ListenButton = Button(root, text="Start listening")
ListenButton.bind("<Button-1>", start)
ListenButton.pack(side=TOP)
canvas = Canvas(width=349, height=349, bg='black')
canvas.pack(expand=YES, fill=BOTH)
gifbackground = PhotoImage(file='/Users/markkinoshita/Desktop/CST205_Project_3-kyle/GUI images/animate.gif')
canvas.create_image(1, 1, image=gifbackground, anchor=NW)
root.mainloop()