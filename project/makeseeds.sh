echo "creating usercards/seeds.json"
python manage.py dumpdata usercards --output usercards/seeds.json --indent=2;


echo "creatingtemplates/seeds.json"
python manage.py dumpdatatemplates --outputtemplates/seeds.json --indent=2;

echo "creating comments/seeds.json"
python manage.py dumpdata comments --output comments/seeds.json --indent=2;

echo "creating jwt_auth/seeds.json"
python manage.py dumpdata jwt_auth --output jwt_auth/seeds.json --indent=2;