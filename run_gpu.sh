#!/bin/bash
cd ComfyUI

if [ -d "custom_nodes/TrackingPlai" ]; then
  # Updating custom node
  echo "Updating TrackingPlai"
  cd custom_nodes/TrackingPlai
  git pull
  cd ../..
else
  # Setting up custom node
  echo "Downloading TrackingPlai"
  cd custom_nodes
  git clone https://github.com/randomcmd/TrackingPlai
  cd TrackingPlai
  ./TAPIP3D_setup.sh
  ./AllTracker_setup.sh
  cd ..
  cd ..
fi

python main.py --preview-method auto --listen 0.0.0.0 --use-sage-attention