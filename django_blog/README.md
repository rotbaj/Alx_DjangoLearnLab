Authentication Workflow
Registration
URL: /register/

View: blog.views.register

Template: blog/templates/blog/register.html

Form: blog.forms.RegisterForm (extends UserCreationForm to include an email field).

Process:

Users fill out the registration form with their username, email, and password.

Upon successful registration, users are logged in and redirected to the home page.

Login
URL: /login/

View: Django's built-in LoginView

Template: blog/templates/blog/login.html

Process:

Users enter their username and password.

Upon successful login, users are redirected to the home page.

Logout
URL: /logout/

View: Django's built-in LogoutView

Process:

Users are logged out and redirected to the home page.

Profile Management
View Profile:

URL: /profile/

View: blog.views.profile

Template: blog/templates/blog/profile.html

Process: Displays the user's profile information (username and email).

Edit Profile:

URL: /edit_profile/

View: blog.views.edit_profile

Template: blog/templates/blog/edit_profile.html

Process: Allows users to update their email.
