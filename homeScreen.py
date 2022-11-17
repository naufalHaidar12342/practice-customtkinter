import customtkinter


class HomeScreen(customtkinter.CTk):
    def __init__(self,):
        super().__init__()

        self.title("Chatbot Mengajar")

        # set window to fullscreen immediately at launched
        self.state("zoomed")


if __name__ == "__main__":
    home_screen = HomeScreen()
    home_screen.mainloop()
