import os

# extensions
file_audio = ['.aif','.cda','.mid','.midi','.mp3','.mpa','.ogg','.wav','.wma']
file_compressed = ['.7z','.deb','.pkg','.rar','.rpm', '.tar.gz','.z', '.zip']
file_documents = ['.ppt','.pptx','.pdf','.xls', '.xlsx','.doc','.docx','.txt', '.tex', '.epub']
file_codes = ['.js','.jsp','.html','.ipynb','.py','.java','.css']
file_images = ['.bmp','.gif', '.ico','.jpeg','.jpg','.png','.jfif','.svg','.tif','.tiff', '.PNG', '.JPG']
file_softwares = ['.apk','.bat','.bin', '.exe','.jar','.msi','.py']
file_videos = ['.3gp','.avi','.flv','.h264','.mkv','.mov','.mp4','.mpg','.mpeg','.wmv']

# downloads folder
downloads_folder = input("Enter filepath to sort folder by file type:")

# subfolders within downloads folder
downloads_subfolder = ['Audio', 'Compressed', 'Documents', 'Codes', 'Images', 'Software', 'Videos', 'Others']

# create those subfolders within downloads folder for the first time only
for subfolder in downloads_subfolder:
    dir_path = os.path.join(downloads_folder, subfolder)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)

# go back to downloads folder to get list of files 
os.chdir(downloads_folder)
for file in downloads_folder:
    downloads_folder_contents = os.listdir(downloads_folder)

# getting the extensions 
for file in downloads_folder_contents:

    # ignoring folders already existing and only looking at files and their extensions
    if os.path.isdir(file) == False:
        extensions = os.path.splitext(file)
        if extensions[1] in file_audio:
            os.rename(os.path.join(downloads_folder, file), os.path.join(downloads_folder, 'Audio', file))
        elif extensions[1] in file_compressed:
            os.rename(os.path.join(downloads_folder, file), os.path.join(downloads_folder, 'Compressed', file))
        elif extensions[1] in file_documents:
            os.rename(os.path.join(downloads_folder, file), os.path.join(downloads_folder, 'Documents', file))    
        elif extensions[1] in file_codes:
            os.rename(os.path.join(downloads_folder, file), os.path.join(downloads_folder, 'Codes', file))
        elif extensions[1] in file_images:
            os.rename(os.path.join(downloads_folder, file), os.path.join(downloads_folder, 'Images', file))
        elif extensions[1] in file_softwares:
            os.rename(os.path.join(downloads_folder, file), os.path.join(downloads_folder, 'Software', file))
        elif extensions[1] in file_videos:
            os.rename(os.path.join(downloads_folder, file), os.path.join(downloads_folder, 'Videos', file))
        else:
            os.rename(os.path.join(downloads_folder, file), os.path.join(downloads_folder, 'Others', file))
