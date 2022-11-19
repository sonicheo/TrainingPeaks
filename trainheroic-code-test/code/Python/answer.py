import json




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

# HelperFunctions
# Finds the userId of the user whose lastName and firstName match
def findUserID(firsName, lastName):
    for user in users:
        if user['name_first'] == firsName and user['name_last'] == lastName:
            return(user['id'])

def findExerciseID(exerciseName):
    for exercise in exercises:
        if exercise['title'] == exerciseName:
            return exercise['id']

def totalWeightInBlock(blocks):
    weight = 0
    for block in blocks:
        for set in block['sets']:
            if set['weight']:
                weight += int(set['weight'])
    return weight

  
#question funtions 
def q1():
    pounds = 0
    for workout in workouts:
        pounds += totalWeightInBlock(workout['blocks'])
    return pounds        

def q2():
    userID = findUserID('Barry', 'Moore')
    pounds = 0  
    for workout in workouts:
        if workout['user_id'] == userID and '2016' in workout['datetime_completed']:
            pounds += totalWeightInBlock(workout['blocks'])
    
    return pounds

def q3():
    exerciseId = findExerciseID("Back Squat")
    userID = findUserID('Barry', 'Moore')
    
    for workout in workouts:
        if workout['user_id'] == userID and '2017' in workout['datetime_completed']:
            print(workout)
    

def q4():
    pass

q3()
q4()


# Collect answers
answers = {
    # In total, how many pounds have these athletes Bench Pressed?
    'q1': q1(),

    # How many pounds did Barry Moore Back Squat in 2016?
    'q2': q2(),

    # In what month of 2017 did Barry Moore Back Squat the most total weight?
    'q3': None,

    # What is Abby Smith's Bench Press PR weight?
    # PR defined as the most the person has ever lifted for that exercise, regardless of reps performed.
    'q4': None
}

print(json.dumps(answers))