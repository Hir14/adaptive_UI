import tkinter as tk
from tkinter import messagebox

class AdaptiveUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Adaptive UI - Light/Dark Mode")
        self.root.geometry("500x350")
        self.click_count = 0
        self.current_mode = "Light"

        # Main container frame
        self.frame = tk.Frame(root)
        self.frame.pack(fill="both", expand=True)

        # Title Label
        self.title_label = tk.Label(self.frame, text="Adaptive User Interface", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=15)

        # Status Label
        self.status_label = tk.Label(self.frame, text="Current Mode: Light", font=("Helvetica", 12))
        self.status_label.pack(pady=5)

        # Light Mode Button
        self.light_btn = tk.Button(self.frame, text="Light Mode", width=25, command=self.set_light_mode)
        self.light_btn.pack(pady=5)

        # Dark Mode Button
        self.dark_btn = tk.Button(self.frame, text="Dark Mode", width=25, command=self.set_dark_mode)
        self.dark_btn.pack(pady=5)

        # Click Me Button
        self.click_btn = tk.Button(self.frame, text="Click Me!", width=25, command=self.track_clicks)
        self.click_btn.pack(pady=20)

        self.widgets = [self.title_label, self.status_label, self.light_btn, self.dark_btn, self.click_btn]

        self.set_light_mode()  # Start in Light Mode

    def set_light_mode(self):
        self.current_mode = "Light"
        self.status_label.config(text="Current Mode: Light")
        self.apply_theme(bg="white", fg="black", btn_bg="#e0e0e0", btn_fg="black")

    def set_dark_mode(self):
        self.current_mode = "Dark"
        self.status_label.config(text="Current Mode: Dark")
        self.apply_theme(bg="#121212", fg="white", btn_bg="#444444", btn_fg="white")

    def apply_theme(self, bg, fg, btn_bg, btn_fg):
        self.root.config(bg=bg)
        self.frame.config(bg=bg)

        for widget in self.widgets:
            if isinstance(widget, tk.Label):
                widget.config(bg=bg, fg=fg)
            elif isinstance(widget, tk.Button):
                widget.config(
                    bg=btn_bg,
                    fg=btn_fg,
                    activebackground=bg,
                    activeforeground=fg,
                    highlightbackground=bg
                )

    def track_clicks(self):
        self.click_count += 1
        if self.click_count == 5:
            messagebox.showinfo("Adaptive Response", "You've clicked 5 times. Switching to Dark Mode!")
            self.set_dark_mode()

# Run the UI
if __name__ == "__main__":
    root = tk.Tk()
    app = AdaptiveUI(root)
    root.mainloop()
