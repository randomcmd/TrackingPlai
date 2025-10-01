from inspect import cleandoc

from .alltracker_demo_modified import run

class AllTrackerNode:
    """
    AllTracker Tracking
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

    def track(self, images):
        return (images,)