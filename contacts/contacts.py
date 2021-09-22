from contacts.database import Database
from contacts.messages import Messages
from tkinter import CENTER, E, END, Label, PhotoImage, Tk, W
from tkinter.ttk import Button as TButton
from tkinter.ttk import Entry as TEntry
from tkinter.ttk import Label as TLabel
from tkinter.ttk import LabelFrame as TLabelFrame
from tkinter.ttk import Scrollbar, Style, Treeview


class Contacts:
    def __init__(self, root: Tk) -> None:
        self.top = None
        self.t_name = None
        self.t_email = None
        self.t_number = None
        self.t_view = None
        self.root: Tk = root
        self.gui()

    def gui(self) -> None:
        """self.__init__() calls self.gui()"""
        self.root.configure(bg='black')
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
        self.top_frame()
        self.contacts_icon()
        self.bottom_frame()
        self.view()

    def top_frame(self) -> None:
        """self.gui() calls self.top_frame()"""
        top_frame: TLabelFrame = TLabelFrame(self.root, text='Criar novo contato', labelanchor='n')
        top_frame.place(x=20, y=10, width=400, height=150)
        TLabel(top_frame, text='Nome:').place(x=75, y=10, anchor=E)
        TLabel(top_frame, text='Email:').place(x=75, y=35, anchor=E)
        TLabel(top_frame, text='Número:').place(x=75, y=60, anchor=E)
        self.t_name: TEntry = TEntry(top_frame)
        self.t_email: TEntry = TEntry(top_frame)
        self.t_number: TEntry = TEntry(top_frame)
        self.t_name.place(x=76, y=10, anchor=W, width=299)
        self.t_email.place(x=76, y=35, anchor=W, width=299)
        self.t_number.place(x=76, y=60, anchor=W, width=299)
        self.t_name.bind('<Key-Return>', lambda _: self.add())
        self.t_email.bind('<Key-Return>', lambda _: self.add())
        self.t_number.bind('<Key-Return>', lambda _: self.add())
        self.t_name.bind('<KP_Enter>', lambda _: self.add())
        self.t_email.bind('<KP_Enter>', lambda _: self.add())
        self.t_number.bind('<KP_Enter>', lambda _: self.add())
        TButton(top_frame, text='Adicionar contato', command=self.add)\
            .place(x=200, y=100, anchor=CENTER, width=200)

    def add(self) -> None:
        """self.top_frame() calls self.add()"""
        if self.check_add():
            add = (self.t_name.get(), self.t_email.get(), int(self.t_number.get()))
            Database.execute(Database.add(), add)
            self.t_name.delete(0, END)
            self.t_email.delete(0, END)
            self.t_number.delete(0, END)
            Messages.show_info(
                'Contato adicionado!',
                f'{add[0]} foi adicionado(a) aos contatos!'
            )
            self.view()

    def check_add(self) -> bool:
        """self.add() calls self.check_add()"""
        t_name = self.t_name.get()
        t_email = self.t_email.get()
        t_number = self.t_number.get()
        names: tuple = self.t_view.get_children()
        names: list = [self.t_view.item(_)['text'] for _ in names]
        if len(t_name) == 0 and len(t_email) == 0 and len(t_number) < 10:
            Messages.show_error(
                'Algo de errado não está certo!',
                'Algo de errado não está certo!'
            )
            return False
        elif t_name in names:
            Messages.show_error(
                'Verifique sua lista de contatos!',
                f'{t_name} já está na sua lista de contatos.')
            return False
        elif '@' not in t_email or '.com' not in t_email:
            Messages.show_error(
                'Email inválido!',
                '@ e .com são necessários para validar o email.'
            )
            return False
        elif len(t_number) < 10:
            Messages.show_error(
                'Telefone inválido',
                'Exemplo de número: 27912345678'
            )
        else:
            return True

    @staticmethod
    def contacts_icon() -> None:
        """self.gui() calls self.contacts_icon"""
        icon: PhotoImage = PhotoImage(file='contacts/.contacts.gif')
        label: TLabel = TLabel(image=icon, border=0)
        label.image = icon
        label.place(x=455, y=35)

    def bottom_frame(self) -> None:
        """self.gui() calls self.bottom_frame()"""
        self.t_view = Treeview(columns=(0, 0))
        self.t_view.place(x=20, y=170, width=550, height=250)
        self.t_view.heading('#0', text='Nome', anchor=W)
        self.t_view.heading('#1', text='Email', anchor=W)
        self.t_view.heading('#2', text='Número', anchor=W)
        Scrollbar(orient='vertical', command=self.t_view.yview).place(x=570, y=170, height=250, width=15)
        Scrollbar(orient='horizontal', command=self.t_view.xview).place(x=20, y=420, height=15, width=550)
        Label(self.root, background='violet').place(x=570, y=420, height=15, width=15)
        TButton(self.root, text='Modificar contato').place(x=175, y=465, anchor=CENTER, width=200)
        TButton(self.root, text='Deletar contato', command=self.delete)\
            .place(x=420, y=465, anchor=CENTER, width=200)

    def delete(self) -> None:
        """self.bottom_frame() calls self.delete()"""
        name = self.t_view.item(self.t_view.selection())['text']
        if name == '':
            Messages.show_error(
                'Nenhum contato selecionado!',
                'Selecione um contato antes de continuar.'
            )
        elif Messages.try_action('Confirma ação?', f'Deseja deletar {name} dos contatos?'):
            if Database.execute(Database.delete(), (name,)):
                Messages.show_info(
                    'Contato excluído!',
                    f'{name} foi removido(a) dos contatos.'
                )
                self.view()
            else:
                Messages.show_error(
                    'Algo de errado não está certo!',
                    'Erro de SQL, verifique!'
                )

    def view(self) -> None:
        """self.gui(), self.add() and self.delete() call self.view()"""
        for _ in self.t_view.get_children():
            self.t_view.delete(_)
        for _ in Database.list():
            self.t_view.insert('', 0, text=_[0], values=(_[1], _[2]))
