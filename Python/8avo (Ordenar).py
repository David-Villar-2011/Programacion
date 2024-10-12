import os
import glob
import shutil

while (True):
    if os.path.exists("Documentos") == True:
        pass
    else:
        os.mkdir("Documentos")
        continue

    if os.path.exists("Fotos") == True:
        pass
    else:
        os.mkdir("Fotos")
        continue

    if os.path.exists("Videos") == True:
        pass
    else:
        os.mkdir("Videos")
        continue

    if os.path.exists("Otros") == True:
        pass
    else:
        os.mkdir("Otros")
        continue

    if os.path.exists("Música") == True:
        pass
    else:
        os.mkdir("Música")
        break

# Fotos
png = glob.glob("*.png")
jpg = glob.glob("*.jpg")
jpeg = glob.glob("*.jpeg")

# Videos
mp4 = glob.glob("*.mp4")
mkv = glob.glob("*.mkv")
avi = glob.glob("*.avi")
mov = glob.glob("*.mov")
divx = glob.glob("*.divx")

# Audios
wav = glob.glob("*.wav")
mp3 = glob.glob("*.mp3")
aac = glob.glob("*.acc")
aiff = glob.glob("*.aiff")
wma = glob.glob("*.wma")
flv = glob.glob("*.flv")

# Documentos
pdf = glob.glob("*.pdf")
doc = glob.glob("*.doc")
docx = glob.glob("*.docx")
odt = glob.glob("*.odt")
txt = glob.glob("*.txt")

# Otros
py = glob.glob("*.py")
rar = glob.glob("*.rar")
zip = glob.glob("*.zip")
exe = glob.glob("*.exe")

# Mover archivos (fotos)
for i in (png):
    shutil.move(i, "fotos")
for i in (jpg):
    shutil.move(i, "fotos")
for i in (jpeg):
    shutil.move(i, "fotos")

# Mover archivos (videos)
for i in (mp4):
    shutil.move(i, "videos")
for i in (mkv):
    shutil.move(i, "videos")
for i in (avi):
    shutil.move(i, "videos")
for i in (mov):
    shutil.move(i, "videos")
for i in (flv):
    shutil.move(i, "videos")
for i in (divx):
    shutil.move(i, "videos")

# Mover archivos (audios)
for i in (mp3):
    shutil.move(i, "música")
for i in (aac):
    shutil.move(i, "música")
for i in (wav):
    shutil.move(i, "música")
for i in (aiff):
    shutil.move(i, "música")
for i in (wma):
    shutil.move(i, "música")

# Mover archivos (documentos)
for i in (pdf):
    shutil.move(i, "documentos")
for i in (doc):
    shutil.move(i, "documentos")
for i in (docx):
    shutil.move(i, "documentos")
for i in (txt):
    shutil.move(i, "documentos")
for i in (odt):
    shutil.move(i, "documentos")

# Mover archivo (otros)
for i in (py):
    shutil.move(i, "otros")
for i in (rar):
    shutil.move(i, "otros")
for i in (zip):
    shutil.move(i, "otros")
for i in (exe):
    shutil.move(i, "otros")
