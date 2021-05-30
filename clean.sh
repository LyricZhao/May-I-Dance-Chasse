python3 manage.py flush
rm -rf db.sqlite3 __pycache__
python3 manage.py migrate --run-syncdb
