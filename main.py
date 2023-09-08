import send2trash
import os

# Substitua o caminho abaixo pelo caminho da sua lixeira
trash_path = 'C:\\$Recycle.Bin'

for root, dirs, files in os.walk(trash_path):
    for file in files:
        file_path = os.path.join(root, file)
        send2trash.send2trash(file_path)