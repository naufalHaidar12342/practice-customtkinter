import customtkinter
import tkinter


class HomeScreen(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.set_appearance_mode("system")
        self.title("Chatbot")

        # set window to fullscreen immediately at launched
        self.state("zoomed")

        # header
        self.header_section = customtkinter.CTkFrame(self)
        self.header_section.pack(padx=10, pady=10)

        self.header_text = customtkinter.CTkLabel(
            self.header_section,
            width=200,
            height=200,
            text_font=("", 20),
            text="Selamat datang di Chatbot Dinas Penanaman Modal dan Pelayanan Terpadu Satu Pintu Kota Semarang." +
            "\n Silahkan klik tombol di bawah untuk mulai berinteraksi",
        )
        self.header_text.pack(padx=10, pady=10)

        # button section
        self.button_section = customtkinter.CTkFrame(
            self).pack(padx=20, pady=20)
        self.button = customtkinter.CTkButton(
            self.button_section, text="Click here").pack(padx=20, pady=20)


if __name__ == "__main__":
    home_screen = HomeScreen()
    home_screen.mainloop()
