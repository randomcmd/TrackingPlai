#!/usr/bin/env python

"""Tests for TAPIP3D import fix."""

import sys
import os

# Mock the required dependencies
class MockModule:
    """Mock module for testing imports without actual dependencies."""
    def __getattr__(self, name):
        return MockModule()
    
    def __call__(self, *args, **kwargs):
        return MockModule()
    
    def get_torch_device(self):
        return "cpu"

# Install mocks before importing
sys.modules['numpy'] = MockModule()
sys.modules['torch'] = MockModule()
sys.modules['comfy'] = MockModule()
sys.modules['comfy.model_management'] = MockModule()

def test_tapip3d_node_can_be_imported():
    """Test that Tapip3DNode can be imported without crashing."""
    from src.tapip3d import Tapip3DNode
    assert Tapip3DNode is not None
    assert Tapip3DNode.__name__ == "Tapip3DNode"

def test_tapip3d_node_has_required_attributes():
    """Test that the node has all required ComfyUI attributes."""
    from src.tapip3d import Tapip3DNode
    
    # Check required class attributes
    assert hasattr(Tapip3DNode, 'INPUT_TYPES')
    assert hasattr(Tapip3DNode, 'RETURN_TYPES')
    assert hasattr(Tapip3DNode, 'RETURN_NAMES')
    assert hasattr(Tapip3DNode, 'FUNCTION')
    assert hasattr(Tapip3DNode, 'CATEGORY')
    
    # Check attribute values
    assert Tapip3DNode.RETURN_TYPES == ("STRING", "IMAGE")
    assert Tapip3DNode.FUNCTION == "track"
    assert Tapip3DNode.CATEGORY == "Tracking"

def test_tapip3d_path_calculation():
    """Test that the TAPIP3D path is calculated correctly."""
    # Get the expected path
    repo_root = os.path.dirname(os.path.dirname(__file__))
    expected_path = os.path.join(repo_root, "TAPIP3D")
    
    # The path should exist (even if empty)
    assert os.path.exists(expected_path), f"TAPIP3D directory not found at {expected_path}"
    assert os.path.isdir(expected_path), f"TAPIP3D path is not a directory: {expected_path}"

def test_graceful_import_failure():
    """Test that import failure doesn't crash the module."""
    # The module should import successfully even if TAPIP3D is not set up
    # This is verified by the fact that other tests can import it
    from src.tapip3d import Tapip3DNode
    
    # The node should be instantiable
    node = Tapip3DNode()
    assert node is not None
