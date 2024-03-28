from marshmallow import Schema, fields

class LearnerSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.Str()
    final_test = fields.Boolean()


# Доп параметры для поля email (Пример)
# required=True # параметр является обязательным
# error_messages={'required': 'email is required', 'code':400 }
# сообщение при возникновении ошибки