import os
import shutil
from glob import glob
from tqdm import tqdm  


FILE_CATEGORIES = {
    'images': ['.png', '.jpg', '.jpeg', '.gif', '.bmp'],
    'videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'documents': ['.pdf', '.docx', '.txt'],
    
}

def scan_files(directory):
    """Belirtilen dizindeki dosyaları tarar ve türlerine göre gruplar."""
    files_by_type = {category: [] for category in FILE_CATEGORIES}
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_ext = os.path.splitext(file)[1].lower()
            for category, extensions in FILE_CATEGORIES.items():
                if file_ext in extensions:
                    files_by_type[category].append(os.path.join(root, file))
    return files_by_type

def organize_files(directory, files_by_type):
    """Dosyaları kategorilere ayırıp ilgili klasörlere taşır."""
    for category, files in files_by_type.items():
        category_dir = os.path.join(directory, category)
        if not os.path.exists(category_dir):
            os.makedirs(category_dir)
        
        print(f"{category} kategorisindeki dosyalar taşınıyor...")

        
        for file in tqdm(files, desc=f"{category.capitalize()} dosyaları taşınıyor", unit="file"):
            try:
                shutil.move(file, category_dir)
            except Exception as e:
                print(f'Dosya taşınamadı: {file}, Hata: {e}')

def search_files(directory, query):
    """Belirtilen dizinde dosya adı veya uzantısına göre arama yapar."""
    result = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if query.lower() in file.lower():
                result.append(os.path.join(root, file))
    return result

def menu():
    print("Dosya Yöneticisi")
    print("1. Dosyaları organize et (resimler, videolar, belgeler)")
    print("2. Dosya ara")
    print("3. Çıkış")
    
    choice = input("Seçiminizi yapın (1/2/3): ")
    return choice

def main():
    directory = input("Lütfen taranacak dizini belirtin: ")

    while True:
        choice = menu()

        if choice == '1':
            
            files_by_type = scan_files(directory)
            organize_files(directory, files_by_type)

        elif choice == '2':
            
            query = input("Aranacak dosya adı veya uzantısı: ")
            results = search_files(directory, query)
            if results:
                print("Bulunan dosyalar:")
                for result in results:
                    print(result)
            else:
                print("Eşleşen dosya bulunamadı.")
        
        elif choice == '3':
            print("Çıkış yapılıyor.")
            break

        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
