from tortoise import fields, models

class Mensagem(models.Model):
    id = fields.IntField(pk=True)
    mensagem = fields.TextField()
    criado_em = fields.DatetimeField(auto_now_add=True)