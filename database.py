from redis_om import get_redis_connection, HashModel

redis = get_redis_connection(
    host="redis-17720.c274.us-east-1-3.ec2.cloud.redislabs.com",
    port="17720",
    password="mKHlo37VVoRhesZEo68KAruIshDseZcM",
    decode_responses=True
)

class Product(HashModel):
    name:str
    price:float
    quantity:int

    class Meta:
            database = redis