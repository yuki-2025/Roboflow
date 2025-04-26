import roboflow
from roboflow import Roboflow  # This line is missing


rf = Roboflow(api_key=" ")
project = rf.workspace().project("my-first-project-ykneo")
model = project.version(1).model

# Infer on a local image

response = model.predict("IMG_9961.jpg", confidence=70, overlap=30).json()

sum = 0
for pred in response['predictions']:
    print(pred['class'])
    if pred['class'] == 'quarter':
        sum += 0.25
    if pred['class'] == 'dime':
        sum += 0.10
    if pred['class'] == 'nickel':
        sum += 0.05
    if pred['class'] == 'penny':
        sum += 0.01

print("The sum is $" + str(sum))