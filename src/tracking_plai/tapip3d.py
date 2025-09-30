from inspect import cleandoc
from pathlib import Path
import json

import sys
import os

PROJECT_ROOT = os.path.abspath(
    #\ComfyUI\custom_nodes     
    os.path.join(os.path.dirname(__file__), "..", "..", "TrackingPlai", "TAPIP3D", "utils")
)
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from utils.inference_utils import inference, load_model

import numpy as np
import torch

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
        # Track video using model
        resolution_factor = 2
        
        # TODO: import load_model(checkpoint) from TAPIP3D
        # from utils.inference_utils import load_model, read_video, inference, get_grid_queries, resize_depth_bilinear
        path = Path("")
        print(path.absolute)
        return ("", images)
    
        model = load_model("")
        model.to(self.device)

        inference_res = (int(model.image_size[0] * np.sqrt(resolution_factor)), int(model.image_size[1] * np.sqrt(resolution_factor)))
        model.set_image_size(inference_res)

        # TODO: Missing variables
        support_grid_size = None
        num_threads = None
        num_iters = None

        video, depths, intrinsics, extrinsics, query_point, support_grid_size = self.prepare_inputs_node(
            images=images, 
            inference_res=inference_res, 
            support_grid_size=support_grid_size,
            num_threads=num_threads,
            device=self.device
        )

        with torch.autocast("cuda", dtype=torch.bfloat16):
            # TODO: import inference from TAPIP3D
            coords, visibs = inference(
                model=model,
                video=video,
                depths=depths,
                intrinsics=intrinsics,
                extrinsics=extrinsics,
                query_point=query_point,
                num_iters=num_iters,
                grid_size=support_grid_size,
            )

        # Save results
        coords = coords.cpu().numpy()
        visibs = visibs.cpu().numpy()

        # dummy data
        frame_amount = video.shape[1]

        results = [{
            "x": tracking_point_x, 
            "y": tracking_point_y, 
            "z": 0,
        }] * frame_amount

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
    
    def prepare_inputs_node(self, images, inference_res, support_grid_size, num_threads, device):
        # TODO: Implement
        depths = None
        intrinsics = None
        extrinsics = None
        query_point = None
        support_grid_size = None

        images_np = images.cpu().numpy()
        images_np = np.ascontiguousarray((images_np * 255).astype(np.uint8))
        video = self.preprocess_images(images)

        return (video, depths, intrinsics, extrinsics, query_point, support_grid_size)