import tkinter as tk

class HoverElement:
    def __init__(self, root):
        self.root = root
        self.root.title("Hover Effect")

        self.label = tk.Label(
            root,
            text="Hover over me!",
            bg="blue",
            fg="white",
            font=("Arial", 14),
            width=20,
            height=5
        )
        self.label.pack(expand=True, padx=20, pady=20)

        self.label.bind("<Enter>", self.on_enter)
        self.label.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        self.label.config(bg="red", fg="white")

    def on_leave(self, event):
        self.label.config(bg="blue", fg="white")

if __name__ == "__main__":
    root = tk.Tk()
    app = HoverElement(root)
    root.mainloop()

