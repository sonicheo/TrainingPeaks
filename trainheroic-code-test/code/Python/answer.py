import json

# Collect answers
answers = {
    # In total, how many pounds have these athletes Bench Pressed?
    'q1': None,

    # How many pounds did Barry Moore Back Squat in 2016?
    'q2': None,

    # In what month of 2017 did Barry Moore Back Squat the most total weight?
    'q3': None,

    # What is Abby Smith's Bench Press PR weight?
    # PR defined as the most the person has ever lifted for that exercise, regardless of reps performed.
    'q4': None
}


# Load data
with open('../../data/users.json') as json_file:
    users = json.load(json_file)
json_file.close()

with open('../../data/exercises.json') as json_file:
    exercises = json.load(json_file)
json_file.close()

with open('../../data/workouts.json') as json_file:
    workouts = json.load(json_file)
json_file.close()


# Candidate TODO: Write code to answer questions


# Output answers
print json.dumps(answers)