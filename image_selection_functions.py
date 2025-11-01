import os
from tkinter import Tk, filedialog, Button, Label, Entry, messagebox
import shutil
from mask_creation import extract_and_create_masks  # Import the function from mask_creation

# Global variable to store the selected folder path
selected_folder_path = None

def get_image_paths(project_path):
    """
    Opens a file selection dialog using tkinter, retrieves image paths,
    and calls the provided callback function with the paths.
    """
    root = Tk()
    root.title("Select Images")
    root.geometry("400x200")  # Adjust window size as needed

    def create_new_project():
        project_name = project_name_entry.get()  # Get project name from Entry widget
        if not project_name:
            print("Please enter a project name!")
            return
        project_path = os.path.join(os.getcwd(), project_name)
        create_folder(project_path)
        input_folder = os.path.join(project_path, "input")
        create_folder(input_folder)  # Create the "input" subfolder
        select_images(project_path)  # Call to select images for the new project

    def open_existing_project():
        global selected_folder_path  # Use global variable
        selected_folder_path = filedialog.askdirectory(title="Select Existing Project")
        if not selected_folder_path:
            print("No project selected.")
            return
        input_folder = os.path.join(selected_folder_path, "input")
        if not os.path.exists(input_folder):
            # Show messagebox with a button to select images
            result = messagebox.askquestion(title="Missing 'input' folder", message="Existing project doesn't have an 'input' folder. Select images to create it?", icon='question')
            if result == 'yes':
                select_images(selected_folder_path)  # Call to select images for existing project (no input folder)
            else:
                root.destroy()  # Close the main window if user cancels
        else:
            # Close the dialog box after confirmation message
            messagebox.showinfo(title="Project Opened", message=f"Opened existing project: {selected_folder_path}")
            extract_and_create_masks(selected_folder_path)  # Call mask creation function
            root.destroy()  # Destroy the main window after selecting an existing project

    instructions_label = Label(root, text="Project:")
    instructions_label.pack(pady=5)

    project_name_entry = Entry(root)
    project_name_entry.pack(pady=5)

    create_project_button = Button(root, text="Create New Project", command=create_new_project)
    create_project_button.pack(pady=5)

    open_project_button = Button(root, text="Open Existing Project", command=open_existing_project)
    open_project_button.pack(pady=5)

    def select_images(selected_project_path):
        global filepaths
        filepaths = filedialog.askopenfilenames(filetypes=[("Image Files", "*.jpg")])
        for path in filepaths:
            print(f"Selected Image: {path}")
        input_folder = os.path.join(selected_project_path, "input")
        create_folder(input_folder)  # Ensure "input" subfolder exists
        copy_images(filepaths, input_folder)
        root.destroy()  # Destroy the window after selection

    root.mainloop()

    return filepaths if 'filepaths' in globals() else None  # Return None if no images were selected

def create_folder(folder_name):
    """
    Creates a folder with the given name if it doesn't exist already.
    """
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def copy_images(image_paths, destination_folder):
    """
    Copies the images from the provided paths to the specified destination folder.
    """
    for path in image_paths:
        filename = os.path.basename(path)
        new_path = os.path.join(destination_folder, filename)
        os.makedirs(os.path.dirname(new_path), exist_ok=True)  # Create destination directory if needed
        shutil.copy2(path, new_path)  # Use shutil.copy2 to preserve creation/modification times
        print(f"Image copied: {filename}")

# Get user input (create new or open existing project)
get_image_paths(None)  # No initial project path

# Now you can use selected_folder_path variable to access the selected folder path
if selected_folder_path:
    print("Selected folder path:", selected_folder_path)
