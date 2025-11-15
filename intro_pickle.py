import pickle 

# lines for introduction script 
intro_script = [
    'Hi there, my name is QT!',
    'What\'s your name?',
    'It’s really nice to meet you',
    'Today, we are going to be working with the Mood Meter.', 
    'This is a tool that will help us to understand our feelings. Each corner of the Mood Meter represents a type of emotion. As we go from left to right along the line, it represents how pleasant we are feeling.',
    'The left side has more unpleasant emotions',
    'and the right side is more pleasant.',
    'Going up and down the middle line shows how much energy we feel',
    'High energy emotions are higher up', 
    'while lower energy ones are lower on the meter.',
    'These lines split the Mood Meter into four corners, and each area has a color that goes with it. The red area is home to emotions that feel unpleasant with higher energy in our bodies,',
    'like angry',
    'and scared.',
    'The blue area is home for emotions that feel unpleasant with lower energy,',
    'like sad or lonely',
    'The green area is home for emotions that feel pleasant with lower energy,',
    'like relaxed and calm',
    'The yellow area is home for emotions that feel pleasant with higher energy,',
    'like excited!',
    'and happy!',
    'Take a look at the Mood Meter and see what other emotions you recognize!',
    'Great! I am going to be asking you to use this Mood Meter to help describe emotions and how you feel.'
]

# dictionary version of intro
# intro_script = {
#     '1': 'Hi there, my name is QT! It’s really nice to meet you! Today, we are going to be working with the Mood Meter.', 
#     '2': 'This is a tool that will help us to understand our feelings. Each corner of the Mood Meter represents a type of emotion. As we go from left to right along the line, it represents how pleasant we are feeling.',
#     '3': 'The left side has more unpleasant emotions',
#     '4': 'and the right side is more pleasant.',
#     '5': 'Going up and down the middle line shows how much energy we feel',
#     '6': 'High energy emotions are higher up', 
#     '7': 'while lower energy ones are lower on the meter.',
#     '8': 'These lines split the Mood Meter into four corners, and each area has a color that goes with it. The red area is home to emotions that feel unpleasant with higher energy in our bodies,',
#     '9': 'like angry',
#     '10': 'and scared.',
#     '11': 'The blue area is home for emotions that feel unpleasant with lower energy,',
#     '12': 'like sad or lonely',
#     '13': 'The green area is home for emotions that feel pleasant with lower energy,',
#     '14': 'like relaxed and calm',
#     '15': 'The yellow area is home for emotions that feel pleasant with higher energy,',
#     '16': 'like excited!',
#     '17': 'and happy!',
#     '18': 'Take a look at the Mood Meter and see what other emotions you recognize!',
#     '19': 'Great! I am going to be asking you to use this Mood Meter to help describe emotions and how you feel.'
# }

with open('intro_script.pkl', 'wb') as f:  # open a text file
    pickle.dump(intro_script, f) # serialize the list

f.close()


conclusion_script = [
    "Amazing job today!",
    "You did really well at using the Mood Meter.",
    "I hope you learned some new emotions today.",
    "I really enjoyed talking with you! See you next time!"
]

with open('outro_script.pkl', 'wb') as f:  # open a text file
    pickle.dump(intro_script, f) # serialize the list

f.close()

with open('intro_script.pkl', 'rb') as f:
    intro_script_loaded = pickle.load(f) # deserialize using load()
    print(intro_script_loaded[3]) # print script

f.close()