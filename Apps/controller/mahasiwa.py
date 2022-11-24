from Apps.models.mahasiswa import Mahasiswa, MahasiswaSchema
from Apps.modules import Session, Optional, HTTPException, os


class MahasiswaModel:
    def __init__(self, db):
        self.db: Session = db

    def get_all_mahasiswa(self):
        return self.db.query(Mahasiswa).all()

    def get_mahasiswa_by_id(self, id: int):
        return self.db.query(Mahasiswa).filter(Mahasiswa.id == id).first()

    async def create_mahasiswa(self, payload: MahasiswaSchema, file: str):
        _mahasiswa = self.db.query(Mahasiswa).filter(Mahasiswa.email == payload.email).first()
        if _mahasiswa:
            raise HTTPException(status_code=400, detail="Email already registered")
        mahasiswa = Mahasiswa(email=payload.email, fullname=payload.fullname, nim=payload.nim, image=file)
        self.db.add(mahasiswa)
        self.db.commit()
        self.db.refresh(mahasiswa)
        return mahasiswa

    async def update_mahasiswa(self, id, payload: Optional[MahasiswaSchema]):
        mahasiswa = self.get_mahasiswa_by_id(id)
        if not mahasiswa:
            raise HTTPException(status_code=404, detail="Mahasiswa not found")
        if payload.fullname is not None:
            mahasiswa.fullname = payload.fullname
        if payload.nim is not None:
            mahasiswa.nim = payload.nim
        if payload.email is not None:
            mahasiswa.email = payload.email
        self.db.merge(mahasiswa)
        self.db.commit()
        self.db.refresh(mahasiswa)
        return mahasiswa

    def delete_mahasiswa(self, id: int):
        mahasiswa = self.db.query(Mahasiswa).filter(Mahasiswa.id == id).first()
        os.remove(mahasiswa.image)
        if not mahasiswa:
            raise HTTPException(status_code=404, detail="Mahasiswa not found")
        self.db.delete(mahasiswa)
        self.db.commit()
        return mahasiswa
