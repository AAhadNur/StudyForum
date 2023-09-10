<div align="center">
# StudyForum - Online Study Community
</div>

Welcome to StudyForum, your go-to platform for creating and participating in study rooms on various topics. This web application is built using Django and provides a secure and feature-rich environment for users to collaborate, discuss, and learn together.

## Features

- **User Authentication and Authorization:** Secure user registration and login system with role-based authorization to ensure the privacy and security of your study rooms.

- **Create Study Rooms:** Users can create study rooms for specific topics, subjects, or courses. Each room has its own discussion board and chat functionality.

- **Room Discussions:** Engage in meaningful discussions with fellow students and experts in each study room. Share knowledge, ask questions, and provide answers.

- **Profile Management:** Customize your user profile, upload avatars, and showcase your expertise and interests.

### App Preview :

<table width="100%"> 
<tr>
<td width="50%">      
&nbsp; 
<br>
<p align="center">
  Feed Home
</p>
<img src="https://github.com/AAhadNur/StudyForum/blob/main/static/images/SF-frontpage.png">
</td> 
<td width="50%">
<br>
<p align="center">
  Room Preview
</p>
<img src="https://github.com/AAhadNur/StudyForum/blob/main/static/images/SF-room.png">  
</td>
</table>

## Getting Started

Follow these steps to set up and run StudyForum locally on your machine:

1. **Clone the Repository:**

   ```
   git clone https://github.com/AAhadNur/StudyForum.git
   cd StudyForum
   ```

2. **Install Dependencies:**

   ```
   pip install -r requirements.txt
   ```

3. **Database Setup:**

   - Configure your database settings in `settings.py`.
   - Apply database migrations:

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create Superuser:**

   ```
   python manage.py createsuperuser
   ```

5. **Run the Development Server:**

   ```
   python manage.py runserver
   ```

6. **Access the Application:**
   Open your web browser and go to `http://localhost:8000` to access StudyForum. You can log in with your superuser credentials to start using the application.

## Usage

- Create your study rooms and invite others to join.
- Participate in discussions and share your knowledge.
- Explore user profiles and connect with like-minded learners.
- Enjoy a secure and robust study community experience.

## Contributing

We welcome contributions to make StudyForum even better! Feel free to open issues, suggest new features, or submit pull requests.

## Acknowledgments

- Special thanks to the Django community and all the open-source contributors who make projects like this possible.

---

Thank you for choosing StudyForum!
