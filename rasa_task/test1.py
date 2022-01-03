from rasa_nlu.model import Interpreter
import pdb
# modelpath ="/home/ubuntu/media/aibot/production/models/current/merged20to22sept"
modelpath ="models/current/intentClassifier3/"
print("\n\n\n\nLoading model from ", modelpath)
#pdb.set_trace()
interpreter = Interpreter.load(modelpath)
while True:
    inp = input("Input :\t")
    if inp=='q':
        break
    o = interpreter.parse(inp)
    print('Model_Output:\t' ,o['intent']['name'], o['intent']['confidence'] )
