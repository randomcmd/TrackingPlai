from inspect import cleandoc

class Tapip3DNode:
    """
    Tapip3D Tracking
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "images": ("IMAGE",),
                "tracking_point_x": ("FLOAT",),
                "tracking_point_y": ("FLOAT",),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("tracking_preview")
    # DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "track"

    CATEGORY = "Tracking"

    def track(self, images, tracking_point_x, tracking_point_y):
        return (images,)