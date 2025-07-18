from ftplib import FTP

ftp = FTP()
ftp.connect('ftp-sth.sta.my.id', 21)
ftp.login('hylab', 'hy4umlbT!1')

ftp.cwd('/ftp/image')  # Ganti path sesuai folder
print("🟢 Login dan navigasi berhasil!")

ftp.quit()
