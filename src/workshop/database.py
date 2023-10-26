from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .settings import settings

# определяем самое первоочередное для работы с алхимией
engine = create_engine(
    settings.database_url,
    connect_args={'check_same_thread': False}
)
# check_same_thread - фастапи использует фоновые потоки, а sqlite предпочитает работать в 1 потоке, то добавим такой
# параметр check_same_thread


# в алхимии вся работа с БД ведется через сессию. Созадем ее с помощью фабрики sessionmaker
Session = sessionmaker(
    engine,
    autoflush=False,
    autocommit=False
)


def get_session() -> Session:
    session = Session()
    try:
        yield session
    finally:
        session.close()
