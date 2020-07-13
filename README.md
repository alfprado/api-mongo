# api-mongo

Foi utilizado docker para subir um banco de dados mongodb.
```
docker pull mongo
```
```
docker run -d --name mongo-api -p 27017:27017 -p 28017:28017 -e AUTH=no mongo
```
```
docker start mongo-api
```
Passos para execução do projeto.

```
pip install -r requirements.txt
```
```
python manage.py migrate
```
```
python manage.py makemigrations
```
```
python manage.py runserver
```

