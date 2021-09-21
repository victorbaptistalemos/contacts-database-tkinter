from contacts.contacts import Contacts
from tkinter import Tk

root = Tk()
root.title('Minha Agenda de Contatos')
root.geometry("600x500+450+200")
root.resizable(False, False)
app = Contacts(root)
root.mainloop()
