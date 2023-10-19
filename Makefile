.PHONY: run
run:
	python src/manage.py runserver

# fix formatting / and order imports
.PHONY: format
format:
	python -m black ./
	python -m isort ./
# check type annotations
.PHONY: types
types:
	python -m mypy --check-untyped-defs ./src

# check everything
.PHONY: check
check:
	python -m ruff .
	python -m black --check .
	python -m isort --check .
	python -m mypy --check-untyped-defs .