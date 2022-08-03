from datetime import datetime
from re import S
from domain.base.repository import RepositoryAbstract
from infarstructure.redis import RedisConnector


class sessionReposity(RepositoryAbstract):


    def __init__(self):
        super().__init__()
        self.redis =  RedisConnector.connect()
      

    def save(self, key, value, exp = 60 * 15):
        try:
            self.redis.set(f"{key}",
                value,
                ex = exp
            )
        except Exception as err:
            print(err)


    def search(self, id_):
        return self.redis.get(id_)

    def delete(self, id_):
        self.redis.delete(id_)








    
        

