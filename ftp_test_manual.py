from ftplib import FTP

ftp = FTP()
ftp.connect('ftp', 21)
ftp.login('user', 'password')

ftp.cwd('/ftp/image')  # Ganti path sesuai folder
print("🟢 Login dan navigasi berhasil!")

ftp.quit()
