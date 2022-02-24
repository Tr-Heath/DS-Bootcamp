#The beginning
#Let's create a sample set for a coin flip
sample_set = ["heads", "tails"]

def probability_check_sample_set(sample_set):
    if len(sample_set) != 0:
        return 1 / len(sample_set)
    else:
        return 0

def select(sample_set):
    return sample_set[0]

print(select_outcome(sample_set))
print(f'The probability of choosing one element in the given sample set is: {probability_check_sample_set(sample_set)}')
