# python-shopping-card

Admin service

GET http://localhost/api/products

Commands
```shell
sudo docker-compose up --build
sudo docker-compose up -d db
sudo docker-compose up backend queue
docker-compose exec backend sh
python consumer.py
python manage.py makemigrations
python manage.py migrate
```
