from tkinter import *
from dicothomie2 import dicothomie
from newton import newton
from steffenson import Steffenson
from balayage import search_intervals
from steffenson import Steffenson
from gestion import get_intervals


def get_function(function):
    return eval(f'lambda x: {function}')


def Answer(event):
    func = get_function(entry.get())
    __INT__ = list(map(int, ints.get().split()))
    precis = float(prec.get())

    __TRUEINT__ = get_intervals(search_intervals, func, *__INT__, prec)
    for val in __TRUEINT__:

        formatString = f"SUR L'INTERVALLE {val}:\n\nDichotomie:\n" + str(dicothomie(func, *val, precis)) + "\n" \
                                                                                   "Stenffensen:\n" + str(
            Steffenson(func, *val, precis))

    chaine.configure(text=formatString)


a, b, = (-3, 3)
precision = 10 ** (-10)
fen = Tk()

intervals = Label(fen, text="Entrer [a, b]")
ints = Entry(fen, width=57)

precPre = Label(fen, text='Entrez la précision')
prec = Entry(fen, width=57)

presentation = Label(fen, text="Entrez la fonction monotone dont vous cherchez la solution ci-dessous")
entry = Entry(fen, width=57)
entry.bind("<Return>", Answer)

chaine = Label(fen)
quitbtn = Button(fen, text="Quitter", command=fen.quit)

intervals.pack()
ints.pack()

precPre.pack()
prec.pack()

presentation.pack()
quitbtn.pack(side=BOTTOM)
entry.pack()
chaine.pack()
fen.mainloop()
