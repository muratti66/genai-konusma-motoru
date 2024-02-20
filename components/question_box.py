import tkinter
from conf.static import StaticValues, Messages
from lib.component_lib import Others


class QuestionTextBox:
    __entry: tkinter.Text = None

    @staticmethod
    def init(root: tkinter.Tk) -> None:
        QuestionTextBox.__entry = tkinter.Text(root, height=10, width=54, font=('Arial', 13))
        QuestionTextBox.__entry.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
        QuestionTextBox.__entry.insert(tkinter.END, StaticValues.DEFAULT_QUESTION)
        Others.set_padding(QuestionTextBox.__entry, 5, 5)
        print(Messages.COMP_INIT_DONE.format(QuestionTextBox.__name__))

    @staticmethod
    def get_question() -> str:
        return QuestionTextBox.__entry.get("1.0", tkinter.END)

    @staticmethod
    def write_response(text: str) -> None:
        QuestionTextBox.__entry.config(state=tkinter.NORMAL)
        QuestionTextBox.__entry.delete(1.0, tkinter.END)
        QuestionTextBox.__entry.insert(tkinter.END, text)
        QuestionTextBox.__entry.config(state=tkinter.DISABLED)
