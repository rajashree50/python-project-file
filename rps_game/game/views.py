from django.shortcuts import render

# Create your views here.
import random

def index(request):
    options = ['rock','paper','scissors']
    computer_choice = None
    player_choice = None
    result = ''

    if request.method == 'POST':
        player_choice = request.POST.get('choice')
        if player_choice in options:
            computer_choice = random.choice(options)
            
            if player_choice == computer_choice:
                result = 'Tie!'
            elif(player_choice,computer_choice)in[
                ('rock','scissors'),
                ('paper','rock'),
                ('scissors','paper')

            ]:
                result = 'you win!'
            else:
                result = 'you lose.'
    return render(request,'game/index.html',{
        'player_choice':player_choice,
        'computer_choice': computer_choice,
        'result':result
    })