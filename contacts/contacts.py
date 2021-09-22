from contacts.database import Database
from tkinter import CENTER, E, Label, PhotoImage, Tk, W
from tkinter.ttk import Button as TButton
from tkinter.ttk import Entry as TEntry
from tkinter.ttk import Label as TLabel
from tkinter.ttk import LabelFrame as TLabelFrame
from tkinter.ttk import Scrollbar, Style, Treeview


class Contacts:
    def __init__(self, root: Tk) -> None:
        self.t_view = None
        self.root: Tk = root
        style: Style = Style()
        style.configure('.', font='TimesNewRoman 12', background='black', foreground='violet')
        style.configure('TButton', font='TimesNewRoman 14 bold')
        style.configure('TEntry', fieldbackground='violet', foreground='black')
        style.configure('TLabel', font='TimesNewRoman 14')
        style.configure('TLabelframe.Label', font='TimesNewRoman 14 bold')
        style.configure('TScrollbar', background='violet')
        style.configure('Treeview', fieldbackground='black')
        style.configure('Treeview.Heading', font='TimesNewRoman 12 bold')
        style.map(
            'TButton',
            background=[('active', 'purple'), ('!active', 'violet')],
            foreground=[('active', 'black'), ('!active', 'black')])
        style.map(
            'Treeview',
            foreground=[('selected', 'black'), ('!selected', 'violet')],
            background=[('selected', 'violet'), ('!selected', 'black')],
        )
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
        self.view()

    def top_frame(self) -> None:
        top_frame = TLabelFrame(self.root, text='Criar novo contato', labelanchor='n')
        top_frame.place(x=20, y=10, width=400, height=150)
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
        label: TLabel = TLabel(image=icon, border=0)
        label.image = icon
        label.place(x=455, y=35)

    def bottom_frame(self):
        self.t_view = Treeview(columns=(0, 0))
        self.t_view.place(x=20, y=170, width=550, height=250)
        self.t_view.heading('#0', text='Nome', anchor=W)
        self.t_view.heading('#1', text='Email', anchor=W)
        self.t_view.heading('#2', text='Número', anchor=W)
        Scrollbar(orient='vertical', command=self.t_view.yview).place(x=570, y=170, height=250, width=15)
        Scrollbar(orient='horizontal', command=self.t_view.xview).place(x=20, y=420, height=15, width=550)
        Label(self.root, background='violet').place(x=570, y=420, height=15, width=15)
        TButton(self.root, text='Modificar contato').place(x=175, y=465, anchor=CENTER, width=200)
        TButton(self.root, text='Deletar contato').place(x=420, y=465, anchor=CENTER, width=200)

    def view(self):
        for _ in self.t_view.get_children():
            self.t_view.delete(_)
        contacts: list = Database.list()
        for contact in contacts:
            self.t_view.insert('', 0, text=contact[0], values=(contact[1], contact[2]))
