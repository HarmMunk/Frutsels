from pydantic import (
    BaseModel,
    BaseSettings,
    PyObject,
    RedisDsn,
    PostgresDsn,
    AmqpDsn,
    Field,
)


class SubModel(BaseModel):
    foo = 'bar'
    apple = 1


class Settings(BaseSettings):
    auth_key: str = "auth"  # the environment variable name is changed in Config in the fields into my_auth_key
    api_key: str = Field(env='my_api_key',default="ha")  # The environment variable is my_api_key, not api_key

    redis_dsn: RedisDsn = 'redis://user:pass@localhost:6379/1'
    pg_dsn: PostgresDsn = 'postgres://user:pass@localhost:5432/foobar'
    amqp_dsn: AmqpDsn = 'amqp://user:pass@localhost:5672/'

    special_function: PyObject = 'math.cos'

    # to override domains:
    # export my_prefix_domains='["foo.com", "bar.com"]'
    domains: set[str] = set()

    # to override more_settings:
    # export my_prefix_more_settings='{"foo": "x", "apple": 1}'
    more_settings: SubModel = SubModel()

    class Config:
        env_prefix = 'my_prefix_'   # This changes all environment variables, defaults to no prefix, i.e. ""
        fields = {
            #'auth_key': {
            #    'env': 'my_auth_key',
            #},
            'redis_dsn': {
                'env': ['service_redis_dsn', 'redis_url']
            }
        }


print(Settings().dict())