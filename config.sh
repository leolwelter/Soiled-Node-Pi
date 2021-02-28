#! /bin/bash
# this should be run on each new node
# before running the Docker container
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install python3 -y
sudo apt-get install python3-pip -y
sudo apt-get install python3-venv
#cd ~ || exit
# clone the GitHub repo, which should contain this, so that's kind of meta
# TODO
#mkdir soiled && cd soiled || exit
python3 -m venv .env
source .env/bin/activate
pip3 install -r requirements.txt