import os
import shutil

# 다운로드 폴더 경로
DOWNLOAD_FOLDER = r"C:\Users\2022761\Downloads"

# 파일 확장자별 이동할 폴더 설정
FILE_CATEGORIES = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".jfif"],
    "data": [".csv", ".xlsx"],
    "docs": [".txt", ".doc", ".docx",".pdf"],
    "archive": [".zip"],
    "exe": [".exe"],
    "ppt": [".ppt", ".pptx"],
}

# 각 폴더의 전체 경로 생성 및 폴더 생성
for folder in FILE_CATEGORIES.keys():
    folder_path = os.path.join(DOWNLOAD_FOLDER, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# 파일 이동 함수
for file_name in os.listdir(DOWNLOAD_FOLDER):
    file_path = os.path.join(DOWNLOAD_FOLDER, file_name)
    
    if os.path.isfile(file_path):  # 파일인 경우만 처리
        file_ext = os.path.splitext(file_name)[1].lower()
        
        for folder, extensions in FILE_CATEGORIES.items():
            if file_ext in extensions:
                dest_folder = os.path.join(DOWNLOAD_FOLDER, folder)
                shutil.move(file_path, os.path.join(dest_folder, file_name))
                print(f"Moved: {file_name} -> {dest_folder}")
                break
