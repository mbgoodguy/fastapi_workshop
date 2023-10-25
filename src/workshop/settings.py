from pydantic_settings import BaseSettings


# когда создается экземпляр этого класса, под капотом читаются перем-ые окружения и находит перем-ые с именами
# соотв-щими этим полям. Далее оттуда они достаются, валидируются и преобразуются в нужные.
class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = '7000'


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)
