def course_details(course_num):
    # Prints course details based on course number if course exists
    room_number = {
        'CSC101': 3004, 
        'CSC102': 4501, 
        'CSC103': 6755, 
        'NET110': 1244, 
        'COM241': 1411
    }
    instructors = {
        'CSC101': 'Haynes',
        'CSC102': 'Alvarado',
        'CSC103': 'Rich',
        'NET110': 'Burke',
        'COM241': 'Lee'
    }
    meeting_times = {
        'CSC101': '8:00 a.m.',
        'CSC102': '9:00 a.m.',
        'CSC103': '10:00 a.m.',
        'NET110': '11:00 a.m.',
        'COM241': '1:00 p.m.'
    }

    if course_num in room_number:
        # print formatted string with course details if course_num exists
        print(f"Course {course_num} is in room number {room_number[course_num]}, instructed by {instructors[course_num]}, meeting at {meeting_times[course_num]}")
    else:
        print("Course not found.")


if __name__ == "__main__":
    course_num = input("Enter course number: ")
    course_details(course_num = course_num )
