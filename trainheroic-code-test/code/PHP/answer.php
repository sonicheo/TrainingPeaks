<?php

// Collect answers
$answers = [
    // In total, how many pounds have these athletes Bench Pressed?
    'q1' => null,

    // How many pounds did Barry Moore Back Squat in 2016?
    'q2' => null,

    // In what month of 2017 did Barry Moore Back Squat the most total weight?
    'q3' => null,

    // What is Abby Smith's Bench Press PR weight?
    // PR defined as the most the person has ever lifted for that exercise, regardless of reps performed.
    'q4' => null,
];

// Load data
$users = json_decode(file_get_contents(__DIR__ . '/../../data/users.json'));
$exercises = json_decode(file_get_contents(__DIR__ . '/../../data/exercises.json'));
$workouts = json_decode(file_get_contents(__DIR__ . '/../../data/workouts.json'));

// Candidate TODO: Write code to answer questions

// Output answers
echo json_encode($answers);
