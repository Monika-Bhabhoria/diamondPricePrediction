echo [$(date)]: "START"

echo [$(date)]: "creating env"

conda create --prefix ./env python=3.8 -y

echo [$(date)]: "Activating Env"

source activate ./env

echo [$(date)]: "Installing the requirements.txt"

pip install -r requirements.txt

echo [$(date)]: "END"