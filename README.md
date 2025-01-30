

## local env (Windows)
---------------------
1. cd /path/to/your/project
2. 	python -m venv eats-venv		# create virtual env first time only
	.\venv\Scripts\activate			# activate venv
	python -m ensurepip --upgrade
3. # First time installed libs can be: pip freeze > requirements.txt
	pip install -r requirements.txt  
   # any error run below command
   # pip install -r requirements.txt --user

4. Run:
	set FLASK_ENV=local (check: cmp>echo %FLASK_ENV% if prints %FLASK_ENV% means not set yet)
	python app.py


## Dev Deployment (ubuntu/debian)
--------------------------------

# sudo apt install python3-venv		
python3 -m venv eats-venv			# create virtual env first time only
cd eats-customer-api
source ../eats-venv/bin/activate			# activate going inside eats-customer-api
pip install -r requirements.txt


Run:
	export FLASK_ENV=dev				# Verify cmd: echo $FALSK_ENV
  	# Gunicorn Server: (Green Unicorn) with Nginix integration
	gunicorn -w 2 -b 127.0.0.1:5000 app:app
	
	# Non Nginix - All IPs
	# gunicorn -w 2 -b 0.0.0.0:5000 app:app

export FLASK_ENV=dev
python3 app.py


## Util commands --

Find process ID:
---------------
lsof -i :5000
kill -9 <PID>

Update Dependencies:
--------------------
pip freeze > requirements.txt


UTILS:
----
mkdir eats-customer-api && unzip eats-customer-api.zip -d eats-customer-api

Jenkins:
-------
zip:
tar -a -c -f eats-customer-api.zip *

remote:
unzip eats-customer-api.zip

or

(if Jenkins running in Windows)
powershell -Command "Compress-Archive -Path * -DestinationPath eats-customer-api.zip"

remote:
mkdir eats-customer-api && unzip eats-customer-api.zip -d eats-customer-api