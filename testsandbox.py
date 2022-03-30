#Test functions and datasets from the Sandbox
import sandbox
sample_space = sandbox.sample_space
print(sample_space)

print(f'The probability of choosing one element in the given sample space is: {sandbox.probability_check_sample_set(sample_space)}')
print('For an Event Condition, which Events in a given Sample Space will Satisfy it?')
print(f'For the condition "Is Heads?" the event {sandbox.get_matching_event(sandbox.is_heads, sample_space)} is required')