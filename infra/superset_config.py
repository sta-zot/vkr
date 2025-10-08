import os

SECRET_KEY = 'your_very_long_random_secret_key_here'  # Сгенерируйте надежный ключ, например, через модуль secrets в Python

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://superset:superset@superset-db:5432/superset'

CACHE_CONFIG = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': 300,
    'CACHE_KEY_PREFIX': 'superset_',
    'CACHE_REDIS_HOST': 'redis',
    'CACHE_REDIS_PORT': 6379,
    'CACHE_REDIS_DB': 1,
}

# Опционально: отключение загрузки примеров данных
SUPERSET_LOAD_EXAMPLES = False

# Опционально: настройка MinIO как S3-совместимого хранилища для миниатюр/кэша (сначала создайте бакет 'superset-thumbnails' в MinIO)
# THUMBNAIL_CACHE_CONFIG = {
#     'CACHE_TYPE': 'S3Cache',
#     'CACHE_BUCKET': 'superset-thumbnails',
#     'CACHE_S3_ENDPOINT_URL': 'http://minio:9000',
#     'CACHE_AWS_ACCESS_KEY_ID': 'minioadmin',
#     'CACHE_AWS_SECRET_ACCESS_KEY': 'minioadmin',
# }