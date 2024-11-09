version=$(python3 -V 2>&1 | grep -Po '(?<=Python )(.+)')
if [[ -z "$version" ]]
then
    echo "Python not installed."
    exit 1
else
    echo "Python $version installed: [OK]"
fi

pip_version=$(pip3 -V 2>&1)
if [[ $? -ne 0 ]]
then
    echo "pip not installed. Attempting to install pip."
    sudo apt-get update
    sudo apt-get install -y python3-pip
else
    echo "pip installed: [OK]"
fi

if ! pip3 show virtualenv > /dev/null; then
    echo "Installing virtualenv..."
    pip3 install virtualenv
fi

env_name="my_virtual_env"
if [ ! -d "$env_name" ]; then
    echo "Creating virtual environment..."
    python3 -m virtualenv "$env_name"
else
    echo "Virtual environment $env_name already exists."
fi

echo "Activating virtual environment..."
source "$env_name/bin/activate"

if ! pip show pycryptodome > /dev/null; then
    echo "Installing pycryptodome..."
    pip install pycryptodome
else
    echo "pycryptodome already installed."
fi

echo "Setup complete. Virtual environment '$env_name' is ready and activated."
