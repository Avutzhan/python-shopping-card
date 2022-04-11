# python-shopping-card

Main service

GET http://172.23.0.3:5000/api/products/5/like

Commands
```shell
sudo docker-compose up --build
sudo docker-compose up -d db
sudo docker-compose up backend queue
docker-compose exec backend sh
python consumer.py
flask db init
flask db upgrade
```
