all: install

deps: FORCE
		pip install --requirement requirements.txt
	
install: deps
		python setup.py install

test: FORCE
		python setup.py test

publish: FORCE
		python setup.py sdist upload

gh-pages:
		cd doc; make clean html
		touch doc/_build/html/.nojekyll
		git add doc/
		git commit -m "Generated gh-pages for `git log master -1 --pretty=short --abbrev-commit`"
		git subtree push --prefix doc/_build/html origin gh-pages


clean: FORCE
	rm -rf build/ *.pyc ficus/*.pyc ficus/*.egg-info  *.egg-info

FORCE:
