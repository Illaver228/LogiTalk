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

        self.send = CTkButton(self, text="→", height=40, width=40, command=self.add_message)
        self.send.place(x=360, y=260)
        
        # self.username = "Illa"
        # try: 
        #     self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #     self.client.connect(("0.0.0.0", 8080))
        #     hello = f"{self.username} приєднався до чату! \n"
        #     self.client.send(hello.encode('utf-8'))
        #     threading.Thread(target=self.recv_message, daemon=True).start()
        # except Exception as exp:
        #     self.add_message(f"Не вдалося підключитися до сервера: "{exp})
            


    def show_menu(self):
        if self.is_show_menu:
            self.is_show_menu = False
            self.field.configure(width=0)
            self.field.configure(width=400)
            self.field.place(x=0, y=0)
            self.button.configure(text="→")
        else:
            self.is_show_menu = True
            self.field.configure(width=200)
            self.field.configure(width=200)
            self.field.place(x=200, y=0)
            self.button.configure(text="←")

        
    def change_theme(self, value):
        set_appearance_mode(value)


    # додати повідомлення
    def add_message(self):
        self.field.configure(state='normal')
        text = self.messege.get()
        self.field.insert(END, f"Я:{text} \n")
        self.messege.delete(0, END)
        self.field.configure(state="disable")
        
    # надіслати повідомлення
    # def send_message(self):
    #     get_message = self.message.get()
    #     if get_message:
    #         self.message(f"{self.username}: {get_message}")
    #         data = f"{self.username}: {get_message} \n"
    #         try:
    #             self.client.sendall(data.encode())
    #         except:
    #             pass
    # self.message.delete(0, END)
            

        
    # отримати повідомлення
    # def recv_message(self):
    #     buffer = ""
    #     while True:
    #     try:
    #         word = self.client.recv(4096)
    #         i not word:
    #             break
    #             buffer += word.decode()
    #             while "\n" in buffer:
    #                 line, buffer = buffer,split("\n", 1)
    #     except:
    #         break
    # self.client.close()
        

      


window = Mainwindow()
window.mainloop()
