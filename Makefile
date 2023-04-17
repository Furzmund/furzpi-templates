help:
	@cat Makefile

# Remove the template git repo
remove-git:
	@./.remove_git.sh

# Create virtual environment
venv:
	@virtualenv venv
	@echo "Activate environment with: 'source ./venv/bin/activate'"

# Install requirements needed to run the program
install-req:
	@pip install -r requirements.txt

# Install requirements needed by the developer
install-dev-req:
	@pip install -r requirements-dev.txt

# Compile requirements file
compile-req:
	@pip-compile --output-file=requirements.txt

# Compile development requirements file
compile-dev-req:
	@pip-compile --extra=dev --output-file=requirements-dev.txt

# Remove all packages installed
uninstall-all:
	@pip freeze | grep -v "^-e" | xargs pip uninstall -y

# Install pre-commit hook
pre-commit:
	@pre-commit install

# Remove pre-commit hook
remove-pre-commit:
	@pre-commit uninstall

test:
	@pytest tests

# Remove all untracked and ignored files/directories
# CAUTION: This will delete venv, .python-version, etc.
clean-all:
	@git clean -fx .

build:
	@python -m build .

# Remove build directories and re-build
rebuild:
	@rm -rf dist
	@rm -rf *.egg-info
	@python -m build .
