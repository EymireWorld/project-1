# Env files structure
## db.env
```
POSTGRES_HOST: str
POSTGRES_DB: str
POSTGRES_USER: str
POSTGRES_PASSWORD: str
```
## How to start
1. Clone repository
```
git clone https://github.com/EymireWorld/project-1.git
```
2. Start docker container
```
docker compose up -d
```
3. Join app shell
```
docker exec -t app sh
```
4. Start migrations
```
alembic revision --autogenerate
alembic upgrade head
```
5. Enjoy)