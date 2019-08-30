# create a mad-libs | random story generator
# randomly select words to create a unique mad-libs story

from random import randint
import copy

# create a dictionary of the words of the type you will use in the story
word_dict = {
    'adjective':['greedy','abrasive','grubby','groovy','rich','harsh','tasty','slow'],
    'city name':['Chicago','New York','Charlotte','Indianapolis','Louisville','Denver'],
    'noun':['people','map','music','dog','hamster','ball','hotdog','salad'],
    'action verb':['run','fall','crawl','scurry','cry','watch','swim','jump','bounce'],
    'sports noun':['ball','mit','puck','uniform','helmet','scoreboard','player'],
    'place':['park','desert','forest','store','restaurant','waterfall']
}

# create a story and insert placeholders for the words you want to randomly select
story = (
    "One day my {} friend and I decided to go to the {} game in {}. " +
    "We really wanted to see the {} play the {}. " +
    "So, we {} our {} down to the {} and bought some {}s. " +
    "We got into the game and it was a lot of fun. " + 
    "We ate some {} {} and drank some {} {}. " +
    "We had a great time! We plan to go ahead next year!"
)

# create a function that will randomly select a word from the word_dict by type of word
def get_word(type, local_dict):
    ''' select words based on type and then pop the selected word from the list 
        so that it isn't select more than once '''
    words = local_dict[type]
    cnt = len(words)-1 # used to set range of index
    index = randint(0, cnt)
    return local_dict[type].pop(index)

# create a function that will insert a random word into the story, based on word type
def create_story():
    ''' create a story with randomly selected words of certain type '''
    local_dict = copy.deepcopy(word_dict) # deepcopy to prevent changes to word_dict
    return story.format(
        get_word('adjective', local_dict),
        get_word('sports noun', local_dict),
        get_word('city name', local_dict),
        get_word('noun', local_dict),
        get_word('noun', local_dict),
        get_word('action verb', local_dict),
        get_word('noun', local_dict),
        get_word('place', local_dict),
        get_word('noun', local_dict),
        get_word('adjective', local_dict),
        get_word('noun', local_dict),
        get_word('adjective', local_dict),
        get_word('noun', local_dict)
    )

print("STORY 1: ")
print(create_story())
print()
print("STORY 2:")
print(create_story())

