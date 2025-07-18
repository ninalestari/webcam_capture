import os
from ftplib import FTP
from dotenv import load_dotenv

load_dotenv()

FTP_HOST = os.getenv("FTP_HOST")
FTP_USER = os.getenv("FTP_USER")
FTP_PASS = os.getenv("FTP_PASS")
FTP_PATH = os.getenv("FTP_PATH")

def upload_to_ftp(filename):
    try:
        ftp = FTP(FTP_HOST)
        ftp.login(FTP_USER, FTP_PASS)
        with open(filename, "rb") as file:
            ftp.storbinary(f"STOR {FTP_PATH}/{filename}", file)
        print(f"📤 Upload ke FTP sukses: {filename}")
        ftp.quit()
    except Exception as e:
        print(f"❌ Gagal upload ke FTP: {e}")
