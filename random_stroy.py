# Importing random module
import random

# Defining list of phrases which will help to build a story

Sentence_starter = ['About 100 years ago', ' In the 20 BC', 'Once upon a time']
character = [' there lived a king.',' there was a man named Jack.',
             ' there lived a farmer.']
time = [' One day', ' One full-moon night']
story_plot = [' he was passing by',' he was going for a picnic to ']
place = [' the mountains', ' the garden']
second_character = [' he saw a man', ' he saw a young lady']
age = [' who seemed to be in late 20s', ' who seemed very old and feeble']
work = [' searching something.', ' digging a well on roadside.']

times= int(input("Please input how many stories you want to generate="))

for i in range(1,times+1):
    
    if i ==1:
        print(f"\nthis is the {i}-st story:")
    elif i ==2:
        print(f"\nthis is the {i}-nd story:")    
    elif i ==3:
        print(f"\nthis is the {i}-rd story:")    
    else:
        print(f"\nthis is the {i}-th story:")        
        
        
    # Selecting an item from each list and concatenating them.
    print(random.choice(Sentence_starter)+random.choice(character)+
          random.choice(time)+random.choice(story_plot) +
          random.choice(place)+random.choice(second_character)+
          random.choice(age)+random.choice(work))