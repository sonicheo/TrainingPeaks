import json
from datetime import datetime




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

#----------------------------------------------------------------------------
# HelperFunctions

# Finds the userId of the user whose lastName and firstName match
def findUserID(firsName, lastName):
    for user in users:
        if user['name_first'] == firsName and user['name_last'] == lastName:
            return(user['id'])

#Finds the id of the exercise that is inputed
def findExerciseID(exerciseName):
    for exercise in exercises:
        if exercise['title'] == exerciseName:
            return exercise['id']

#TODO: turn totalWeightInBlocks into a class so it grabs a different function based on parameters entered

# Grabs blocks and adds the total weight from each exercise
def totalWeightInBlock(blocks):
    weight = 0
    for block in blocks:
        for set in block['sets']:
            if set['weight']:
                weight += int(set['weight'])
    return weight

# Same as above but limits the search to only exercises with a matching ID
def totalWeightInBlock2(blocks, exerciseID):
    weight = 0
    for block in blocks:
        if block['exercise_id'] == exerciseID:
            for set in block['sets']:
                if set['weight']:
                    weight += int(set['weight'])
    return weight

# Similar to the one above, but finds the biggest weight instead of adding them together
def mostWeightInRepBlock(blocks, exerciseID):
    weight = 0
    
    for block in blocks:
        if block['exercise_id'] == exerciseID:
            for set in block['sets']:
                if set['weight'] and int(set['weight'] > weight):
                    weight = int(set['weight'])
    return weight
  
#---------------------------------------------------------------------
#question funtions 

#Goes through workouts.json and adds every weight in existence
def q1():
    pounds = 0
    for workout in workouts:
        pounds += totalWeightInBlock(workout['blocks'])
    return pounds        



def q2():
    userID = findUserID('Barry', 'Moore')
    pounds = 0  
    
    #Goes through workouts.json and filters the search by the user and year
    for workout in workouts:
        if workout['user_id'] == userID and '2016' in workout['datetime_completed']:       
        #Then adds every weight found into pounds
            pounds += totalWeightInBlock(workout['blocks'])
    
    return pounds



def q3():
    exerciseID = findExerciseID("Back Squat")
    userID = findUserID('Barry', 'Moore')
    mostWeight = 0
    mostDate = 'date'
    
    for workout in workouts:
        #Goes through workouts.json and filters the search by the user and year
        if workout['user_id'] == userID and '2017' in workout['datetime_completed']:
            currentWeight = totalWeightInBlock2(workout['blocks'], exerciseID)
            #Then compares mostWeight with currentWeight to see which is higher
            #In order Assigns both currentWeight and the currentTime to mostWeight and mostDate respectively
            if currentWeight > mostWeight:
                mostWeight = currentWeight
                mostDate = workout['datetime_completed']
    
    # Converts mostDate into datetime, then gets converted again to only display the month
    return datetime.strptime(mostDate, '%Y-%m-%d %H:%M:%S').strftime('%B')
    
    
                
def q4():
    exerciseID = findExerciseID("Bench Press")
    userID = findUserID('Abby', 'Smith')
    mostWeight = 0
    
    for workout in workouts:
        #Goes through workouts.json and filters the search by the user
        if workout['user_id'] == userID:
            currentWeight = mostWeightInRepBlock(workout['blocks'], exerciseID)
            #Compares currentWight and mostWeight and assigns it if it's bigger
            if currentWeight > mostWeight:
                mostWeight = currentWeight
    
    return mostWeight
    
q4()


# Collect answers
answers = {
    # In total, how many pounds have these athletes Bench Pressed?
    'q1': q1(),

    # How many pounds did Barry Moore Back Squat in 2016?
    'q2': q2(),

    # In what month of 2017 did Barry Moore Back Squat the most total weight?
    'q3': q3(),

    # What is Abby Smith's Bench Press PR weight?
    # PR defined as the most the person has ever lifted for that exercise, regardless of reps performed.
    'q4': q4()
}

print(json.dumps(answers))