from contacts.database import Database
from contacts.messages import Messages
from tkinter import CENTER, E, END, Label, PhotoImage, Tk, Toplevel, W
from tkinter.ttk import Button as TButton
from tkinter.ttk import Entry as TEntry
from tkinter.ttk import Label as TLabel
from tkinter.ttk import LabelFrame as TLabelFrame
from tkinter.ttk import Scrollbar, Style, Treeview


class Contacts:
    def __init__(self, root: Tk) -> None:
        self.top: None = None
        self.t_name: None = None
        self.t_email: None = None
        self.t_number: None = None
        self.top_window: None = None
        self.top_name: None = None
        self.top_new_number: None = None
        self.update_new_number: None = None
        self.t_view: None = None
        self.new_window: bool = False
        self.root: Tk = root
        self.gui()

    def gui(self) -> None:
        """self.__init__() calls self.gui()"""
        self.root.configure(bg='black')
        style: Style = Style()
        style.configure('.', font='TimesNewRoman 12', background='black', foreground='violet')
        style.configure('TButton', font='TimesNewRoman 14 bold')
        style.configure('TEntry', foreground='black')
        style.configure('TLabel', font='TimesNewRoman 14')
        style.configure('TLabelframe.Label', font='TimesNewRoman 14 bold')
        style.configure('TScrollbar', background='violet')
        style.configure('Treeview', fieldbackground='black')
        style.configure('Treeview.Heading', font='TimesNewRoman 12 bold')
        style.map(
            'TEntry',
            fieldbackground=[('disabled', 'violet'), ('!disabled', 'violet')],
            foreground=[('disabled', 'purple'), ('!disabled', 'black')],
        )
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
        self.t_name.focus()

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
        TButton(self.root, text='Modificar contato', command=self.update)\
            .place(x=175, y=465, anchor=CENTER, width=200)
        TButton(self.root, text='Deletar contato', command=self.delete)\
            .place(x=420, y=465, anchor=CENTER, width=200)

    def update(self) -> None:
        """self.bottom_frame() calls self.update()"""
        selection: dict = self.t_view.selection()
        name: str = self.t_view.item(selection)['text']
        if name == '':
            Messages.show_error(
                'Nenhum contato selecionado!',
                'Selecione um contato antes de modificá-lo.'
            )
        else:
            email: str = self.t_view.item(selection)['values'][0]
            number: str = self.t_view.item(selection)['values'][1]
            if not self.new_window:
                self.new_window: bool = True
                self.top_level((name, email, number))
            else:
                Messages.show_error(
                    'Erro ao abrir nova tela!',
                    'Você já está editando um contato.'
                )

    def top_level(self, args: tuple) -> None:
        """self.update() calls self.top_level()"""
        self.top_window = Toplevel()
        self.top_window.title('Atualização de contato:')
        self.top_window.geometry('400x150+550+200')
        self.top_window.configure(background='black')
        TLabel(self.top_window, text='Nome:').place(x=125, y=15, anchor=E)
        TLabel(self.top_window, text='Email:').place(x=125, y=40, anchor=E)
        TLabel(self.top_window, text='Número antigo:').place(x=125, y=65, anchor=E)
        TLabel(self.top_window, text='Número novo:').place(x=125, y=90, anchor=E)
        self.top_name: TEntry = TEntry(self.top_window)
        self.top_name.insert(0, args[0])
        self.top_name.configure(state='disabled')
        self.top_name.place(x=126, y=5, width=254)
        top_email: TEntry = TEntry(self.top_window)
        top_email.insert(0, args[1])
        top_email.configure(state='disabled')
        top_email.place(x=126, y=30, width=254)
        top_old_number: TEntry = TEntry(self.top_window)
        top_old_number.insert(0, args[2])
        top_old_number.configure(state='disabled')
        top_old_number.place(x=126, y=55, width=254)
        self.top_new_number: TEntry = TEntry(self.top_window)
        self.top_new_number.place(x=126, y=80, width=254)
        self.top_new_number.bind('<Key-Return>', lambda _: self.update_contact())
        self.top_new_number.bind('<KP_Enter>', lambda _: self.update_contact())
        self.top_new_number.focus()
        TButton(self.top_window, text='Atualizar', command=self.update_contact)\
            .place(x=100, y=125, width=150, anchor=CENTER)
        TButton(self.top_window, text='Cancelar', command=self.cancel_update)\
            .place(x=300, y=125, width=150, anchor=CENTER)

    def update_contact(self) -> None:
        """self.top_level() calls self.update_contact()"""
        if self.check_update():
            Database.execute(
                Database.update(),
                (int(self.top_new_number.get()), self.top_name.get())
            )
            Messages.show_info('Sucesso!', 'Contato atualizado!')
            self.cancel_update()
            self.view()
        else:
            Messages.show_error('Algo de errado não está certo!', 'Número inválido!')

    def check_update(self) -> bool:
        """self.update_contact() calls self.check_update()"""
        return len(self.top_new_number.get()) >= 10

    def cancel_update(self) -> None:
        """self.update_contact() calls self.cancel_update()"""
        self.top_window.destroy()
        self.new_window: bool = False
        self.top_window: None = None

    def delete(self) -> None:
        """self.bottom_frame() calls self.delete()"""
        name = self.t_view.item(self.t_view.selection())['text']
        if name == '':
            Messages.show_error(
                'Nenhum contato selecionado!',
                'Selecione um contato antes de deletá-lo.'
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
        """self.gui(), self.add(), self.update() and self.delete() call self.view()"""
        for _ in self.t_view.get_children():
            self.t_view.delete(_)
        for _ in Database.list():
            self.t_view.insert('', 0, text=_[0], values=(_[1], _[2]))
