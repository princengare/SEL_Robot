import pickle

child_story = {
    "intro": "Now you can try! Can you tell a story about yourself? You can talk about anything you want.",
    "if_no": "That’s okay! We can move on and if you want we can try next time!",
    "if_yes": "Great! Start whenever you want and tell whatever story you’d like.",
    "affirm": "Wow that was a great story! Now I’d like you to point out where you felt on the mood meter. Were you feeling pleasant or unpleasant?",
    "energy": "Were you feeling high energy or low energy?",
    "color": "That sounds like you felt like you were in the",
    "color_pt_2": "corner. What emotion do you think you felt? How did you feel in your body while you were feeling it?",
    "red": " red ",
    "blue": " blue ",
    "green": " green ",
    "yellow": " yellow ",
    "thanks": "Thanks for sharing!"
}

emotion_regulation = {
    "intro": "Now let’s talk about how we can deal with emotions. We all feel emotions like anger and sadness, but sometimes it helps to be able to lessen those feelings so we can be in the moment. Let’s imagine you’re feeling",
    "valence":"Let’s find out where that is on the mood meter. Does",
    "valence_2": "feel pleasant or unpleasant?",
    "if_correct":"That’s right!",
    "if_wrong":"Close, but normally we would say that",
    "if_wrong_2": " is a ",
    "if_wrong_3": "emotion.",
    "energy":"Does ",
    "energy_2":"feel high energy or low energy?",
    "corner":"Since ",
    "corner_2":" is a ",
    "corner_3":"and ",
    "corner_4":" emotion, we would say it is in the",
    "corner_5":"corner.",
    "feel":"Emotions in this corner might make us ",
    "activity":" In order to calm down, we can do things like ",
    "affirm": "Great job! When we do this, we can deal with ",
    "affirm_2": " in a safe way and start to feel more calm and pleasant.",
    "angry": " angry ",
    "angry_valence": " unpleasant ",
    "angry_energy": " high energy ",
    "angry_color": " red ",
    "angry_feel": "Sweaty, shaky, with a really fast heartbeat and tense muscles. Sometimes anger can grow very big and explode like a volcano!",
    "angry_activity": "Exercise! Let’s try practicing by running in place for a few seconds.",
    "sad": " sad ",
    "sad_valence": "unpleasant",
    "sad_energy": " low energy ",
    "sad_color": " blue ",
    "sad_feel": "Cry, with a tummy ache, no energy, and not wanting to speak. Sometimes sadness can make it hard for us to have fun and enjoy things.",
    "sad_activity": "Breathing! Let’s practice. Start by strengthening your hand out like a star. Next, use your other hand to slide up each finger slowly and then slowly back down the other side. While you slide up, breathe in through your nose and when you slide down breathe out through your mouth. Keep doing this until you finish tracing your hand. Let’s do it together: Breathe in, breathe out, breathe in, breathe out, breathe in, breathe out, breathe in, breathe out, breathe in, breathe out.",
    "excited": " excited ",
    "excited_valence": " pleasant ",
    "excited_energy": " high energy ",
    "excited_color": " yellow ",
    "excited_feel": "Laugh, smile, talk loudly, feel warm, dance, and jump.",
    "excited_activity": "Dancing! Let’s do some dancing. If you can’t dance while you feel excited because you are doing something else, consider talking to someone else about your excitement or doing something quiet, like drawing.",
    
}

anger_story = {
    "intro": "Now let’s begin with the first activity! I’m going to tell you about something that happened to me, and I want you to think about how I was feeling. At the end of the story, I’ll ask you to guess where my feelings were on the Mood Meter. Are you ready?",
    "story": (
        "Yesterday afternoon, when I was looking for my favorite pair of scissors in the classroom, I noticed that my classmate Leo was using them. "
        "“HEY!” I said loudly, “I ALWAYS use those scissors!” Leo said, “But these belong to everyone.” I shouted, “Give me those scissors!” I kicked over the chair "
        "and it almost hit Leo. I didn’t mean to do it, but I was really upset. How do you think I was feeling - was it pleasant or unpleasant?"
    ),

    "if_unpleasant": "Yes, that's right! Do you think it was high energy or low energy?",
    "if_pleasant": "That's not quite right - I was upset, so I was feeling unpleasant.",
    "if_unrelated": "I didn't understand. Please answer pleasant or unpleasant.",
    "if_he": "Good job!",
    "if_le": "Almost there - I felt strong feelings of anger, so it was a high energy feeling.",
    
    "mood_meter": "Now can you point out the color on the Mood Meter?",
    
    "if_rcolor": "That's right! I was feeling a strong, unpleasant feeling so I was in the red zone",
    "if_not_rcolor": "Close! I was feeling a strong, unpleasant feeling so I was in the red zone.",
    
    "prompt": "Can you guess the emotion word?",
    
    "if_angry": "Good guess! I was feeling furious - that means I was REALLY angry.",
    "if_not_angry": "Almost there! I was feeling furious - that means I was REALLY angry.",
    
    "prompt2": "Do you think yelling and kicking the chair was a good way to express my feelings?",
    
    "if_yes": "Not quite. Even though it's normal to feel angry, my actions were hurtful, and I shouldn't have reacted that way. I went to a corner of the classroom and practiced slow breathing to calm down. I realized that instead of shouting at Leo, I could have asked him, “Can I use those scissors when you’re done?”, or said, “It’s okay, I can use another scissor this time”.",
    "reply": "That's right - I shouldn’t have reacted that way. I went to a corner of the classroom and practiced slow breathing to calm down. I realized that instead of shouting at Leo, I could have asked him, “Can I use those scissors when you’re done?”, or said, “It’s okay, I can use another scissor this time”.",
    
    "reflection": "Now that I told you my story, can you think of a time when you felt angry? How did you deal with it?",
    "reflection_response": "Thank you for sharing! I'll see you next time."
}

sad_story = {
    "intro": "Now let’s begin with the first activity! I’m going to tell you about something that happened to me, and I want you to think about how I was feeling. At the end of the story, I’ll ask you to guess where my feelings were on the Mood Meter. Are you ready?",
    "story": (
        "Yesterday, during playtime, my best friend, Penny, wasn’t there. I felt lonely without her,"
        "but I still wanted to play. I asked my some of my classmates, “Hey, can I play with you?”. But they ignored me."
        "I tried asking again, but they still didn’t talk to me. My chest felt tight and I started to cry. I didn’t feel"
        "like playing anymore, so I walked back into the classroom for the rest of playtime. How do you think I was feeling - was it pleasant or unpleasant?"

    ),

    "if_unpleasant": "Yes, that's right! Do you think it was high energy or low energy?",
    "if_pleasant": "That's not quite right - I was upset, so I was feeling unpleasant.",
    "if_he": "Almost there - I felt down, so it was a low energy feeling.",
    "if_le": "Good job!",
    
    "mood_meter": "Now can you point out the color on the Mood Meter?",
    
    "if_rcolor": "That's right! I was feeling a low, unpleasant feeling so I was in the blue zone",
    "if_not_rcolor": "Close! I was feeling a low, unpleasant feeling so I was in the blue zone.",
    
    "prompt": "Can you guess the emotion word?",
    
    "if_sad": "Good guess! I was feeling very sad and lonely without my friend. It hurt to be ignored by my classmates.",
    "if_not_sad": "Almost there! I was feeling very sad and lonely without my friend. It hurt to be ignored by my classmates.",
    
    "prompt2": "Do you think crying was a good way to express my feelings?",
    
    "reply": "It's perfectly okay to cry when you're sad. It also helps to talk to a trusted friend or parent." ,
    
    "reflection": "Now that I told you my story, can you think of a time when you felt sad or lonely? How did you deal with it?",
    "reflection_response": "Thank you for sharing! I'll see you next time."
}

happy_story = {
    "intro": "Now let’s begin with the first activity! I’m going to tell you about something that happened to me, and I want you to think about how I was feeling. At the end of the story, I’ll ask you to guess where my feelings were on the Mood Meter. Are you ready?",
    "story": (
        "Yesterday, when I came home from school, I saw a little brown box behind the front door. “What’s inside this box, Mommy?” I asked."
        "She said, “I have a surprise for you! Why don’t you open it and see what’s inside?” I slowly opened the box, and I saw the cutest black kitten inside."
        "“Surprise!”, said Mommy, “this is your new pet, Mimi”. “Thank you, Mommy!”, I said, jumping up and down. I have always wanted a pet cat, and I spent"
        "the rest of the day playing and running around with Mimi, my new best friend. How do you think I was feeling when I saw Mimi - was it a pleasant or unpleasant feeling?" 
    ),

    "if_pleasant": "Yes, that's right! Do you think it was high energy or low energy?",
    "if_unpleasant": "That's not quite right - it felt really good to see Mimi, so it was a pleasant feeling.",
    "if_he": "Good job!",
    "if_le": "Not quite - I was jumping up and down, so it was a high energy feeling.",
    
    "mood_meter": "Now can you point out the color on the Mood Meter?",
    
    "if_rcolor": "That's right! I was feeling a high, pleasant feeling so I was in the yellow zone",
    "if_not_rcolor": "Close! I was feeling a high, pleasant feeling so I was in the yellow zone.",
    
    "prompt": "Can you guess the emotion word?",
    
    "if_happy": "Good guess! I felt ecstatic to see Mimi - that means I was VERY happy to finally have a cute pet!",
    "if_not_happy": "Almost there! I felt ecstatic to see Mimi - that means I was VERY happy to finally have a cute pet!",
    
    "reflection": "Now that I told you my story, can you think of a time when you felt happy or excited? How did you deal with it?",
    "reflection_response": "Thank you for sharing! I'll see you next time."
}

calm_story = {
    "intro": "Now let’s begin with the first activity! I’m going to tell you about something that happened to me, and I want you to think about how I was feeling. At the end of the story, I’ll ask you to guess where my feelings were on the Mood Meter. Are you ready?",
    "story": (
        "Yesterday, when I went to school, I was very stressed about my math test. I spent a lot of time studying for it."
        "Before the test, my teacher said, “I know you all are worried about the test. Let’s do a breathing activity before we start”."
        "I took a deep breath in through my nose - one…two…three, and slowly let it out through my mouth. I did this again three times."
        "Slowly, my shoulders relaxed and all my worries melted away. I wasn’t stressed anymore. How do you think the breathing exercise made me feel - was it a pleasant or unpleasant emotion?"
    ),

    "if_pleasant": "Yes, that's right! Do you think it was high energy or low energy?",
    "if_unpleasant": "That's not quite right - I was feeling good after the breathing exercise, so it was a pleasant emotion.",
    "if_le": "Good job!",
    "if_he": "Not quite - I was feeling more relaxed, so it was a low energy feeling.",
    
    "mood_meter": "Now can you point out the color on the Mood Meter?",
    
    "if_rcolor": "That's right! I was feeling a low, pleasant feeling so I was in the green zone",
    "if_not_rcolor": "Close! I was feeling a low, pleasant feeling so I was in the green zone.",
    
    "prompt": "Can you guess the emotion word?",
    
    "if_calm": "Good guess! All my stress disappeared, so I was feeling calm",
    "if_not_not": "Almost there! All my stress disappeared, so I was feeling calm and relaxed",

    "prompt2": "Do you think doing the breathing exercise was a good way to deal with stress?",
    
    "reply": "Deep breathing is a great way to calm down. It's like telling your brain - \"Don't worry, everything will be okay!\"", 
    
    "reflection": "Now that I told you my story, can you think of a time when you felt calm or relaxed? What did you do?",
    "reflection_response": "Thank you for sharing! I'll see you next time."
}

with open('anger_story.pkl', 'wb') as file:
    # change first arg based on which story you want to choose
    pickle.dump(anger_story, file)

with open('sad_story.pkl', 'wb') as file:
    # change first arg based on which story you want to choose
    pickle.dump(sad_story, file)

with open('happy_story.pkl', 'wb') as file:
    # change first arg based on which story you want to choose
    pickle.dump(happy_story, file)    

with open('calm_story.pkl', 'wb') as file:
    # change first arg based on which story you want to choose
    pickle.dump(calm_story, file)



# with open('child_story.pkl', "wb") as file:
#     pickle.dump(child_story, file)
    
# with open("emotion_regulation.pkl", "wb") as file:
#     pickle.dump(emotion_regulation, file)