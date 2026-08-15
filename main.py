import customtkinter as ctk

from cards_frame.app import App


def main():
    ctk.set_widget_scaling(1.20)
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
