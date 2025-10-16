import redis
import config

redis_client = redis.Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    decode_responses=True,
    username=config.REDIS_USER,
    password=config.REDIS_PASSWORD,
)

pubsub = redis_client.pubsub()
pubsub.subscribe('school')

# Слухаємо повідомлення
with open('school_messages.txt', 'a', encoding='utf-8') as f:
    for message in pubsub.listen():
        if message['type'] == 'message':
            text = message['data']
            if 'контрольна робота' in text:
                f.write(text + '\n')
                print("Збережено:", text)