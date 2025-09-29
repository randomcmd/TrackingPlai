git clone https://github.com/aharley/alltracker

cd alltracker
pip install -r requirements.txt

cd demo_video
sh download_video.sh
cd ..

apt-get install -y ffmpeg