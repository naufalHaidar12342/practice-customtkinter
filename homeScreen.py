import customtkinter


class HomeScreen(customtkinter.CTk):
    def __init__(self,):
        super().__init__()

        self.title("Home screen")
        self.geometry("1920x1080")


if __name__ == "__main__":
    home_screen = HomeScreen()
    home_screen.mainloop()
