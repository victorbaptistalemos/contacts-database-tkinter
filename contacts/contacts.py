from tkinter import CENTER, E, Label, LabelFrame, PhotoImage, Tk, W
from tkinter.ttk import Button as TButton
from tkinter.ttk import Entry as TEntry
from tkinter.ttk import Label as TLabel
from tkinter.ttk import Style, Treeview


class Contacts:
    # __database = '.contacts.s3db'

    def __init__(self, root: Tk) -> None:
        self.root: Tk = root
        style: Style = Style()
        style.configure('.', font='TimesNewRoman 12', background='black', foreground='violet')
        style.configure('TLabel', font='TimesNewRoman 14')
        style.map(
            'TEntry',
            foreground=[('!focus', 'black'), ('selected', 'purple')],
            background=[('!focus', 'violet'), ('selected', 'violet')],)
        style.configure('TButton', font='TimesNewRoman 14 bold')
        style.map(
            'TButton',
            background=[('active', 'purple'), ('!active', 'violet')],
            foreground=[('active', 'black'), ('!active', 'black')])
        style.configure('Treeview', fieldbackground='black')
        style.map(
            'Treeview',
            foreground=[('selected', 'black'), ('!selected', 'violet')],
            background=[('selected', 'violet'), ('!selected', 'black')],
        )
        style.configure('Treeview.Heading', font='TimesNewRoman 12 bold')
        style.map(
            'Treeview.Heading',
            background=[('active', 'violet'), ('!active', 'violet')],
            foreground=[('active', 'black'), ('!active', 'black')]
        )
        self.gui()

    def gui(self) -> None:
        self.root.configure(bg='black')
        self.top_frame()
        self.contacts_icon()
        self.bottom_frame()

    def top_frame(self) -> None:
        top_frame = LabelFrame(
            self.root,
            text='Criar novo contato',
            background='black',
            foreground='violet',
            font='TimesNewRoman 14 bold',
            labelanchor='n',
            bd=0
        )
        top_frame.place(x=25, y=10, width=400, height=150)
        TLabel(top_frame, text='Nome:').place(x=75, y=10, anchor=E)
        TLabel(top_frame, text='Email:').place(x=75, y=35, anchor=E)
        TLabel(top_frame, text='Número:').place(x=75, y=60, anchor=E)
        TEntry(top_frame).place(x=76, y=10, anchor=W, width=299)
        TEntry(top_frame).place(x=76, y=35, anchor=W, width=299)
        TEntry(top_frame).place(x=76, y=60, anchor=W, width=299)
        TButton(top_frame, text='Adicionar contato').place(x=200, y=100, anchor=CENTER, width=200)

    @staticmethod
    def contacts_icon() -> None:
        icon: PhotoImage = PhotoImage(file='contacts/.contacts.gif')
        label: Label = Label(image=icon, border=0)
        label.image = icon
        label.place(x=450, y=35)

    def bottom_frame(self):
        bottom_frame = Treeview(columns=(0, 0))
        bottom_frame.place(x=25, y=170, width=550, height=250)
        bottom_frame.heading('#0', text='Nome', anchor=W)
        bottom_frame.heading('#1', text='Email', anchor=W)
        bottom_frame.heading('#2', text='Número', anchor=W)
        TButton(self.root, text='Modificar contato').place(x=175, y=450, anchor=CENTER, width=200)
        TButton(self.root, text='Deletar contato').place(x=425, y=450, anchor=CENTER, width=200)
