rm -rf db.sqlite3
rm -rf __pycache__
rm -rf db.sqlite3-journal
rm -rf chasse/__pycache__
rm -rf ticket/__pycache__
rm -rf static/images/tickets/*
python3 manage.py flush
python3 manage.py makemigrations
python3 manage.py migrate --run-syncdb
