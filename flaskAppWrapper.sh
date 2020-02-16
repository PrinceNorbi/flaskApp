export FLASK_APP=/home/pi/git/flaskApp/flaskTestApp1.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --cert=/etc/letsencrypt/live/ad-astra.hu/fullchain.pem --key=/etc/letsencrypt/live/ad-astra.hu/privkey.pem
