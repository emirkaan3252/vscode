import speech_recognition as sr
import os
import platform
import subprocess

def ses_tanima():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Lütfen bir komut verin...")
        audio = recognizer.listen(source)

        try:
            komut = recognizer.recognize_google(audio, language='tr-TR')
            print(f"Algılanan komut: {komut}")

           
            if "merhaba" in komut.lower():
                print("Merhaba! Size nasıl yardımcı olabilirim?")
            elif "dur" in komut.lower():
                print("Ses tanıma durduruluyor...")
                return False  
            elif "discord'u kapat" in komut.lower():
                print("Discord kapatılıyor...")
                kapat_discord()
            elif "discord'u aç" in komut.lower():
                print("Discord açılıyor...")
                ac_discord()
            elif "google chromeyi aç" in komut.lower():
                print("Google Chrome açılıyor...")
                ac_google_chrome()
            else:
                print("Tanımadım, lütfen başka bir komut verin.")

        except sr.UnknownValueError:
            print("Üzgünüm, sesinizi anlayamadım.")
        except sr.RequestError as e:
            print(f"Ses tanıma servisine erişim hatası: {e}")
    
    return True  

def kapat_discord():
    
    os.system("taskkill /F /IM Discord.exe")

def ac_discord():
    
    discord_path = r"C:\Users\msi-nb\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord.lnk"
    if platform.system() == "Windows":
        subprocess.Popen([discord_path], shell=True)
    else:
        print("Desteklenmeyen işletim sistemi.")

def ac_google_chrome():
    
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  
    if platform.system() == "Windows":
        subprocess.Popen([chrome_path])
    else:
        print("Desteklenmeyen işletim sistemi.")

if __name__ == "__main__":
    while True:
        if not ses_tanima():
            break 
