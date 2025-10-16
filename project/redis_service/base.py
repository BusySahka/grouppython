"""Basic connection example.
"""

import redis

import config


redis_client = redis.Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    decode_responses=True,
    username=config.REDIS_USER,
    password=config.REDIS_PASSWORD,
)

redis_client.set('favorite_car', 'Ferrari F40 (1987)')

redis_client.set('favorite_pet', 'german shepherd', ex=2*60*60)

redis_client.delete('products_list')
redis_client.lpush('products_list', 'milk')
redis_client.lpush('products_list', 'eggs')
redis_client.rpush('products_list', 'bread')
redis_client.rpush('products_list', 'butter')

redis_client.expire('products_list', 7*24*60*60)

cake_ingredients = {"flour": 250, "milk": 500}
redis_client.hset('cake', mapping=cake_ingredients)
redis_client.hset('cake', 'sugar', 300)
redis_client.hset('cake', 'sugar', 500)

# redis_client.delete('cake')

messages = [
    "Сьогодні контрольна робота з біології",
    "Яка ж була нудна математика",
    "Пам'ятайте про контрольна робота наступного тижня"
]

for msg in messages:
    redis_client.publish('school', msg)

print("Все збережено та надіслано в канал school")

