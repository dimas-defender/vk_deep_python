build:	cjson.c
	python -m venv venv
	./venv/Scripts/activate
	pip install -r requirements.txt
	python setup.py install

clean:
	rm -rf __pycache__ dist build cjson.egg-info

time:
	python exec_time.py

test:
	python -m unittest test_cjson.py