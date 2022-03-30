#The beginning
#Let's create a sample set for a coin flip
sample_space = ["Heads", "Tails"]

#This example sample space allows for 4 different event conditions. Heads, Tails,
#Heads or Tails, or NOthing
#The set of elements that can satisfy an Event Condition from our Sample Space are the Events
#In other words, Heads, a single element from the Sample Space, satisfies the Event Contion that the element Is Heads
# ie. ->
def is_heads(event):
    return event == "Heads"
def is_tails(event):
    return event == "Tails"
def is_heads_or_tails(event):
    return event in sample_space
def is_neither(event):
    return event not in sample_space


#What's the probability of a given sample set, well 1 out of the number of elements of course!
def probability_check_sample_set(sample_space):
    if len(sample_space) != 0:
        return 1 / len(sample_space)
    else:
        return 0

#How about a function that will grab the event satisfying a given event condition?
def get_matching_event(event_condition, sample_space):
    event = sample_space[0]
    return event

def select(sample_space):
    return sample_space[0]

#print(select_outcome(sample_set))

