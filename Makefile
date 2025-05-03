migrate:	
	docker-compose exec app alembic upgrade head

revision:	
	docker-compose exec app alembic revision --autogenerate -m "$(msg)"

build:	
	docker-compose build

up:	
	docker-compose up -d

logs:	
	docker-compose logs -f

shell:	
	docker-compose exec app sh

init-db:	
	$(MAKE) build	
	$(MAKE) up	
	$(MAKE) migrate