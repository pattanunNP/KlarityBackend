from pydantic import BaseSettings,Field



class RedisConfig(BaseSettings):
    REDIS_PORT: str = Field(..., env="REDIS_PORT")
    REDIS_HOST : str = Field(..., env="REDIS_HOST")
    REDIS_PASSWORD : str = Field(..., env="REDIS_PASSWORD")


    class Config:
        env_file_encoding = 'utf-8'
        case_sensitive = True
class MilvusConfig(BaseSettings):
    MILVUS_PORT: str = Field(..., env="MILVUS_PORT")
    MILVUS_HOST : str = Field(..., env="MILVUS_HOST")
    MILVUS_ALAIS : str = Field(..., env="MILVUS_ALAIS")

    class Config:
        env_file_encoding = 'utf-8'
        case_sensitive = True