import tkinter
from conf.static import StaticValues, Messages
from lib.component_lib import Others


class StatusTextBox:
    __output: tkinter.Text = None
    __answer: str = None

    @staticmethod
    def init(root: tkinter.Tk):
        StatusTextBox.__output = tkinter.Text(root, height=1, width=32, font=('Corbal', 12),
                                              wrap=tkinter.WORD, state=tkinter.DISABLED)
        StatusTextBox.__output.grid(row=5, column=0, columnspan=1, padx=10, pady=4, sticky='w')
        StatusTextBox.write_response(Messages.APP_STARTED)
        Others.set_padding(StatusTextBox.__output, 5, 5)
        print(Messages.COMP_INIT_DONE.format(StatusTextBox.__name__))

    @staticmethod
    def write_response(text: str) -> None:
        StatusTextBox.__answer = text
        StatusTextBox.__output.config(state=tkinter.NORMAL)
        StatusTextBox.__output.delete(1.0, tkinter.END)
        StatusTextBox.__output.insert(tkinter.END, StaticValues.STATUS_PREFIX + text)
        StatusTextBox.__output.config(state=tkinter.DISABLED)
        StatusTextBox.__output.update()
