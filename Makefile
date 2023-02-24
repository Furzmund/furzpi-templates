# Compile requirements file
compile-req:
	@pip-compile --output-file=requirements.txt

# Compile development requirements file
compile-dev-req:
	@pip-compile --extra=dev --output-file=requirements-dev.txt

install-req:
	@pip install -r requirements.txt

install-dev-req:
	@pip install -r requirements-dev.txt

uninstall-all:
	@pip freeze | grep -v "^-e" | xargs pip uninstall -y

pre-commit:
	@pre-commit install

test:
	@pytest tests

# Remove all untracked and ignored files/directories
clean_all:
	@git clean -fx .

build:
	@python -m build .

# Remove ignored files/directories, i.e. build files/dirs
# and re-build them
rebuild:
	@git clean -fX .
	@python -m build .
