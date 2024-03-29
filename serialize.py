from pprint import pprint
from app import Learner
from schema import LearnerSchema

learner = Learner(name='Vladimir', id=10, final_test=True)
learner_schema1 = LearnerSchema()
result = learner_schema1.dump(learner)

pprint(result)
print(type(result))


learners = [
    Learner(id=1, name="Alexander", final_test=True),
    Learner(name="Bill", final_test=False),
    Learner(id=3, name="Tom", final_test="r") # final_test некорректный передается
]

if type(learners) == list:
    learner_schema2 = LearnerSchema(many=True)
    result = learner_schema2.dump(learners)
    pprint(result)
    print(type(result))