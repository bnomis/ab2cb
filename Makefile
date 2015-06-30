PEP := pep8
PYFLAKES := pyflakes
FLAKE8 := flake8

RM := rm -rf
src := src/ab2cb/*.py
PANDOC := pandoc
RST2HTML := rst2html-2.7.py
PYTHON := python
CHMOD := chmod -R
TWINE := twine

.PHONY: dev sdist wheel docs rst html

wheel:
	$(PYTHON) setup.py bdist_wheel 

sdist:
	$(PYTHON) setup.py sdist

twine: sdist wheel
	$(TWINE) upload dist/*

docs: rst html

rst: docs/README.rst

html: docs/README.html

docs/README.rst: README.md
	-@ mkdir docs
	$(PANDOC) -f markdown -t rst -o $@ $<

docs/README.html: docs/README.rst
	-@ mkdir docs
	$(RST2HTML) $< $@

register: rst
	$(PYTHON) setup.py register

pep8:
	-@ $(PEP) $(src)

pyflakes:
	-@ $(PYFLAKES) $(src)

flake8:
	-@ $(FLAKE8) $(src)

# will fail if dev is not on the path
# source bin/activate.sh first
dev:
	-@ mkdir dev
	@ python setup.py develop -d dev

test:
	@ tox

coverage:
	@ tox -c tox-coverage.ini

coverclean:
	@ $(RM) .coverage htmlcov

devclean:
	@ $(RM) dev

clean: coverclean devclean
	@ $(RM) pip-install.log .tox debug.log debug.log.* dist *.egg-info tests-out docs