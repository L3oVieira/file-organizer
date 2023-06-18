import os
from pathlib import Path
import shutil
import random
from datetime import datetime

# Pasta raiz
root_folder = 'C:/Users/leona/Downloads/'
os.chdir(root_folder)

# Pasta que conterá os arquivos organizados
main_folder = './ARQUIVOS_ORGANIZADOS'

if not os.path.exists(main_folder):
    os.mkdir(main_folder)
    

# Pasta atual
print('Você está no diretório: ', os.getcwd())

# Classe ext_dir
class ext_dir:
    def __init__(self, ext, folder):
        self.ext = ext
        self.folder = folder

# Lista com extensões e diretórios
extents = []

extents.append(ext_dir('txt', '/TEXTOS/TXT'))
extents.append(ext_dir('pdf', '/TEXTOS/PDF'))
extents.append(ext_dir('png', '/IMAGENS/PNG'))
extents.append(ext_dir('jpg', '/IMAGENS/JPG'))
extents.append(ext_dir('jpeg', '/IMAGENS/JPEG'))
extents.append(ext_dir('gif', '/IMAGENS/GIF'))
extents.append(ext_dir('mp3', '/MUSICAS/MP3'))
extents.append(ext_dir('wav', '/MUSICAS/WAV'))
extents.append(ext_dir('mp4', '/VIDEOS/MP4'))
extents.append(ext_dir('mkv', '/VIDEOS/MKV'))
extents.append(ext_dir('rar', '/ZIP/RAR'))
extents.append(ext_dir('zip', '/ZIP/ZIP'))
extents.append(ext_dir('7z', '/ZIP/7ZIP'))
extents.append(ext_dir('exe', '/PROGRAMAS/EXE'))
extents.append(ext_dir('msi', '/PROGRAMAS/MSI'))

# Cria pastas para cada extensão
for exts in extents:
    if not os.path.exists(exts.folder):
        os.makedirs(exts.folder)

# Datas customizadas
customized_date = datetime.now().strftime('%d/%m/%Y as %H:%M:%S')
customized_date_file = datetime.now().strftime('%d-%m-%Y')

#Arquivo de log
log = f'../log_{customized_date_file}.txt'
log_file = open(log, 'a')

log_file.write(f'\n\n------------------------------------------------------------------------')
log_file.write(f'\nIniciando Log em {customized_date}')

# logica de organização e movimentação de arquivos
count_files_moved = 0

for file in os.listdir():
    name, ext = os.path.splitext(file)
    ext_dotless = ext.strip('.').lower()

    if os.path.isfile(file):
        for entrie in extents:
            path = entrie.folder
            if ext_dotless == entrie.ext:
                
                if not os.path.exists(f'{main_folder}{path}/{file}'):
                    shutil.move(file, f'{main_folder}{path}/{name}.{ext_dotless}')
                    log_file.write(f'\n  {name}{ext} -> {path}/{name}.{ext_dotless} - em {customized_date}')
                    count_files_moved += 1
                else:
                    rand = random.randint(1, 9999)
                    rand2 = random.randint(1, 9)
                    new_name = f'{name}_{rand * rand2}'
                    shutil.move(file, os.path.join(path, f'{new_name}.{ext_dotless}'))
                    log_file.write(f'\n  {name}{ext} -> {path}/{new_name}.{ext_dotless} - em {customized_date}')
                    count_files_moved += 1
        
# Terminal e Log
print(f'\n------------------------------------------------------------------------')

if (count_files_moved == 0):    
    print('\n  Nenhum arquivo foi movido')
    log_file.write(' Nenhum arquivo foi movido')
    print(f'\n------------------------------------------------------------------------')
elif (count_files_moved == 1):
    print(f'\n  {count_files_moved} arquivo foi movido...')
    log_file.write(f'\n {count_files_moved} arquivo foi movido...')
    print(f'\n------------------------------------------------------------------------')
else:
    print(f'\n  {count_files_moved} arquivos foram movidos...')
    log_file.write(f'\n {count_files_moved} arquivos foram movidos...')
    print(f'\n------------------------------------------------------------------------')

log_file.write(f'\n------------------------------------------------------------------------')
log_file.write(f'\n...finalizando atividades')
log_file.close()
