from fastapi import APIRouter, Request
from fastapi import Form
from models import Mensagem
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/")
async def home(request: Request):
	mensagens = await Mensagem.all()
	return templates.TemplateResponse("index.html", {"request": request, "mensagens": mensagens})

#@router.delete("/notes/{mensagem_id}")
#async def listar(mensagem_id: int):
#    deleted_count = await Mensagem.filter(id=mensagem_id).delete()
#    return {"deleted": deleted_count}

@router.get("/get-notes")
async def get_notes():
	mensagens = await Mensagem.all()
	return mensagens

@router.post("/notes")
async def add(request: Request, texto: str = Form(...)):
	mensagem = await Mensagem.create(mensagem=texto)
	return RedirectResponse(url=request.url_for('home'), status_code=303)
