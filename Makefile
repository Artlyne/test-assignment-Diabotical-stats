# Makefile

lint:
		poetry run flake8 diabotical_stats
install:
		poetry build
		pip install --user dist/*.whl