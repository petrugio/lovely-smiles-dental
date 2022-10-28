#### Landing page (Homepage)

- When clicking or opening the website link [https://lovely-smiles-dental.herokuapp.com/](https://lovely-smiles-dental.herokuapp.com/) the homepage loads.

    Expected:
    
    The page loads without any errors
    
    Actual:
    
    The page loads without any errors
    
- When clicking on the 'Make Appointment' button in the jumbotron.

    Expected:
    
    The Make Appointment page loads without any errors if user logged in
    
    The Login page loads without any errors if user not logged in
    
    Actual:
    
    The Make Appointment page loads without any errors if user logged in
    
    The Login page loads without any errors if user not logged in
    
- When clicking on any item from contact list.
     
     Expected:
     
     The item clicked opens specific app
     
     Phone number -> opens Phone App
     
     Email -> opens Email App
     
     Address -> opens Maps App
     
     Actual:
     
     The item clicked opens specific app
     
     Phone number -> opens Phone App
     
     Email -> opens Email App
     
     Address -> opens Maps App


- When clicking on Mini Map.
    
    Expected:
    
    Google maps opens up in a new tab with location selected  
    
    Actual:
    
    Google maps opens up in a new tab with location selected

### Navigation

 - When clicking on the navigation links as a guest (not logged in).
   
   Expected:
   
   Home - opens Homepage
   
   Services - opens Services page
   
   Appointments - opens Login page
   
   Register - opens Register page
   
   Login - opens Login page
   
   Actual:
   
   Home - opens Homepage
   
   Services - opens Services page
   
   Appointments - opens Login page
   
   Register - opens Register page
   
   Login - opens Login page
  
 - When clicking on the navigation links as a logged in user or staff.
 
   Expected:
   
   Home - opens Homepage
   
   Services - opens Services page
   
   Appointments - opens Login page
   
   Make Appointment - opens Make Appointment page
   
   Logout - opens Logout page
   
   Actual:
   
   Home - opens Homepage
   
   Services - opens Services page
   
   Appointments - opens Login page
   
   Make Appointment - opens Make Appointment page
   
   Logout - opens Logout page

### Footer

- When clicking on the social media navigation links in the footer.

   Expected:
   
   Github icon - opens project Github repository page in a new tab
   
   Linkedin icon - opens authors Linkedin page in a new tab
   
   Actual:
   
   Github icon - opens project Github repository page in a new tab
   
   Linkedin icon - opens authors Linkedin page in a new tab
   
### Services page

 - When landing on the page.
 
   Expected:

   The page loads without any errors

   Actual:
   
   The page loads without any errors

- When clicking on the 'Book' button beside each service.

    Expected:
    
    The Make Appointment page loads without any errors if user logged in
    
    The Login page loads without any errors if user not logged in
    
    Actual:
    
    The Make Appointment page loads without any errors if user logged in
    
    The Login page loads without any errors if user not logged in   
   
### Make Appointment page

- When landing on the page.
 
   Expected:

   The page loads without any errors

   Actual:
   
   The page loads without any errors
   
- When make appointment form  is successfully submitted.
 
   Expected:

   Appointment gets created and logged in user gets redirected to Appointments Page 

   Actual:
   
   Appointment gets created and logged in user gets redirected to Appointments Page 
   
- When make appointment form is unsuccessfully submitted.
   
   Expected:

   A feedback message is displayed pointing to which field contains errors or empty 

   Actual:
   
   A feedback message is displayed pointing to which field contains errors or empty
   
### Appointments page

- When landing on the page.
 
   Expected:

   The page loads without any errors
   
   Upcoming appointments up until today displayed if standard user
   
   Upcoming appointments up until today and up to 5 days in the past displayed if staff user
   
   Actual:
   
   The page loads without any errors
   
   Upcoming appointments up until today displayed if standard user
   
   Upcoming appointments up until today and up to 5 days in the past displayed if staff user
   
- When clicking on the 'Edit' button

   Expected:

   Edit Appointment page loads without any errors
   
   Actual: 

   Edit Appointment page loads without any errors

- When clicking on the 'Delete' button

   Expected:

   Confirm Appointment Deletion page loads without any errors
   
   Actual: 

   Confirm Appointment Deletion loads without any errors
   
### Edit Appointment page   
   
- When Edit Appointment form  is successfully submitted.
 
   Expected:

   Appointment gets updated and logged in user gets redirected to Appointments Page 

   Actual:
   
   Appointment gets updated and logged in user gets redirected to Appointments Page 
   
- When Edit Appointment form is unsuccessfully submitted.
   
   Expected:

   A feedback message is displayed pointing to which field contains errors or empty 

   Actual:
   
   A feedback message is displayed pointing to which field contains errors or empty
   
### Confirm Appointment Deletion page 

- When clicking on the 'Confirm' bellow the appointment.

   Expected:

   Appointment gets deleted and logged in user gets redirected to Appointments Page 
   
   A feedback message is displayed

   Actual:
   
   Appointment gets deleted and logged in user gets redirected to Appointments Page 
   
   A feedback message is displayed
   
### Login page

- When Login form is successfully submitted.
 
   Expected:

   User gets redirected to Services Page 
   
   A feedback message is displayed

   Actual:
   
   User gets redirected to Services Page 
   
   A feedback message is displayed   
   
- When Login form is unsuccessfully submitted.
   
   Expected:

   A feedback message is displayed pointing to which field contains errors or empty 
   
   Actual:
   
   A feedback message is displayed pointing to which field contains errors or empty

### Logout page

- When clicking on the 'Sign Out' button.

   Expected:

   Logged in user gets logout and redirected to Homepage 
   
   A feedback message is displayed

   Actual:
   
   Logged in user gets logout and redirected to Homepage 
   
   A feedback message is displayed

### 404 page

- When user has incorrectly typed the website address 
  
   Expected:

   User gets redirected to 404 page where he/she may press "Home" button to return to the Homepage

   Actual:
   
   User gets redirected to 404 page where he/she may press "Home" button to return to the Homepage 
   
### 403 page

- When user is trying to access unauthorized page
  
   Expected:

   User gets redirected to 403 page where he/she may press "Home" button to return to the Homepage

   Actual:
   
   User gets redirected to 403 page where he/she may press "Home" button to return to the Homepage
   
   
### 500 page

- When there is an internal server error
  
   Expected:

   User gets redirected to 500 page where he/she may press "Home" button to return to the Homepage

   Actual:
   
   User gets redirected to 500 page where he/she may press "Home" button to return to the Homepage

Back to [README.md](README.md)