import customtkinter
import tkinter


class InfoFrame(customtkinter.CTkFrame):
    def __init__(self):
        super().__init__()
        self.frame_home = customtkinter.CTkFrame(self)
        self.frame_home.grid(
            row=0,
            column=0,
            columnspan=1,
            rowspan=7,
            pady=20,
            padx=20,
            sticky="nsew"
        )
        self.frame_home.rowconfigure(0, weight=1)
        self.frame_home.columnconfigure(0, weight=1)
        self.label_info = customtkinter.CTkLabel(
            self.frame_home,
            text="Selamat datang di Chatbot Dinas Penanaman Modal dan Pelayanan Terpadu Satu Pintu Kota Semarang." +
            "\n Silahkan klik tombol di bawah untuk mulai berinteraksi",
            height=200,
            corner_radius=10,
            fg_color=("grey"),
            text_font=("", 20),
            justify=tkinter.CENTER
        )
        self.label_info.grid(column=0, row=0, sticky="nwe", padx=20, pady=20)
