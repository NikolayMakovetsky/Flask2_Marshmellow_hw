from app import Learner
from schema import LearnerSchema

learner = Learner(name='Vlad', id=10, final_test=True)
learner_schema1 = LearnerSchema()
result = learner_schema1.dump(learner)

print(result, type(result)) 


learners = [
    Learner(name="Alex", final_test=True),
    Learner(id=2, name="Bill", final_test=False),
    Learner(id=3, name="Tom", final_test="r")
]
learner_schema2 = LearnerSchema(many=True)
result = learner_schema2.dump(learners)
print(result, type(result))