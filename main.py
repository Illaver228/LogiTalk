from customtkinter import*
import socket
import threading
class Mainwindow(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.title("LogicTalk")


        self.frame = CTkFrame(self, width=200, height=260, corner_radius=15)
        self.frame.pack_propagate(False)
        self.frame.place(x=0, y=0)
        self.is_show_menu = False

        self.label = CTkLabel(self.frame, text="Ваше ім'я")
        self.label.pack(pady=40)

        self.entry = CTkEntry(self.frame)
        self.entry.pack()

        self.theme = CTkOptionMenu(self.frame, values=['dark', 'light'], command=self.change_theme)
        self.theme.pack(side="bottom", pady=20)

        self.field = CTkTextbox(self, width=400, height=260, corner_radius=10)
        self.field.place(x=0, y=0)

        self.button = CTkButton(self, text="→", width=30, command=self.show_menu)
        self.button.place(x=0, y=0)



        self.messege = CTkEntry(self, placeholder_text="Введіть повідомлення", height=40, width=360)
        self.messege.place(x=0, y=260)

        self.send = CTkButton(self, text="→", height=40, width=40)
        self.send.place(x=360, y=260)

    def show_menu(self):
        if self.is_show_menu:
            self.is_show_menu = False
            self.field.configure(width=0)
            self.field.configure(widht=400)
            self.field.place(x=0, y=0)
            self.button.configure(text="→")
        else:
            self.is_show_menu = True
            self.field.configure(width=200)
            self.field.configure(width=200)
            self.field.place(x=200, y=0)
            self.button.configure(text="←")


        
    def change_theme(self, value):
        if value == "dark":
            set_appearance_mode = "dark"
        else:
            set_appearance_mode = "light"

    def change_theme(self, value):
        set_appearance_mode(value)


    # додати повідомлення
    def add_message(self, text):
        self.field.configure(state='normal')
        self.field.insetr(END, f"Я:" {text} \n)
        self.field.configure(state="desadle")
        
    # надіслати повідомлення
        
    # отримати повідомлення


        


window = Mainwindow()
window.mainloop()
