import os
import shutil

UPLOAD_DIR = "uploads"

def create_upload_dir():
    """
    Create uploads directory if it doesn't exist.
    """
    os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_upload_files(uploaded_files):
    """
    Save Streamlit uploaded files.
    Args:
        uploaded_files (list): List of UploadedFile objects
    Returns:
        list: Saved file paths
    """

    create_upload_dir()
    saved_files = []

    for uploaded_file in uploaded_files:
        file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        saved_files.append(file_path)
    return saved_files

def get_uploaded_files():
    """
    Return all uploaded file paths.
    """

    create_upload_dir()
    files = []

    for file in os.listdir(UPLOAD_DIR):
        files.append(os.path.join(UPLOAD_DIR, file))
    return files


def delete_uploaded_files():
    """
    Delete all uploaded files.
    """

    if os.path.exists(UPLOAD_DIR):
        shutil.rmtree(UPLOAD_DIR)
    create_upload_dir()