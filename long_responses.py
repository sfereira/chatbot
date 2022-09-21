import random

R_EATING = "I don't like eating anything because I'm a bot obviously! "

def unknown():
    response = ['Please re-phrase the sentence trying my best to understand.',
                '......',
                'Sounds about right but I\'m not so smart yet.',
                'What does that mean?'][random.randrange(4)]
    return  response