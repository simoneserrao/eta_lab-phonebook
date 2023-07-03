# test_phonebook.py
ETA
Setup
pip install -r requirements.txt
Unittest
python -m unittest -v
Pytest
pytest .
Test Coverage
coverage and pytest-cov packages are required
Add pragma: no cover to exclude code from coverage report
With pytest
Terminal report:

pytest --cov-report term-missing --cov .
HTML report:

pytest --cov-report html --cov .
With unittest
To generate report:

python -m coverage run -m unittest
To view report in terminal:

python -m coverage report
To view report in HTML:

python -m coverage html
