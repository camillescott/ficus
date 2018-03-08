all: install

deps: FORCE
		pip install --requirement requirements.txt
	
install: deps
		python setup.py install

test: FORCE
		python setup.py test

publish: FORCE
		python setup.py sdist upload

clean: FORCE
	rm -rf build/ *.pyc ficus/*.pyc ficus/*.egg-info  *.egg-info

FORCE:
