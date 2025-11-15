import pickle

charades_script = {
    "intro": "Now, let's play emotional charades! I'm going to act out an emotion and it is your job to guess where on the mood meter I am feeling. Are you ready?",
    "can't hear": "I can’t hear you. I said are you ready?",
    "beginning game": "Great! Let's begin!",
    "asking pleasant": "Am I feeling unpleasant or pleasant?",
    "incorrect": "Incorrect, try again.",
    "asking energy": "Correct! Am I feeling high energy or low energy?",
    "asking zone": "Correct! What zone am I in?",
    "asking emotion": "Correct! What emotion am I feeling?",
    "asking why emotion": "Why did you pick that emotion?",
    "interesting": "That's interesting",
    "awesome": "That's awesome",
    "good job": "Good job everyone!",
    "confirm unpleasant": "Did you pick unpleasant?",
    "confirm pleasant": "Did you pick pleasant?",
    "confirm high": "Did you pick high energy?",
    "confirm low": "Did you pick low energy?",
    "red description": "The emotion I picked was anger. It felt unplesant and I had high energy.",
    "blue description": "The emotion I picked was sadness. It felt unpleasant and I low energy.",
    "green description": "The emotion I picked was excitement. It felt pleasant and I had high energy.",
    "yellow description": "The emotion I picked was calmness. It felt pleasant and I had low energy."
}

with open('charades_script.pkl', 'wb') as file:  # open a text file
    pickle.dump(charades_script, file) # serialize the list

file.close()