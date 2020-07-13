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
python manage.py runserver
```


Methods |   Urls              |	Actions
--------|---------------------|--------------------------------------------------
GET	    |api/authors	        | get all authors
POST	  |api/authors	        | add new Author
GET	    |api/authors/:id	    | get authors by id
PUT	    |api/authors/:id	    | update Author by id
DELETE	|api/authors/:id	    | remove Author by id
GET	    |api/news	            | get all news
POST	  |api/news	            | add new News post
GET	    |api/news/:id	        | get news by id
PUT	    |api/news/:id	        | update news by id
DELETE	|api/news/:id	        | remove News post by id
GET	    |api/news?filter=[kw]	| find all News which title and text contains 'kw'
