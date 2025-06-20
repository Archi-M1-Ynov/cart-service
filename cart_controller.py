import redis
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Connexion Redis
r = redis.Redis.from_url(os.getenv("REDIS_URL"), decode_responses=True)

def get_cart(user_id):
    key = f"cart:{user_id}"
    cart = r.hgetall(key)
    return [{ "product_id": k, "quantity": int(v) } for k, v in cart.items()]

def add_to_cart(user_id, product_id, quantity):
    key = f"cart:{user_id}"
    r.hincrby(key, product_id, quantity)
    return { "product_id": product_id, "quantity": int(r.hget(key, product_id)) }

def remove_from_cart(user_id, product_id):
    key = f"cart:{user_id}"
    r.hdel(key, product_id)
    return { "product_id": product_id, "removed": True }
