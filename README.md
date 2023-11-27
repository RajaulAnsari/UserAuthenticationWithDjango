# Django User Authentication

This repository demonstrates how to implement user authentication in a Django web application using the built-in authentication system.

## Getting Started

1. Clone the repository:

   ```
   git clone https://github.com/RajaulAnsari/DjangoUserLoginAuth.git
   
2. Navigate to the project directory:

   ```
   cd DjangoUserLoginAuth

3. Create a virtual environment (optional but recommended):

   ```
   python -m venv venv

4. Activate the virtual environment:
    * On Windows:
      ```
      venv\Scripts\activate

     * On macOs/Linux
       ```
       source venv/bin/activate

5. Install dependencies:

   ```
   pip install django

6. Apply database migrations:

   ```
   python manage.py migrate

7. Create a superuser (admin) account:

   ```
   python manage.py createsuperuser

  Follow the prompts to create an admin account.

8. Run the development server:

   ```
   python manage.py runserver

  The application will be accessible at http://127.0.0.1:8000/.

## Features

  * User registration
  * User login
  * User profile

## Usage

  * Navigate to the registration page at http://127.0.0.1:8000/create/ to create a new account.
  * Log in at http://127.0.0.1:8000/login/ with your credentials.
  * Visit your admin pannel at http://127.0.0.1:8000/admin/ with your superuser credentials to view and update your profile information.

## Contact

If you have any questions or need further assistance, you can contact the repository owner [here](mailto:ansarimdrajaul2@gmail.com).

*Note: You can modify your code as needed...*

## Thanks For Your Interest
