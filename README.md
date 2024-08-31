# LINKNITR
This is a full-stake project 

NITR Referral Network Platform
Overview
The NITR Referral Network Platform is a web application designed to streamline the process of securing internship referrals for students at NITR (National Institute of Technology, Rourkela). The platform focuses exclusively on facilitating referrals between students and alumni, leveraging the NITR community network to maximize opportunities for students.

Features
Referral-Focused Platform: Exclusively designed for internship referrals, avoiding unrelated content.
Student Profiles: Students can create profiles showcasing their skills and receive a CV score to indicate their skill level.
Alumni Interaction: Alumni can browse student profiles and provide referrals based on the CV score and profile details.
NITR Community Integration: Utilizes the strong NITR network to connect students with alumni.
Technologies Used
Backend: Django
Frontend: HTML, CSS (Bootstrap), JavaScript
Database: [Specify Database if needed, e.g., PostgreSQL, SQLite]
Getting Started
Prerequisites
Python 3.x
Django 4.x (or the version specified)
[Database Setup if required]
Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/nitr-referral-network.git
cd nitr-referral-network
Create a Virtual Environment:

bash
Copy code
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Apply Migrations:

bash
Copy code
python manage.py migrate
Create a Superuser:

bash
Copy code
python manage.py createsuperuser
Run the Development Server:

bash
Copy code
python manage.py runserver
Access the Application:

Open your browser and go to http://127.0.0.1:8000/ to view the application.

Usage
Student Registration:

Navigate to the registration page and create a student profile.
Upload your CV and receive a CV score based on your skills.
Alumni Interaction:

Register as an alumni and browse student profiles.
Provide referrals based on the CV score and profile details.
Contributing
Fork the Repository

Create a Feature Branch

bash
Copy code
git checkout -b feature/new-feature
Commit Your Changes

bash
Copy code
git commit -m 'Add new feature'
Push to the Branch

bash
Copy code
git push origin feature/new-feature
Create a Pull Request

License
This project is licensed under the MIT License.

Contact
Project Maintainers:

[Your Name] - [Your Email]
[Team Members' Names and Emails]
Website: [Project Website URL]