from inspect import cleandoc
import numpy as np
import json

import comfy.model_management as mm

class Tapip3DNode:
    """
    Tapip3D Tracking
    """
    def __init__(self):
        self.device = mm.get_torch_device()
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

    RETURN_TYPES = ("STRING", "IMAGE",)
    RETURN_NAMES = ("tracking_results", "tracking_preview")
    # DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "track"

    CATEGORY = "Tracking"

    def track(self, images, tracking_point_x, tracking_point_y):
        images_np = images.cpu().numpy()
        images_np = np.ascontiguousarray((images_np * 255).astype(np.uint8))
        video = self.preprocess_images(images)

        _ = video

        # Track video using model
        results = [{
            "x": tracking_point_x, 
            "y": tracking_point_y, 
            "z": 0,
        }] * images.len

        # Transform tracked point to string
        return (json.dumps(results), images,)
    
    def preprocess_images(self, images):
        # (B, H, W, C) -> (1, B, C, H, W)
        if len(images.shape) == 4:
            images = images.permute(0, 3, 1, 2)  # (B, C, H, W)
            images = images.unsqueeze(0)  # (1, B, C, H, W)
        
        images = images.float()
        images = images * 255
        
        return images.to(self.device)