import os,shutil
path = r"C:/Users/Student/Documents/Galaxy A20/Download/"
files= os.listdir(path)
# for file in files:
#     print(file)
Folder_names = ["Pdf files", "Powerpoint files", "Music", "Images", "word documents", "videos"]
for loop in range(len(Folder_names)):
    if not os.path.exists(path + Folder_names[loop]):
        os.makedirs(path + Folder_names[loop])

for file in files:
    if ".pdf" in file and not os.path.exists(path + "Pdf files/" + file):
        shutil.move(path + file, path + "Pdf files/" + file)
    if ".pptx" in file and not os.path.exists(path + "Powerpoint files/" + file):
        shutil.move(path + file, path + "Powerpoint files" + file)
    if ".mp4" in file and not os.path.exists(path + "videoss/" + file):
        shutil.move(path + file, path + "videos/" + file)
    if "IMG" in file and not os.path.exists(path + "Images/" + file):
        shutil.move(path + file, path + "Images/" + file)
    if ".docx" in file and not os.path.exists(path + "word documents/" + file):
        shutil.move(path + file, path + "word documents/" + file)
    if ".mp3" in file and not os.path.exists(path + "Music/" + file):
        shutil.move(path + file, path + "Music/" + file)
