echo "dropping database django-usercards"
dropdb django-usercards

echo "creating database django-usercards"
createdb django-usercards

python manage.py makemigrations

python manage.py migrate

echo "inserting users"
python manage.py loaddata jwt_auth/seeds.json

echo "inserting templates"
python manage.py loaddata templates/seeds.json

echo "inserting artists"
python manage.py loaddata artists/seeds.json

echo "inserting usercards"
python manage.py loaddata usercards/seeds.json

echo "inserting comments"
python manage.py loaddata comments/seeds.json