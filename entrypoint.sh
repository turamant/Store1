#!/bin/sh
set -e

echo "⏳ Ожидание запуска PostgreSQL..."

# Ждём, пока PostgreSQL начнёт принимать подключения
while ! nc -z db 5432; do
  echo "💤 База данных ещё не готова. Жду 2 секунды..."
  sleep 2
done

echo "🗄️ Применение миграций Alembic..."
alembic upgrade head

echo "🚀 Запуск FastAPI приложения..."
exec "$@"