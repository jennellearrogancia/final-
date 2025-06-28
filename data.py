import random
import string
from datetime import datetime, timedelta

faculty_names = [
    "Manuquil, Rommel D.",
    "Marquez, Jonathan A.",
    "Antone, Marijoy Q.",
    "Bulawan, Darwin Kim Q.",
    "Pera, Angelo P.",
    "Penaflorida, Jhunel B.",
    "Camino, Honesto O.",
    "Pescadero, Don Lenard E.",
    "Ragudo, Angelito S.",
]

pup_directors = [
    "Dr. Manuel M. Muhi",
    "Dr. Emanuel C. De Guzman",
    "Dr. Jerielyn V. Reyes",
    "Dr. Mark Christian Catapang",
    "Dr. Mary Grace T. Cabrido",
]

pup_positions = [
    "University President",
    "Vice President for Academic Affairs",
    "Vice President for Administration",
    "Registrar",
    "Director of Student Affairs",
    "Director of Research",
    "Department Chair",
    "Program Coordinator",
    "Faculty Member",
    "Guidance Counselor",
]

fields_of_expertise = [
    "Computer Science",
    "Business Administration",
    "Education",
    "Information Technology",
    "Marketing",
    "Finance",
    "Hospitality Management",
    "Environmental Science",
    "Graphic Design",
    "Architecture",
]

complete_addresses = [
    "909 Taft Avenue, Manila, Metro Manila",
    "1001 Aurora Boulevard, San Juan, Metro Manila",
    "1112 España Boulevard, Sampaloc, Manila, Metro Manila",
    "1213 Ortigas Avenue, Mandaluyong City, Metro Manila",
    "1314 Roxas Boulevard, Pasay City, Metro Manila",
    "1415 Katipunan Avenue, Quezon City, Metro Manila",
    "1516 Shaw Boulevard, Mandaluyong City, Metro Manila",
    "1617 Commonwealth Avenue, Quezon City, Metro Manila",
    "1718 Marcos Highway, Marikina City, Metro Manila",
    "1819 A. Mabini Street, Malate, Manila, Metro Manila",
]

real_subjects = [
    "Professional Ethics",
    "Data Structures",
    "Software Engineering",
    "Database Management Systems",
    "Operating Systems",
    "Web Development",
    "Network Security",
    "Human-Computer Interaction",
    "Project Management",
    "Research",
]

short_days = {
    "Monday": "Mon",
    "Tuesday": "Tue",
    "Wednesday": "Wed",
    "Thursday": "TH",
    "Friday": "Fri",
    "Saturday": "Sat"
}

def random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def random_number(length):
    return ''.join(random.choice(string.digits) for i in range(length))

def generate_email(full_name):
    first_name = full_name.split(", ")[1].split(" ")[0].lower()
    return f"{first_name}@gmail.com"

def specific_date():
    return "26-06-2025"

def generate_time_range():
    start_hour = random.randint(8, 20) 
    start_minute = random.choice([0, 30])
    start_time = datetime.strptime(f"{start_hour}:{start_minute}", "%H:%M")
    end_time = start_time + timedelta(hours=3)
    return f"{start_time.strftime('%I:%M %p')} - {end_time.strftime('%I:%M %p')}"
