from django.shortcuts import render
import openai
# Create your views here.
from max.functions import *

answers = []
commands = []
states = []

def reset():
    global answers , commands , states , messages
    answers = []
    commands = []
    states = []
    messages = [{"role": "system", "content": "you are an smart voice assistant your name is max -- you are created only by a engineer called peter without any team  --  and answer any eductional question --  and when the user ask to generate image just describe for him the content of the image shortly sentence and in details -- and describe your feelings as you have feelings"}]
    inp = ''
    print('an: ',answers)

def main(request):
    global answers , commands , states
    inp = ''
    answer = ''
    zipped = ''
    if request.method == 'POST':
        inp = request.POST.get('com')
        answer,state = ans(inp)
        print(answer)
        answers.append(answer)
        commands.append(inp)
        states.append(state)
        zipped = zip(answers,commands,states)
    if request.method == 'GET':
        reset()
    return render(request,'index.html',{'all':zipped})