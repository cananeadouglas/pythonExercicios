import sqlalchemy
from sqlalchemy.orm import declarative_base # construir o objeto em python
from sqlalchemy import Column, Integer, String, Float, Boolean, Date, DateTime
from sqlalchemy.orm import sessionmaker
import datetime

#print (sqlalchemy.__version__) -> ver a versão do sistema

engine = sqlalchemy.create_engine('sqlite:///enterprise.db', echo=True)

Base = declarative_base() # Objeto criado "Base"

class User(Base):
    __tablename__ = 'users' # obrigatória

    id = Column(Integer, primary_key=True)
    name = Column(String(30) )
    fullname = Column(String(60))
    age = Column(Integer)

    def __repr__(self):
        return "<User(name={}, fullname{}, age={})>".format(self.name, self.fullname, self.age)

Base.metadata.create_all(engine) # criar a tabela.

user = User (name = 'Doug', fullname = 'Jose Douglas', age = 30)

# print(user.name) -> printando nome de usuário

Session = sessionmaker(bind=engine)

# print(Session) -> recuperando algumas informações

session = Session()

user = session.query(User).filter_by(name='Doug').first()

print (user)

session.delete(user)
session.commit()