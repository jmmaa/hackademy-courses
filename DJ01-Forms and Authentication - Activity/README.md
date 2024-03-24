# DJ01 Forms and Authentication Activities

this is the resulting implementation of the tasks given below

### Create Registration Page
 
Create a view, form and template for Registration

- Form fields include: first name, last name, username, email & password (with repeat password field)
- Set url as `/register`
- Make sure that for every successful registration, there is User object and a Profile object created (as one to one field) - this is done best with the use of signals, but you can also do it through views.

##### EXTRA

- Redirect user to home page after successful registration

### Create Login and Logout page

- Create login & logout view and template, use url '/login' & '/logout' respectively
- Utilize Forms for login information - username and password to login
- After logout, set to redirect to login page.

(hint: you may use views and forms from User Auth system)

### Unit Tests

- Create unit test under tests.py (or tests directory)
- Test whether a Profile is created/existing after successful registration POST method.
- Test whether successful registration redirects correctly to home page.
  (hint: use assertions)
