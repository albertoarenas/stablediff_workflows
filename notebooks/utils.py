# Built-in
from typing import Optional, Union
from pathlib import Path 

# External
import matplotlib.pyplot as plt
from PIL import Image

def display_image(image_path: Union[str, Path]) -> None:
    """
    Displays an image from the specified file path.

    Args:
        image_path (Union[str, Path]): The path to the image file, which can be a string or a Path object.

    Returns:
        None. Displays the image using matplotlib in a Jupyter notebook or similar environment.
    """
    # Ensure the image path is a Path object for consistent handling
    if not isinstance(image_path, Path):
        image_path = Path(image_path)

    # Load the image file
    img = Image.open(image_path)

    # Display the image
    plt.imshow(img)
    plt.axis('off')  # Turn off axis numbers and ticks
    plt.show()

def find_latest_file(directory: Union[str, Path], prefix: str, extension: str) -> Optional[str]:
    """Finds the latest file in the specified directory with the given prefix and file extension.

    Args:
        directory (Union[str, Path]): The directory where the files are located, can be a string or a Path object.
        prefix (str): The prefix that filenames should start with.
        extension (str): The file extension of interest. Ensure it starts with a dot ('.').

    Returns:
        Optional[str]: The full path to the most recently created file that matches the given criteria.
                       Returns None if no matching file is found.

    Example usage:
        latest_file = find_latest_file(Path('/path/to/your/folder'), 'sample', '.png')
        print("The latest file is:", latest_file)
    """
    # Ensure directory is a Path object for uniform handling
    if not isinstance(directory, Path):
        directory = Path(directory)

    # Normalize the extension to ensure it starts with a dot
    if not extension.startswith('.'):
        extension = '.' + extension
    
    # List all files that match the extension and prefix
    files = [file for file in directory.iterdir() if file.name.endswith(extension) and file.name.startswith(prefix)]
    
    # Get full paths and creation times
    files_with_times = [(file, file.stat().st_birthtime) for file in files]
    
    # Sort files by creation time (most recent first)
    files_with_times.sort(key=lambda x: x[1], reverse=True)
    
    # Return the most recent file's path if there are any files
    return str(files_with_times[0][0]) if files_with_times else None

