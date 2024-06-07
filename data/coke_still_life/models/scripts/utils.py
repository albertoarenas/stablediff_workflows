import bpy
from typing import Optional

def set_scene_camera(camera_name:str):
    """
    Sets the scene camera in Blender
    
    Args:
        camera_name (str): The name of the camera to set it as scene camera
        
    Returns:
        None
        
    This function finds the camera given it's name and after that it assign it as scene camera
    """
    
    # Access the current scene
    scene = bpy.context.scene

    # Specify the camera by name
    camera = bpy.data.objects[camera_name]

    # Set the specified camera as the active camera
    scene.camera = camera
    
    
def duplicate_material(material_name: str) -> Optional[bpy.types.Material]:
    """
    Duplicates a specified material in Blender.

    Args:
        material_name (str): The name of the material to duplicate.

    Returns:
        bpy.types.Material or None: The duplicated material object if the original exists,
        otherwise None.

    This function searches for a material by the given name, duplicates it if found,
    and returns the duplicate. If no material with the given name is found, it returns None.
    """
    # Attempt to find the material by name
    original_material = bpy.data.materials.get(material_name)
    
    # Check if the material was found
    if original_material is None:
        print(f"Material named '{material_name}' not found.")
        return None
    
    # Duplicate the material
    duplicated_material = original_material.copy()
    duplicated_material.name = f"{material_name} Copy"
    
    # Return the duplicated material
    return duplicated_material



main_camera_name = "Camera.001"
set_scene_camera(main_camera_name)