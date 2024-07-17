import tkinter as tk
from tkinter import ttk, messagebox
import itertools
import threading
import time

class BruteForceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Şifre Kırma - Rimes Yazılım")
        self.root.geometry("600x400")
        self.root.configure(bg="#2E2E2E")

        self.create_widgets()

    def create_widgets(self):
        # Şifre uzunluğu girişi
        self.length_label = ttk.Label(self.root, text="Şifre Uzunluğu:", background="#2E2E2E", foreground="#FFFFFF")
        self.length_label.pack(pady=10)
        self.length_entry = ttk.Entry(self.root, width=10)
        self.length_entry.pack(pady=5)

        # Karakter kümesi girişi
        self.charset_label = ttk.Label(self.root, text="Karakter Kümesi:", background="#2E2E2E", foreground="#FFFFFF")
        self.charset_label.pack(pady=10)
        self.charset_entry = ttk.Entry(self.root, width=50)
        self.charset_entry.pack(pady=5)

        # Gerçek şifre girişi (test için)
        self.password_label = ttk.Label(self.root, text="Gerçek Şifre:", background="#2E2E2E", foreground="#FFFFFF")
        self.password_label.pack(pady=10)
        self.password_entry = ttk.Entry(self.root, width=50, show='*')
        self.password_entry.pack(pady=5)

        # Taramayı başlat butonu
        self.start_button = ttk.Button(self.root, text="Kırmayı Başlat", command=self.start_brute_force)
        self.start_button.pack(pady=20)

        # Sonuçları gösteren liste kutusu
        self.result_label = ttk.Label(self.root, text="Sonuçlar:", background="#2E2E2E", foreground="#FFFFFF")
        self.result_label.pack(pady=10)
        self.result_listbox = tk.Listbox(self.root, width=60, height=10, bg="#1E1E1E", fg="#FFFFFF")
        self.result_listbox.pack(pady=10)

    def start_brute_force(self):
        self.result_listbox.delete(0, tk.END)
        try:
            length = int(self.length_entry.get())
        except ValueError:
            messagebox.showerror("Hata", "Geçerli bir şifre uzunluğu girin.")
            return

        charset = self.charset_entry.get()
        if not charset:
            messagebox.showerror("Hata", "Geçerli bir karakter kümesi girin.")
            return

        password = self.password_entry.get()
        if not password:
            messagebox.showerror("Hata", "Gerçek şifreyi girin.")
            return

        self.thread = threading.Thread(target=self.brute_force, args=(length, charset, password))
        self.thread.start()

    def brute_force(self, length, charset, password):
        start_time = time.time()
        for guess in itertools.product(charset, repeat=length):
            guess = ''.join(guess)
            self.result_listbox.insert(tk.END, guess)
            self.result_listbox.yview(tk.END)
            if guess == password:
                end_time = time.time()
                duration = end_time - start_time
                self.result_listbox.insert(tk.END, f"Şifre bulundu: {guess}")
                self.result_listbox.insert(tk.END, f"Kırma süresi: {duration:.2f} saniye")
                return

        self.result_listbox.insert(tk.END, "Şifre bulunamadı")

if __name__ == "__main__":
    root = tk.Tk()
    app = BruteForceApp(root)
    root.mainloop()
