from src.infra.db.settings.base import Base

class Users(Base):
    __tablename__ = 'users'

    id = Base.Column(Base.Integer, primary_key=True, autoincrement=True)
    first_name = Base.Column(Base.String(256), nullable=False)
    last_name = Base.Column(Base.String(256), nullable=False)
    age = Base.Column(Base.Integer, nullable=False)

    def __repr__(self):
        return f'Users(id={self.id}, first_name={self.first_name})'
