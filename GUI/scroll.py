import warnings
warnings.filterwarnings("ignore")
from dejavu import Dejavu
from dejavu.recognize import FileRecognizer, MicrophoneRecognizer
from Tkinter import *
from ttk import *
# Main window
root = Tk()
# database config
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

    if song["song_id"] == 1:
        id = Label(frm, text='Your song:  ' + song['song_name'])
        id.pack(side=TOP)
        recommend = Label(frm, text='Recommended songs:')
        recommend.pack(side=TOP)
        recommend1 = Label(frm, text='Stressed Out - Twenty One Pilots')
        recommend1.pack(side=TOP)
        recommend2 = Label(frm, text='Closer - The Chainsmokers')
        recommend2.pack(side=TOP)

## Grid sizing behavior in window
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
## Canvas
cnv = Canvas(root)
cnv.grid(row=0, column=0, sticky='nswe')
## Scrollbars for canvas
hScroll = Scrollbar(root, orient=HORIZONTAL, command=cnv.xview)
hScroll.grid(row=1, column=0, sticky='we')
vScroll = Scrollbar(root, orient=VERTICAL, command=cnv.yview)
vScroll.grid(row=0, column=1, sticky='ns')
cnv.configure(xscrollcommand=hScroll.set, yscrollcommand=vScroll.set)
## Frame in canvas
frm = Frame(cnv)
## This puts the frame in the canvas's scrollable zone
cnv.create_window(0, 0, window=frm, anchor='nw')
## Frame contents

ListenButton = Button(frm, text="Start listening", width=40)
ListenButton.bind("<Button-1>", start)
ListenButton.pack(side=TOP)

## Update display to get correct dimensions
frm.update_idletasks()
## Configure size of canvas's scrollable zone
cnv.configure(scrollregion=(0, 0, frm.winfo_width(), frm.winfo_height()))
## Go!
root.mainloop()