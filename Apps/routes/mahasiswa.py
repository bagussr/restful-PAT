from Apps.modules import (
    APIRouter,
    Depends,
    Session,
    Optional,
    JSONResponse,
    File,
    UploadFile,
    Body,
    open,
    os,
    pathlib,
)
from Apps.controller.mahasiwa import MahasiswaModel
from Apps.confiq import get_db
from Apps.models.mahasiswa import GetMahasiswaSchema, MahasiswaSchema, CreateMahasiswaSchema, MahasiswaUpdateSchema

router = APIRouter(prefix="/mahasiswa", tags=["Mahasiswa"])

x = pathlib.Path("public").absolute()

print(x)


@router.get("/")
def get_all_mahasiswa(db: Session = Depends(get_db)):
    mahasiswa = MahasiswaModel(db)
    x = mahasiswa.get_all_mahasiswa()
    return {"data": x, "status": "success"}


@router.get("//{id}", response_model=Optional[GetMahasiswaSchema])
def get_mahasiswa_by_id(id: int, db: Session = Depends(get_db)):
    mahasiswa = MahasiswaModel(db)
    return mahasiswa.get_mahasiswa_by_id(id)


@router.post("/")
async def create_mahasiswa(
    payload: CreateMahasiswaSchema = Body(...), file: UploadFile = File(), db: Session = Depends(get_db)
):
    mahasiswa = MahasiswaModel(db)
    try:
        new_mahasiswa = await mahasiswa.create_mahasiswa(payload, os.path.join("public/") + file.filename)
        async with open(os.path.join(x, file.filename), "wb") as r:
            content = await file.read()
            await file.close()
            await r.write(content)
    except Exception as e:
        return JSONResponse(status_code=400, content={"message": "Error when upload file", "detail": str(e)})
    return {"data": new_mahasiswa, "status": "success"}


@router.put("/{id}")
async def update_mahasiswa(id: int, payload: MahasiswaUpdateSchema, db: Session = Depends(get_db)):
    mahasiswa = MahasiswaModel(db)
    response = await mahasiswa.update_mahasiswa(id, payload)
    return {"data": response, "status": "success"}


@router.delete("/{id}")
def delete_mahasiswa(id: int, db: Session = Depends(get_db)):
    mahasiswa = MahasiswaModel(db)
    mahasiswa.delete_mahasiswa(id)
    return JSONResponse(content={"status": "success"}, status_code=200)
