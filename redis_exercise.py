import redis
import string
import random

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

values_to_insert = 100
key_name = 'my_key'

print("\n")

print(f"PUSHING {values_to_insert} RANDOM VALUES FOR THE KEY '{key_name}'...")
# loop 100 times and push (insert) a random value into a Redis list (stack) each time
for x in range(1, values_to_insert + 1):
    random_string = ''.join(random.choices(string.ascii_letters, k=7))
    print(f"{key_name}: {str(random_string)}")
    rlist = r.lpush(key_name, str(random_string))

print("\n")

# loop 100 times and pop (retrieve) a random value from the Redis list (stack) each time
print(f"POPPING THE VALUES FROM THE KEY '{key_name}'...")
for x in range(1, values_to_insert + 1):
    print(f"{key_name}: {r.lpop(key_name)}")

