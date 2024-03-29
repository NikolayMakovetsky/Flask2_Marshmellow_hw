from marshmallow import Schema, fields, validate
# Доп инструменты валидации: match-case, try-except

# Валидация применяется только при десериализации
# (преобразовании json-строки в словарь)
# для дальнейшей передачи словаря в ORM
class LearnerSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.Str(
        required=True,
        error_messages={
            'required': {
            'required': 'name is required',
            'code':400
            }
        },
        validate=[validate.Length(max=5)]
    )
    final_test = fields.Boolean(
        required=True,
        error_messages={'required': 'final_test is required'})

