Welcome to the Quiz Application Project! This is a simple but powerful command-line quiz system written in Python. It's designed to manage users, run quiz sessions, and track scores, offering a complete interactive quiz experience right from your terminal.

FEATURES

Dynamic Quiz Sessions: The application can run a quiz, present questions to the user, and evaluate the answers in real-time.

User Profile Management: It creates and manages user profiles, keeping track of individual scores and progress.

Scoring System: Automatically calculates and updates the user's score based on their answers during the quiz.

Modular Codebase: The project is cleanly organized into modules for the quiz engine, user profiles, and utility functions, making it easy to understand and extend.

HOW TO USE

To run the quiz application, simply execute the main script from your terminal. This will start the program, prompt for a username, and begin the quiz session.

python main.py

FILE DESCRIPTIONS

main.py
This is the main entry point of the application. It handles the overall program flow, bringing together the user profile and quiz engine modules to run the quiz.

quiz_engine.py
This file contains the core logic for the quiz itself. It is responsible for managing the questions, checking the user's answers, and calculating the score for a quiz session.

user_profile.py
This module manages all user-related data. It handles creating new user profiles, loading existing ones, and saving the user's score and other relevant information.

utils.py
This is a utility script that contains helper functions used by the other modules in the project. This could include functions for clearing the screen, formatting text, or other shared tasks.