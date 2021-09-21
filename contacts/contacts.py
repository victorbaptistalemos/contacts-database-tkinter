from tkinter import Tk


class Contacts:
    __database = 'contacts.s3db'

    def __init__(self, root: Tk) -> None:
        self.root: Tk = root
