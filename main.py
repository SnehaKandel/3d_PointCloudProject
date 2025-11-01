import os
import subprocess
from image_selection_functions import get_image_paths
import mask_creation

def main():
    colmap_path = r"D:\Major\COLMAP-3.9.1-windows-cuda\colmap.bat"
    if not os.path.exists(colmap_path):
        print("COLMAP executable not found! Please check the path.")
        return

    # Run COLMAP
    colmap_process = subprocess.Popen([colmap_path, "gui"])

    # Wait for COLMAP process to complete
    colmap_process.wait()

    # Once COLMAP is closed, proceed to open Jupyter Notebook
    project_path = get_image_paths()  # Call the function to get the project path

    if project_path:
        mask_creation.create_masks(project_path)  # Pass the project_path

        # Open the Jupyter Notebook after COLMAP is closed
        notebook_path = "D:\\Major\\SNEHAMAJOR\\pointcloudtomesh.ipynb"   # Replace with the actual path
        os.system("jupyter notebook " + notebook_path)

if __name__ == "__main__":
    main()
