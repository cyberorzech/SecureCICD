coverage run --source=. -m pytest tests/test_app.py
coverage report -m
coverage html -d tests/html_report