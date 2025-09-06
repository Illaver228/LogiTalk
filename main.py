from customtkinter import*

class Mainwindow(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.title("LogicTalk")

        self.frame = CTkFrame(self, width=200, height=self.winfo_height())
        self.frame.pack_propagate(False)
        self.frame.configure(width=0)
        self.frame.place(x=0, y=0)
        self.is_show_menu = False
        self.width_frame = 0

        self.label = CTkLabel(self.frame, text="Ваше ім'я")
        self.label.pack(pady=40)

        self.entry = CTkEntry(self.frame)
        self.entry.pack()

        self.theme = CTkOptionMenu(self.frame, values=['dark', 'light'])
        self.theme.pack(side="bottom", pady=20)

        self.button = CTkButton(self, text="→", width=30, command=self.show_menu)
        self.button.place(x=0, y=0)


        self.field = CTkScrollableFrame(self, width=380)
        self.field.place(x=0, y=30)

        self.messege = CTkEntry(self, placeholder_text="Введіть повідомлення", height=40, width=360)
        self.messege.place(x=0, y=260)

        self.send = CTkButton(self, text="→", height=40, width=40)
        self.send.place(x=360, y=260)

    def show_menu(self):
        if self.is_show_menu:
            self.is_show_menu = False
            self.frame.pack_propagate(False)
            self.button.configure(text="→")
        else:
            self.is_show_menu = True
            self.frame.pack_propagate(True)
            self.button.configure(text="←")

    def adaptation_ui(self):
        








    # def change_theme(self, value):
    #     if value == "dark":
    #         set_appearance_mode = "dark"
    #     else:
    #         set_appearance_mode = "light"
        


window = Mainwindow()
window.mainloop()
