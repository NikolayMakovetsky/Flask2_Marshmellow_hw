from schema import LearnerSchema

# Python True == Json true !
json_data = """
{
    "id": 1,
    "name": "Ivan",
    "final_test": true
}
"""
schema1 = LearnerSchema() # работает
result = schema1.loads(json_data)
print(result, type(result))

# Python True == Json true !
json_data = """
[
    {
        "id": 1,
        "name": "Roman",
        "final_test": true
    },
    {
        "id": 2,
        "name": "Kirill",
        "final_test": false
    },
    {
        "id": 3,
        "name": "Evgeniy",
        "final_test": true
    }
]
"""
schema2 = LearnerSchema(many=True) # raise JSONDecodeError("Expecting value", s, err.value) from None
result = schema2.loads(json_data)
print(result, type(result))

