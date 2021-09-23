from contacts.contacts import Contacts
from tkinter import PhotoImage, Tk

root = Tk(className="Minha Agenda de Contatos")
root.tk.call('wm', 'iconphoto', root.__getattribute__('_w'), PhotoImage(file='./contacts/.logo.gif'))
root.title('Minha Agenda de Contatos')
root.geometry("600x500+450+200")
root.resizable(False, False)
app = Contacts(root)
root.mainloop()
