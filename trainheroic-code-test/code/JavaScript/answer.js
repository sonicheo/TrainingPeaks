answers = {
    // In total, how many pounds have these athletes Bench Pressed?
    "q1": null,

    // How many pounds did Barry Moore Back Squat in 2016?
    "q2": null,

    // In what month of 2017 did Barry Moore Back Squat the most total weight?
    "q3": null,

    // What is Abby Smith's Bench Press PR weight?
    // PR defined as the most the person has ever lifted for that exercise, regardless of reps performed.
    "q4": null
}


// Load data
var fs = require("fs");
var fileContentsUsers = fs.readFileSync("./../../data/users.json");
var fileContentsExercises = fs.readFileSync("./../../data/exercises.json");
var fileContentsWorkouts = fs.readFileSync("./../../data/workouts.json");
var users = JSON.parse(fileContentsUsers);
var exercises = JSON.parse(fileContentsExercises);
var workouts = JSON.parse(fileContentsWorkouts);


// Candidate TODO: Write code to answer questions


// Output answers
console.log(JSON.stringify(answers));