import tkinter
from components.status_box import StatusTextBox
from conf.static import StaticValues, Messages
from lib.component_lib import Others


class AnswerTextBox:
    __output: tkinter.Text = None
    __answer: str = None

    @staticmethod
    def init(root: tkinter.Tk):
        AnswerTextBox.__output = tkinter.Text(root, width=77, height=26, font=('Arial', 12),
                                              wrap=tkinter.WORD, state=tkinter.DISABLED)
        AnswerTextBox.__output.grid(row=4, column=0, columnspan=4, padx=10, pady=4, sticky='w')
        AnswerTextBox.write_response('', StaticValues.DEFAULT_ANSWER)
        Others.set_padding(AnswerTextBox.__output, 5, 5)
        print(Messages.COMP_INIT_DONE.format(AnswerTextBox.__name__))

    @staticmethod
    def write_response(prefix: str, text: str) -> None:
        AnswerTextBox.__answer = text
        AnswerTextBox.__output.config(state=tkinter.NORMAL)
        AnswerTextBox.__output.delete(1.0, tkinter.END)
        AnswerTextBox.__output.insert(tkinter.END, prefix + text)
        AnswerTextBox.__output.config(state=tkinter.DISABLED)
        AnswerTextBox.__output.update()

    @staticmethod
    def answer_to_clipboard(event=None):
        n_tk = tkinter.Tk()
        n_tk.clipboard_clear()
        n_tk.clipboard_append(AnswerTextBox.__answer)
        n_tk.destroy()
        StatusTextBox.write_response(Messages.COPY_TO_CLIPBOARD)
