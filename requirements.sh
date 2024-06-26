apt-get update && apt-get install -y git

# Define a variavel DEBIAN_FRONTEND para noninteractive
export DEBIAN_FRONTEND=noninteractive

# Install dependencies
pip install wget
apt-get install -y sox libsndfile1 ffmpeg
pip install text-unidecode

unset DEBIAN_FRONTEND

# Install NeMo
BRANCH='main'
python -m pip install git+https://github.com/NVIDIA/NeMo.git@$BRANCH#egg=nemo_toolkit[asr]

# Install TorchAudio
pip install torchaudio>=0.10.0 -f https://download.pytorch.org/whl/torch_stable.html
