# This code is a simple registration system for a platform that offers various courses based on age and gender. It prompts the user for their name, age, and gender, and then allows them to enroll in courses based on their eligibility. The courses are categorized into sports, technology, cooking, arts, and music, with different options
name=input("enter your name")
print("welcome",name)
age=int(input("enter your age"))
print("your age is",age)
sex=str(input("enter your gender"))
print("your gender is",sex)
# The code checks the user's gender and age to determine which courses they are eligible for. It then prompts the user to choose a course and enroll for a specific duration. If the user is not eligible for any courses based on their age
senior_courses=("Basketball", "football", "AI", "machine learning", "Cuisine", "Baking", "Cuisine")
senior_time=("3 years") 
junior_courses=("Music Producing", "Instrumentals", "Singing", "Painting", "Drawing","None")
junior_time="1 year"

if (sex=="male" or sex=="female") and age>18:
     print("You are eligible for the following courses:", senior_courses)
elif (sex=="male" or sex=="female") and age<=18:
     print("You are eligible for the following courses:", junior_courses)
else:
     print("Sorry, you are not eligible for any courses based on your age.");exit()
course_choice=input("Enter the course you want to enroll in:")
if course_choice in senior_courses and age>18:
     print("You have successfully enrolled in", course_choice, "for", senior_time)
elif course_choice in junior_courses and age<=18:
     print("You have successfully enrolled in", course_choice, "for", junior_time)
else:     print("Sorry, you are not eligible to enroll in this course based on your age.")





