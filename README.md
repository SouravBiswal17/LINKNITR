# LINKNITR
This is a full-stake project 
NITR Referral Network Platform
Overview
The NITR Referral Network Platform is a Django-based web application designed to facilitate internship referrals for students at NITR (National Institute of Technology, Rourkela). The platform leverages the NITR community network to enhance internship opportunities through a referral system.

Features
Referral-Focused Platform: Exclusively for internship referrals, avoiding unrelated content.
Student Profiles: Students can create profiles with a CV score indicating their skill level.
Alumni Interaction: Alumni can browse student profiles and provide referrals based on CV scores and profile details.
NITR Community Integration: Utilizes the NITR network to connect students and alumni effectively.
Technologies Used
Backend: Django
Frontend: HTML, CSS, JavaScript
Database: SQLite
Getting Started
Prerequisites
Python 3.x
Django 4.x (or the version specified)
[Database Setup if required]
Installation
Clone the Repository:

Open VSCode and open the terminal (`Ctrl + ``):

bash
Copy code
git clone https://github.com/your-username/nitr-referral-network.git
cd nitr-referral-network
Create a Virtual Environment:

In the VSCode terminal, run:

bash
Copy code
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
Install Dependencies:

Make sure you have requirements.txt in your project directory. Install the dependencies with:

bash
Copy code
pip install -r requirements.txt
Apply Migrations:

Run the following command to apply database migrations:

bash
Copy code
python manage.py migrate
Create a Superuser:

Create a superuser for accessing the Django admin panel:

bash
Copy code
python manage.py createsuperuser
Run the Development Server:

Start the development server with:

bash
Copy code
python manage.py runserver
Access the Application:

Open your browser and navigate to http://127.0.0.1:8000/ to view the application.

Usage
Student Registration:

Go to the registration page and create a student profile.
Upload your CV, and a CV score will be generated based on your skills.
Alumni Interaction:

Register as an alumni and browse student profiles.
Provide referrals based on CV scores and profile details.
Contributing
To contribute to the project:

Fork the Repository

Create a Feature Branch

bash
Copy code
git checkout -b feature/new-feature
Make Your Changes in VSCode.

Commit Your Changes

bash
Copy code
git commit -m 'Add new feature'
Push to the Branch

bash
Copy code
git push origin feature/new-feature
Create a Pull Request on GitHub.

License
This project is licensed under the MIT License.

Contact
Project Maintainers:

Hackin Pirates :- 

1. Akshay Cohoudhary
2. Sourav Biswal
3. Jayesh Verma
4. Yug Agrawal

Website: [Project Website URL]
