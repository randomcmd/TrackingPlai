git clone https://github.com/zbw001/TAPIP3D

cd TAPIP3D
pip install torch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 "xformers>=0.0.27" --index-url https://download.pytorch.org/whl/cu124
pip install torch-scatter -f https://data.pyg.org/whl/torch-2.4.1+cu124.html
pip install -r requirements.txt
pip install gdown

cd third_party/pointops2
LIBRARY_PATH=$CONDA_PREFIX/lib:$LIBRARY_PATH python setup.py install
cd ../..

cd third_party/megasam/base
LIBRARY_PATH=$CONDA_PREFIX/lib:$LIBRARY_PATH python setup.py install
cd ../../..

cd checkpoints/
wget https://huggingface.co/zbww/tapip3d/resolve/main/tapip3d_final.pth
cd ..

cd third_party/megasam/Depth-Anything
mkdir checkpoints
cd checkpoints
wget https://huggingface.co/spaces/LiheYoung/Depth-Anything/resolve/main/checkpoints/depth_anything_vitl14.pth
cd ../../../..

cd third_party/megasam/cvd_opt
gdown https://drive.google.com/file/d/1MqDajR89k-xLV0HIrmJ0k-n8ZpG6_suM/view?usp=drive_link
cd ../../..