import streamlit as st

# Complete quiz data
quiz_data = [
    {
        "question": "What is the time complexity of a binary search algorithm?",
        "options": ["O(n)", "O(log n)", "O(n^2)", "O(1)"],
        "answer": 1  # Index of the correct option
    },
    {
        "question": "Which data structure is used for implementing recursion?",
        "options": ["Queue", "Stack", "Array", "Linked List"],
        "answer": 1
    },
    {
        "question": "What does the term 'polymorphism' mean in Object-Oriented Programming?",
        "options": [
            "Many forms of a single entity",
            "Multiple classes in one program",
            "Encapsulation of data",
            "Inheritance of classes"
        ],
        "answer": 0
    },
    {
        "question": "What is the default value of a boolean variable in Java?",
        "options": ["true", "false", "0", "undefined"],
        "answer": 1
    },
    {
        "question": "Which sorting algorithm has the best average-case time complexity?",
        "options": ["Bubble Sort", "Insertion Sort", "Quick Sort", "Merge Sort"],
        "answer": 3
    },
    {
        "question": "In Python, what will len(\"hello\"[1:3]) return?",
        "options": ["1", "2", "3", "4"],
        "answer": 1
    },
    {
        "question": "Which of the following is a valid way to declare a tuple in Python?",
        "options": ["[1, 2, 3]", "(1, 2, 3)", "{1, 2, 3}", "None of the above"],
        "answer": 1
    },
    {
        "question": "In C++, which operator is used to allocate memory dynamically?",
        "options": ["malloc", "calloc", "new", "delete"],
        "answer": 2
    },
    {
        "question": "Which of the following is not a valid SQL command?",
        "options": ["SELECT", "JOIN", "DELETE", "FETCH_ALL"],
        "answer": 3
    },
    {
        "question": "What is the technique of hiding implementation details called?",
        "options": ["Abstraction", "Encapsulation", "Polymorphism", "Inheritance"],
        "answer": 1
    },
    {
        "question": "What is the keyword in Python to define a function?",
        "options": ["function", "def", "func", "lambda"],
        "answer": 1
    },
    {
        "question": "Which command is used to clone a repository in Git?",
        "options": ["git pull", "git push", "git clone", "git fork"],
        "answer": 2
    },
    {
        "question": "What is the process of finding and fixing errors in a program called?",
        "options": ["Debugging", "Testing", "Compiling", "Refactoring"],
        "answer": 0
    },
    {
        "question": "Which HTTP method is used to update resources on a server?",
        "options": ["GET", "POST", "PUT", "DELETE"],
        "answer": 2
    },
    {
        "question": "What is the value of 5 % 2 in most programming languages?",
        "options": ["0", "1", "2", "5"],
        "answer": 1
    },
    {
        "question": "What is the term for a variable that is accessible only inside the function where it is declared?",
        "options": ["Global", "Local", "Static", "Constant"],
        "answer": 1
    },
    {
        "question": "What is the method name in Python to convert a string to lowercase?",
        "options": ["toLowerCase", "lower", "convertLower", "downcase"],
        "answer": 1
    },
    {
        "question": "Which programming paradigm is based on the concept of 'objects'?",
        "options": ["Functional Programming", "Object-Oriented Programming", "Procedural Programming", "Event-Driven Programming"],
        "answer": 1
    },
    {
        "question": "What is the structure called that holds multiple elements but only allows access in a LIFO manner?",
        "options": ["Queue", "Stack", "Array", "HashMap"],
        "answer": 1
    },
    {
        "question": "What is the output of the expression 3 + 4 * 2 in most programming languages?",
        "options": ["14", "11", "10", "7"],
        "answer": 1
    },
]

# Initialize session state variables
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = False

# Display the quiz
st.title("Programming Quiz")
st.write("Test your programming knowledge! Answer the questions below:")

current_question = st.session_state.current_question
question_data = quiz_data[current_question]

# Display question
st.subheader(f"Question {current_question + 1}: {question_data['question']}")

# Display options as radio buttons
selected_option = st.radio("Choose your answer:", question_data["options"], key=f"question_{current_question}")

# Feedback and move to next question
if st.session_state.answered:
    if selected_option == question_data["options"][question_data["answer"]]:
        st.success("Correct! 🎉")
        st.session_state.score += 1
    else:
        st.error(f"Incorrect! The correct answer is: {question_data['options'][question_data['answer']]}")

    # Move to the next question after feedback
    if current_question + 1 < len(quiz_data):
        st.session_state.current_question += 1
    else:
        st.write(f"🎓 **Quiz Finished!** Your final score is **{st.session_state.score}/{len(quiz_data)}**.")
        st.stop()

# "Next" button to allow moving to the next question
if st.button("Next"):
    st.session_state.answered = True
