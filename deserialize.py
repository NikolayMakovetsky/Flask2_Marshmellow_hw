from schema import LearnerSchema
from pprint import pprint

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
pprint(result)
print(type(result))

# Python True == Json true !
json_data = """
[
    {
        "id": 1,
        "name": "Roma",
        "final_test": true
    },
    {
        "id": 2,
        "name": "Kiri",
        "final_test": false
    },
    {
        "id": 3,
        "name": "Evge",
        "final_test": true
    }
]
"""
schema2 = LearnerSchema(many=True) # raise JSONDecodeError("Expecting value", s, err.value) from None
result = schema2.loads(json_data)
pprint(result)
print(type(result))

