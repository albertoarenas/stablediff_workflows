import bpy



def set_scene_camera(camera_name):
    
    # Access the current scene
    scene = bpy.context.scene

    # Specify the camera by name
    camera = bpy.data.objects[camera_name]

    # Set the specified camera as the active camera
    scene.camera = camera


main_camera_name = "Camera.001"
set_scene_camera(main_camera_name)