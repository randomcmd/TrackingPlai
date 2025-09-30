from .example import TrackingPlai
from .alltracker import AllTrackerNode
from .tapip3d import Tapip3DNode

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "TrackingPlai": TrackingPlai,
    "AllTracker": AllTrackerNode,
    "Tapip3D": Tapip3DNode
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "TrackingPlai": "Tracking Plai"
}