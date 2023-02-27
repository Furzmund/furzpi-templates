#/bin/sh

echo "
 Setup will:
 - Remove the template git repository (.git directory)
 - Create a clean git repository
 - Create a virtual environment
 - Install package requirements into the virtual environment
 - Install Pre-Commit hook
"

echo "Remove template git repo"
./.remove_git.sh
if [ $? != 0 ]; then
    exit 0
fi

echo "
Initialize new git repo"
git init

echo "
Create environment"
virtualenv venv
source ./venv/bin/activate

echo "
Install packages"
python -m pip install --upgrade pip
pip install --requirement requirements.txt
pip install --requirement requirements-dev.txt

echo "
Install pre-commit hook"
pre-commit install

echo "
Activate virtual environment with:
    source ./venv/bin/activate
Deactivate with:
    deactivate
"

echo "NOTE:
    After updating pyproject.toml with packages,
    remember to run 'make compile-req' and/or
    'make compile-dev-req' respectively
"
