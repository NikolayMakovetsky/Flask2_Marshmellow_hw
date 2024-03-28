from schema import LearnerSchema

json_data = """
{
    "id": "1",
    "name": "Ivan",
    "final_test": "True"
}
"""
schema1 = LearnerSchema() # работает
result = schema1.loads(json_data)
print(result, type(result))


json_data = """
[
    {
        "id": 1,
        "name": "Roman",
        "final_test": True
    },
    {
        "id": 2,
        "name": "Kirill",
        "final_test": False
    },
    {
        "id": 3,
        "name": "Evgeniy",
        "final_test": True
    }
]
"""
schema2 = LearnerSchema(many=True) # raise JSONDecodeError("Expecting value", s, err.value) from None
result = schema2.loads(json_data)
print(result, type(result))

