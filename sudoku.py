import tkinter as tk
from tkinter import messagebox


sudoku_board = [
    [1, 0, 3, 0, 5],
    [0, 0, 0, 4, 0],
    [4, 5, 0, 0, 3],
    [0, 3, 0, 0, 1],
    [2, 0, 5, 0, 4]
]


solution_board = [
    [1, 4, 3, 2, 5],
    [5, 2, 1, 4, 3],
    [4, 5, 2, 1, 3],
    [3, 3, 5, 3, 1],
    [2, 1, 5, 3, 4]
]

# Tkinter arayüzü için ana pencere
root = tk.Tk()
root.title("5x5 Sudoku")

entries = []

# Sudoku tahtası oluşturma
for i in range(5):
    row_entries = []
    for j in range(5):
        if sudoku_board[i][j] == 0:  # Eğer hücre boşsa, kullanıcı giriş yapabilir
            entry = tk.Entry(root, width=3, font=("Arial", 18), justify='center')
        else:
            entry = tk.Entry(root, width=3, font=("Arial", 18), justify='center', fg='black')
            entry.insert(0, sudoku_board[i][j])  # Başlangıçtaki sayıyı yerleştir
            entry.config(state='disabled')  # Bu hücreler düzenlenemez
        entry.grid(row=i, column=j, padx=5, pady=5)
        row_entries.append(entry)
    entries.append(row_entries)

# Sudoku çözümünü kontrol etme fonksiyonu
def check_sudoku():
    for i in range(5):
        for j in range(5):
            if sudoku_board[i][j] == 0:  # Sadece kullanıcı girişlerini kontrol et
                try:
                    user_value = int(entries[i][j].get())
                except ValueError:
                    messagebox.showerror("Hata", "Geçersiz giriş! Lütfen 1 ile 5 arasında bir sayı girin.")
                    return
                
                if user_value != solution_board[i][j]:
                    messagebox.showinfo("Sonuç", "Hatalı giriş. Lütfen tekrar deneyin!")
                    return

    messagebox.showinfo("Tebrikler!", "Tüm sayılar doğru! Sudoku'yu çözdünüz.")

# Kontrol butonu
check_button = tk.Button(root, text="Kontrol Et", font=("Arial", 14), command=check_sudoku)
check_button.grid(row=5, column=0, columnspan=5, pady=10)

root.mainloop()
