import tkinter as tk
import random
import time
from tkinter import messagebox

# Test için kullanılacak metinlerden bazıları
texts = [
    "Fırat Üniversitesinde Okuyorum.",
    "Pratik mükemmelleştirir. Daha iyi olmaya çalış.",
   
]

start_time = 0
typed_words = 0

def start_test():
    global start_time, typed_words
    typed_words = 0
    start_time = time.time()  

    random_text = random.choice(texts)  
    label_text.config(text=random_text)  
    entry_text.delete(0, tk.END)  
    entry_text.config(state=tk.NORMAL) 
    result_label.config(text="")  
    entry_text.focus_set()  

def calculate_speed():
    global start_time
    elapsed_time = time.time() - start_time  # Geçen süreyi hesapla
    typed_text = entry_text.get()  # Kullanıcının yazdığı metni al
    typed_words_list = typed_text.split()  # Yazılan kelimeleri listeye ayır
    displayed_text = label_text.cget("text").split()  # Gösterilen metni kelimelere ayır

    # Doğru kelimeleri say
    correct_words = 0
    for i, word in enumerate(typed_words_list):
        if i < len(displayed_text) and word == displayed_text[i]:
            correct_words += 1

    # Kelime başına süreyi dakikaya çevirelim
    time_in_minutes = elapsed_time / 60
    words_per_minute = len(typed_words_list) / time_in_minutes

    # Sonuçları göster
    result_label.config(text=f"Doğru Kelime: {correct_words}\n"
                             f"Toplam Kelime: {len(typed_words_list)}\n"
                             f"Doğruluk: {correct_words / len(typed_words_list) * 100:.2f}%\n"
                             f"Hız: {words_per_minute:.2f} WPM")

def end_test():
    entry_text.config(state=tk.DISABLED)  # Test bitince girişe izin verme
    calculate_speed()  # Sonuçları hesapla

# Tkinter arayüzü oluşturma
root = tk.Tk()
root.title("Hızlı Yazma Testi")

# Metni gösterecek etiket
label_text = tk.Label(root, text="Yazmaya başlamak için 'Başlat' düğmesine basın.", font=("Arial", 14), wraplength=400)
label_text.pack(pady=20)

# Kullanıcının yazacağı metin kutusu
entry_text = tk.Entry(root, width=50, font=("Arial", 12))
entry_text.pack(pady=10)
entry_text.config(state=tk.DISABLED)  # Başlangıçta yazma kutusu kapalı

# Sonuçları gösterecek etiket
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Testi başlatma ve bitirme düğmeleri
start_button = tk.Button(root, text="Başlat", command=start_test, font=("Arial", 12))
start_button.pack(side=tk.LEFT, padx=20)

end_button = tk.Button(root, text="Bitiş", command=end_test, font=("Arial", 12))
end_button.pack(side=tk.RIGHT, padx=20)

# Tkinter penceresini çalıştırma
root.mainloop()
