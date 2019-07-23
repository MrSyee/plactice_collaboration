dev:
	pip install -U -r requirements.txt

test:
	flake8 . --exclude .env
	py.test --cov=. .