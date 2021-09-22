from tkinter import Button, E, Entry, Label, LabelFrame, PhotoImage, Tk, W


class Contacts:
    # __database = '.contacts.s3db'

    def __init__(self, root: Tk) -> None:
        self.root: Tk = root
        self.gui()

    def gui(self) -> None:
        self.root.configure(bg='black')
        self.top_frame()
        self.contacts_icon()

    def top_frame(self):
        main_frame = LabelFrame(
            self.root,
            text='Criar novo contato',
            background='black',
            foreground='violet',
            font='TimesNewRoman 14',
            labelanchor='n',
            bd=1
        )
        main_frame.place(x=25, y=25, width=400, height=150)
        Label(
            main_frame,
            text='Nome:',
            background='black',
            foreground='violet',
            font='TimesNewRoman 14'
        ).place(x=75, y=10, anchor=E)
        Label(
            main_frame,
            text='Email:',
            background='black',
            foreground='violet',
            font='TimesNewRoman 14'
        ).place(x=75, y=35, anchor=E)
        Label(
            main_frame,
            text='Número:',
            background='black',
            foreground='violet',
            font='TimesNewRoman 14'
        ).place(x=75, y=60, anchor=E)
        Entry(main_frame).place(x=76, y=10, anchor=W, width=299)
        Entry(main_frame).place(x=76, y=35, anchor=W, width=299)
        Entry(main_frame).place(x=76, y=60, anchor=W, width=299)
        Button(
            main_frame,
            text='Adicionar contato',
            background='violet',
            foreground='black',
            font='TimesNewRoman 14'
        ).place(x=200, y=100, anchor='center', width=200)

    @staticmethod
    def contacts_icon() -> None:
        icon: PhotoImage = PhotoImage(file='contacts/.contacts.gif')
        label: Label = Label(image=icon, border=0)
        label.image = icon
        label.place(x=475, y=50)
