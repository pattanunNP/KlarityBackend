from redis import ConnectionPool, Redis
from domain.base.Singleton import Singleton
from config.config import RedisConfig

class RedisConnector(metaclass=Singleton):
    ENV = RedisConfig()

    redisPool = ConnectionPool(
        host=ENV.REDIS_HOST,
        port=ENV.REDIS_PORT,
        password=ENV.REDIS_PASSWORD,
        db=0
    )
    redis = Redis(connection_pool=redisPool)

    @classmethod
    def connect(cls) -> redis:
        print("Redis => Connected")
        
        return cls.redis