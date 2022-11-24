from Apps.confiq import Base
from Apps.modules import Column, String, Integer, DateTime, datetime, json, BaseModel, Optional


class Mahasiswa(Base):
    __tablename__ = "mahasiswa"
    id = Column(Integer, primary_key=True)
    email = Column(String(50), unique=True)
    nim = Column(String(10), unique=True)
    fullname = Column(String(50))
    image = Column(String(50))
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    def __repr__(self):
        data = {
            "id": self.id,
            "email": self.email,
            "nim": self.nim,
            "fullname": self.fullname,
            "image": self.image,
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at),
        }
        return json.dumps(data)


class MahasiswaSchema(BaseModel):
    email: str
    nim: str
    fullname: str


class MahasiswaUpdateSchema(BaseModel):
    email: Optional[str]
    nim: Optional[str]
    fullname: Optional[str]


class GetMahasiswaSchema(MahasiswaSchema):
    id: int


class CreateMahasiswaSchema(MahasiswaSchema):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate_to_json

    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value

    class config:
        orm_mode = True
