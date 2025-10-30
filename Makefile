deps:
	pip install -r requirements.txt
start:
	python3 main.py
venv:
	python -m venv testing-venv
	source testing-venv/bin/activate
conda:
	source /home/user0/miniconda3/bin/activate web