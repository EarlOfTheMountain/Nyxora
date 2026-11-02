# Nyxora
A small python game using pygame

# Development setup:

Make sure you have Python3 and pip installed,  We will use Debian as an example:

```sh
sudo apt update
sudo apt install python3 python3-pip python3-venv

```
Then we need to setup a virtual environment and install pygame and basedpyright for your editor/IDE.
First, clone the repo:
```bash
git clone https://github.com/EarlOfTheMountain/Nyxora.git
cd Nyxora
# Create the virtual environment for pygame and basedpyright
python3 -m venv .venv
# Now we need to activate the virtual environment we just created, assuming bash,
source .venv/bin/activate
#Then we install pygame and basedpyright, which is in the requirements.txt
python3 -m pip install -r requirements.txt
```
We can now use LSP with the editor of our choice and navigate the code.
To run the game, simply:
```sh
./main.py
```
