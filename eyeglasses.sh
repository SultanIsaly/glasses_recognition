# configuration script
sudo apt update
sudo apt-get update

sudo apt install build-essential checkinstall
sudo apt install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
sudo apt install libffi-dev

sudo git clone https://github.com/cleardusk/MeGlass.git

# get python
wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tar.xz
tar xvf Python-3.7.2.tar.xz
cd Python-3.7.2/
./configure
sudo make altinstall


# make venv with py37
cd ~
python3.7 -m venv ./eyec
cd eyec
. bin/activate

# install common libraries
pip install --upgrade pip
pip install numpy scipy pandas scikit-learn matplotlib jupyter
sudo pip install argparse

#pytorch
pip3 install torch torchvision