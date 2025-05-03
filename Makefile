.PHONY: migrate revision build up logs shell init-db stop

# Применить миграции
migrate:	
	docker-compose exec app alembic upgrade head

# Создать новую миграцию
revision:	
	docker-compose exec app alembic revision --autogenerate -m "$(msg)"

# Собрать образы
build:	
	docker-compose build

# Запустить контейнеры в фоне
up:	
	docker-compose up -d

# Просмотр логов
logs:	
	docker-compose logs -f

# Открыть shell в контейнере
shell:	
	docker-compose exec app sh

# Инициализация БД (сборка + запуск + миграции)
init-db:	
	build up migrate

# Остановить и удалить контейнеры
stop:	
	docker-compose down