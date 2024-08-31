### Pseudocode

1. **Initialize Dictionaries**
   - Create a dictionary `room_numbers` with course numbers as keys and room numbers as values.
   - Create a dictionary `instructors` with course numbers as keys and instructor names as values.
   - Create a dictionary `meeting_times` with course numbers as keys and meeting times as values.

2. **Prompt User for Input**
   - Display a message asking the user to enter a course number.
   - Read the user input and store it in a variable `course_number`.

3. **Retrieve and Display Course Details**
   - Check if `course_number` exists in the `room_numbers` dictionary.
     - If it exists:
       - Retrieve and print the room number from `room_numbers` using `course_number` as the key.
       - Retrieve and print the instructor name from `instructors` using `course_number` as the key.
       - Retrieve and print the meeting time from `meeting_times` using `course_number` as the key.
     - If it does not exist:
       - Print a message indicating that the course number was not found.