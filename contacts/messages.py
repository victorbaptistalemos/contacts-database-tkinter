from tkinter.messagebox import askokcancel, showerror, showinfo


class Messages:
    @classmethod
    def try_action(cls, title: str, message: str) -> bool:
        return askokcancel(title, message)

    @classmethod
    def show_error(cls, title: str, message: str) -> str:
        return showerror(title, message)

    @classmethod
    def show_info(cls, title: str, message: str) -> str:
        return showinfo(title, message)
