<h1 align="center">Lovely Smiles Dental</h1>

<a href="https://lovely-smiles-dental.herokuapp.com/" target="_blank" rel="noopener" alt="Lovely Smiles Dental, click here to open the website"><img src="documentation/features/responsive.jpg" alt="Lovely Smiles Dental" max-height="650px" max-width="1300px"></a>
<hr>
View the repository in GitHub
<a href="https://github.com/petrugio/lovely-smiles-dental" target="_blank" rel="noopener">here</a>

View the live project
<a href="https://lovely-smiles-dental.herokuapp.com/" target="_blank" rel="noopener">here</a>

# Table of Contents

* [User Experience](#user-experience)
   * [Goals](#goals)
   * [Planing](#planning)
   * [Epics and User Stories](#epics-and-user-stories)
* [Features](#features)
* [Design](#design)
    * [Wireframes](#wireframes)
    * [Database](#database)
    * [Fonts](#fonts)
    * [Color Scheme](#color-scheme)
* [Testing](#testing)
    * [Responsive Design](#responsive-design)
    * [Validator Testing](#validator-testing)
        * [HTML5](#html5)
        * [CSS3](#css3)
        * [Lighthouse](#lighthouse)
        * [Accessibility](#accessibility)
    * [Functional Testing ](#functional-testing)
    * [Browser Testing](#browser-testing)
* [Bugs](#bugs)
    * [Fixed Bugs](#fixed-bugs)
    * [Bug fix during testing](#bug-fix-during-testing)
    * [Unfixed Bugs](#unfixed-bugs)
* [Deployment](#deployment)
    * [Version Control](#version-control)
    * [Heroku](#heroku)
    * [How to Clone this repository](#how-to-clone-this-repository)
* [Technologies used](#technologies-used)
* [Credits](#credits)
* [Contact](#contact)
* [Acknowledgments](#acknowledgments)

<hr>

 # User Experience
 
 ## Goals

The goal of this website is to provide information about dental practice services offered, location, contact information also users and staff with the ability to create an account for the purpose of creating, viewing, updating and deleting appointments.


## Planning 

Significant amount of time  was devoted to planing the layout and structure of the agile board.  
Having a meeting by myself and changing the hat from product owner to user and then to developer was decided to use Github projects as a agile tool for the ***Lovely smiles dental*** PP4 project. 
From the time remaining to submit a working project was decided to split the development into 5 iteration each lasting 1 week.

After the project scope was clearly defined, following the process of creating milestones/epics, I added User Stories and Tasks to the Backlog and prioritized them using **M.o.S.C.o.W prioritization technique** and assigned them to the appropriate milestone/epic and iteration.

[Lovely Smiles Dental Github project](https://github.com/users/petrugio/projects/4)


Bellow are screenshots of Agile planing, prioritization and development:

<details>
<summary>Screenshots</summary>
<br>

![Backlog_1](documentation/agile/backlog_1.jpg)
![Backlog](documentation/agile/backlog.jpg)
![Current iteration](documentation/agile/current.jpg)
![Status](documentation/agile/status.jpg)
![Epics](documentation/agile/epics.jpg)
![M.o.S.C.o.W](documentation/agile/moscow.jpg)


<br>
</details> 

## Epics and User Stories

<hr>

## Epic: Create initial Django Setup

 - Tasks: Install Django and dependencies (libraries) #4

    - Install Django
    - Install libraries
    - Create a requirements.txt file
    - Create the project
    - Create the app
    - Make database migration
    - Test locally in the browser to confirm successful Django installation

- Issue: Early deployment to Heroku #5
    
    - Task 1 - Create Heroku app
    - Task 2 - Attach the PosgreSQL database to the Heroku app
    - Task 3 - Prepare environment and settings.py files
    - Task 4 - Add new SECRET_KEY to settings.py and to Heroku
    - Task 5 - Connect PosgreSQL database in the settings.py
    - Task 6 - Make database migration
    - Task 7 - Disable STATIC_ROOT on Heroku by adding DISABLE_COLLECTSTATIC=1 to Config Vars
    - Task 8 - Add Procfile

<hr>


## Epic: Create App and pages

#### USER STORY: Pages

As a **user** I can **view site content** so that **what is the purpose of the site and what benefits it can offer**

**Acceptance Criteria:**

   - 1: Base template for all pages completed
   - 2: If the users have accessed a page that doesn't exist - a 404 error page is displayed 
   - 3: If an internal server error occurs - a 500 error page is displayed  

<hr>


## Epic: Navigation

#### USER STORY: Site navigation

As a **user** I can **navigate to different pages** so that **I can see the content on that page**

**Acceptance Criteria:**
    
   - 1: A functioning navigation menu that takes the user to specific pages when clicked 
   - 2: Menu should be responsive so that it provides an intuitive way of navigating the site regardless of the device used
   - 3: Logo in the top left corner should link back to the homepage

#### USER STORY: Footer and social media

As a **user** I can **find links to social media sites** so that **I can engage with service provider on popular social media sites**

**Acceptance Criteria:**
    
   - 1: A footer with social media icons that takes the user to specific sites when clicked 
   - 2: Footer should be responsive regardless of the device being used
   - 3: Link to the Github page of the developer should be displayed as well

<hr>


## Epic: Pages content

#### USER STORY: Contact information

As a **user** I can **easily find contact information** so that **I can contact the owner if I am interested in the services offered**

**Acceptance Criteria:**

   - 1: Address, email address and phone number should be displayed clearly on the homepage
   - 2: When clicked on mobile each contact option should open in the specific app: 
        
        * Phone number should open in the phone app
        * Email address should open in the mail app
        * Address should open in the map app

#### USER STORY: Specific benefits

As a **user** I can **find specific benefits offered by this particular service provider** so that **receive those benefits**

**Acceptance Criteria:**
   
   - 1: A list of benefits should be displayed on the homepage

#### USER STORY: Services offered

As a **user** I can **find services offered page** so that **I can decide if I need those services**

**Acceptance Criteria:**
   
   - 1: Every service should have a image that is intuitive to the user 
   - 2: Every service should have a short description of the service
   - 3: Every service should have a button that takes the user to the make appointment page

#### USER STORY: Map

As a **user** I can **find service provider on a map** so that **easily find my way to specified address**

**Acceptance Criteria:**
    
   - 1: A minimized map is displayed on the page with address of the service provider populated
   
#### USER STORY: Opening hours  

As a **user** I can **find opening hours for service provider** so that **I can know when to make an appointment**

**Acceptance Criteria:**
    
   - 1: Opening hours for the whole week displayed on the page   
   
<hr>


## Epic: Authentication

#### USER STORY: Registration

As a **user** I can **register an account** so that **I can access the full range of features on the site**

**Acceptance Criteria:**
    
   - 1: User can register an account
   - 2: A login button should be displayed bellow the registration form to take the user to the login page
   - 3: User is redirected to the services page after registration

#### USER STORY: Login and Logout

As a **registered user** I can **login and logout of the site** so that **I can access manage my appointments**

**Acceptance Criteria:**
    
   - 1: User can login and logout of site
   - 2: User is redirected to the services page after login
   - 3: User is redirected to the homepage after logout 
   - 4: When an unregistered user press **Book** or **Make an appointment** buttons - he/she is redirected to the Register page
   - 5: When a logged-in user press the Logout button - a confirmation screen should appear and ask the user to confirm the logout 

<hr>


## Epic: Appointment management

#### USER STORY: Make appointment

As a **logged-in user** I can **make an appointment** so that **I can receive the services offered by the service provider**

**Acceptance Criteria:**
    
   - 1: Only logged-in user can see Make appointment page
   - 2: The form cannot be submitted if the required fields are not correctly completed
   - 3: An appointment cannot be outside of working hours or in the past

#### USER STORY: Manage appointment

As a **logged-in user** I can **manage an appointment (CRUD functionality)** so that **I can receive the services offered by the service provider at a convenient time**

**Acceptance Criteria:**
    
   - 1: Logged-in user can view any appointments he/she made on the Make appointment page in a separate page called Appointments
   - 2: Logged-in user can create, read, update and delete (CRUD functionality) appointments from the appointments page.
  
### USER STORY:  View alerts

As a **user** I can **view alerts and feedback messages** so that **I can be sure when task/action has been completed successfully or not**

**Acceptance Criteria:**
    
   - 1: User can see feedback alerts of successful log-in/out and when performing (CRUD) actions 
   - 2: If the alert does not dismisses by itself, user should be able to close it manually
   
<hr>


## Epic: Testing and Deployment
   
#### USER STORY: Website works as intended

As a **user/logged-in user/admin** I can **use the website for its intended purpose** so that **I accomplish the required task/goal**

**Acceptance Criteria:**
    
   - 1: Website loads quickly (depending on the internet speed) and all pages work as intended
   - 2: Website does not have any errors or images not displaying 
   - 3: All images have **alt** attribute 


#### Issues:
 
 - Issue: Complete all the testing necessary and attempt to correct any errors that may arise
 - Issue: Deploy the website to Heroku
  

<hr>

## Epic: Documentation

#### Issues:
    
   - Issue: Complete readme documentation
<hr>

   
# Features  

### Landing page

[USER STORY: Pages](#user-story-pages)

This page welcomes any potential user. It has a hero image of a woman smiling - hinting to the user that the user may have this as well if he/ she decides to avail of the services offered by this dental practice.
In the center of the page there is a jumbotron with a greeting message and a call to action - to make an appointment (consultation is free).  


<details>
<summary>Screenshots</summary>
<br>

![Home page](documentation/features/home_desk.jpg)
![Home page tablet](documentation/features/home_tab.jpg)
![Home page mobile](documentation/features/home_mob.jpg)

<br>
</details>

#### Navigation menu
[USER STORY: Site navigation](#user-story-site-navigation)

At the top of the page the user can find the navbar. On the left the logo of the practice is displayed. If clicked - takes the user to homepage. And on the right the navigation links. Navigation menu is visible on all pages.
Navigation links change depending if the user is logged in or not:

The navigation links available for guest (not logged in):
  - Home
  - Services
  - Appointments ( the user can see the link but if clicked - the user has to login first in order to see the appointments)
  - Register 
  - Login
  
<details>
<summary>Screenshots</summary>
<br>

![Nav guest](documentation/features/nav_outside.jpg)

<br>
</details>  


 The navigation links available for logged in users and staff:
  - Home
  - Services
  - Appointments 
  - Make Appointment
  - Logout
 
<details>
<summary>Screenshots</summary>
<br>

![Nav logged in user](documentation/features/nav_inside.jpg)

<br>
</details>

#### Contact details
[USER STORY: Contact information](#user-story-contact-information)

Bellow the jumbotron the user can see contact details: email, phone and address.
If the user press any of them he/she will be redirected to specific app (both on desktop or mobile):
   - Phone number -> Phone App
   - Email -> Email App
   - Address -> Maps App

<details>
<summary>Screenshots</summary>
<br>

![Contact](documentation/features/contact.jpg)

<br>
</details>

#### Specific Benefits
[USER STORY: Specific benefits](#user-story-specific-benefits)

Below the contact section the user can find Specific Benefits section. The user may decide to avail of these benefits if making an appointment.

<details>
<summary>Screenshots</summary>
<br>

![Benefits](documentation/features/benefit.jpg)

<br>
</details>

#### Map and opening hours
[USER STORY: Map](#user-story-map)

[USER STORY: Opening hours](#user-story-opening-hours)

A mini-map with dental practice location and a table with opening hours is displayed in the homepage.

<details>
<summary>Screenshots</summary>
<br>

![Map and opening hours](documentation/features/map_hours.jpg)

<br>
</details>

#### Footer
[USER STORY: Footer and social media](#user-story-footer-and-social-media)

And lastly in the bottom of the page ( footer) the user can see who developed this site and find different social links of the developer. Footer is visible on all pages.

<details>
<summary>Screenshots</summary>
<br>

![Footer](documentation/features/footer.jpg)

<br>
</details>


### Services page
[USER STORY: Services offered](#user-story-services-offered)

On the services page the user can find out more information about services offered by the dental practice. Each service offered has a short description an image associated with that service and a button that takes the user to the Make Appointment page.
Services are available as an drop down option when making an appointment.
All services are:
   - Consultation
   - Bridges
   - Crowns
   - Fillings
   - Root canal treatment
   - Scale and polish
   - Braces
   - Wisdom tooth removal
   - Dental implants
   - Dentures or false teeth
   - Teeth whitening
   - Dental veneers

  

<details>
<summary>Screenshots</summary>
<br>

![Services page](documentation/features/services_desk.jpg)
![Services tablet](documentation/features/services_tab.jpg)
![Services mobile](documentation/features/services_mob.jpg)

<br>
</details>


### Register Page
[USER STORY: Registration](#user-story-registration)

Due to the fact that this is a demo website, I decided to go for a simpler registration process. 
Registration is handled by Django library Allauth and it is done using username and password. Email is optional and back-end functionality to receive emails was not activated.


<details>
<summary>Screenshots</summary>
<br>

![Register page](documentation/features/register_desk.jpg)
![Register tablet](documentation/features/register_tab.jpg)
![Register mobile](documentation/features/register_mob.jpg)

<br>
</details>

Upon successful registration user is redirected to services page.

<details>
<summary>Screenshots</summary>
<br>

![Registered](documentation/features/registered.jpg)


<br>
</details>

### Login Page
[USER STORY: Login and Logout](#user-story-login-and-logout)

Login page requires username and password that were selected/provided during registration.
Upon successful registration user is redirected to services page. 
If the user pressed Appointments link in the Navigation menu prior to be logged in or registered -
the user will be redirected to the appointments page after successful registration or sign in.

<details>
<summary>Screenshots</summary>
<br>

![Login page](documentation/features/sign_in_desk.jpg)
![Login tablet](documentation/features/sign_in_tab.jpg)
![Login mobile](documentation/features/sign_in_mob.jpg)

<br>
</details>

### Make Appointments Page
[USER STORY: Make appointment](#user-story-make-appointment)

Make Appointments Page can be view by a logged in user. Here the user can make an appointment that he/she may need. 
Placeholders are in place to aid the user in filling out the form correctly.
Form validation is in place for each input option.

The user is presented with a form that takes some basic information:
 - Patient name - max 45 caracters
 - Phone number - uses django-phonenumber-field library for validation
 - Dentist - a drop-down menu of dentists, by default Dr. Becket
 - Service - a drop-down menu of services, by default Consultation
 - Date - uses bootstrap_datepicker_plus library to enter the date
 - Time - uses bootstrap_datepicker_plus library to enter the time

<details>
<summary>Screenshots</summary>
<br>

![Make Appointments page](documentation/features/make_desk.jpg)
![Make Appointments tablet](documentation/features/make_tab.jpg)
![Make Appointments mobile](documentation/features/make_mob.jpg)


<br>
</details>    

### Appointments Page 
[USER STORY: Manage appointment](#user-story-manage-appointment)

Appointments Page can be view by a logged in user. Here the user can see the upcoming appointments that he/she may have. The user can see the appointment up until present day, if the appointment is past due the user cannot longer see it.


<details>
<summary>Screenshots</summary>
<br>

![Appointments page](documentation/features/app_desk.jpg)
![Appointments tablet](documentation/features/app_tab.jpg)
![Appointments mobile](documentation/features/app_mob.jpg)


<br>
</details>    

A user with staff status (which can be assigned to any registered user from the Django Admin panel) can see future appointments for all users and also can see past due appointments up to 5 days in the past for the purpose of editing or deleting them.

<details>
<summary>Screenshots</summary>
<br>

![Staff assign](documentation/features/staff_assign.jpg)
![Staff view](documentation/features/staff_view.jpg)
![Staff confirm](documentation/features/staff_confirm.jpg)
![Staff delete](documentation/features/staff_delete.jpg)

<br>
</details>      

### Feedback messages
[USER STORY: View alerts](#user-story--view-alerts)

A feedback message is displayed for 2 seconds at the top of the page to let the user know that action was successful. 
If for any reason the javascript code will not work and feedback message does not dismiss automatically then the user can manually disable the message by pressing the X button on the right side of the message.

Feedback messages that disappear automatically:

  - Register : "Successfully sign in as {username}"
  - Sign in : "Successfully sign in as {username}"
  - Logout: "You have sign out"
  - Successful created appointment: "Appointment confirmed for {patient_name} on {date} at {time}""
  - Successful updated appointment: "Successfully updated appointment for {patient_name} on {date} at {time}"
  - Successful deleted appointment: "Appointment deleted!"

<details>
<summary>Screenshots</summary>
<br>

![Message sign in/register](documentation/features/mess_sign_in.jpg)
![Message sign in out ](documentation/features/mess_sign_out.jpg)
![Message created](documentation/features/mess_created.jpg)
![Message updated](documentation/features/mess_updated.jpg)
![Message deleted](documentation/features/mess_deleted.jpg)

<br>
</details>  

  
Feedback messages that stay on until user closes them by pressing X button:
  - Appointment outside of working hours: "Invalid time - Hours for appointments are : Mon-Fri: 8am-5pm, Sat: 8am-1pm"
  - Appointment cannot be in the past: "Invalid date or time - Appointment cannot be in the past"


<details>
<summary>Screenshots</summary>
<br>

![Invalid date](documentation/features/invalid_date.jpg)
![Invalid time](documentation/features/invalid_time.jpg)

<br>
</details>    

# Design

## Wireframes
Wireframes were made using [Balsamiq](https://balsamiq.com/).
During development effort was put in to make the final website look and function as described in wireframe.

<details>
<summary>Screenshots</summary>
<br>

Homepage

![Homepage](documentation/wireframes/Homepage.png)

Services

![Services](documentation/wireframes/Services.png)

Register

![Register](documentation/wireframes/Register.png)

Login

![Login](documentation/wireframes/Login.png)

Logout

![Logout](documentation/wireframes/Logout.png)

Make appointment

![Make appointment](documentation/wireframes/Make_appointment.png)

Appointments

![Appointments](documentation/wireframes/Appointments.png)

<br>
</details> 
 
<hr>  

## Database

## Fonts

## Color Scheme












# Testing
[USER STORY: Website works as intended](#user-story-website-works-as-intended)

## Responsive Design

## Validator Testing

### HTML5

### CSS3

### Lighthouse

### Accessibility

Accessibility was tested during development using [Wave Chrome extension](https://wave.webaim.org/) and after final deployment was tested with **accessibilitytest.org**

[Accessibility test result ](https://accessibilitytest.org/results/v7_9UaOphxoT)

## Functional Testing

## Browser Testing



 

## Bugs   

### Fixed Bugs

Error: That port is already in use
[Fix](https://stackoverflow.com/questions/27066366/django-development-server-how-to-stop-it-when-it-run-in-background)

## Bug fix during testing: 
- Place html templates inside the app folder
- Add allauth email settings ( was getting 500 Error if user imputed email during registration)
- Add iframe title to improve accessibility score
- Remove Logo image alt attribute 

## Unfixed Bugs

# Deployment

## Version Control

## Heroku

## How to Clone this repository



# Technologies used
- [Django 3.2.15](https://docs.djangoproject.com/en/4.1/releases/) for the structure of the website.
- [HTML5](https://en.wikipedia.org/wiki/HTML5) for the contents and structure of the website.
- [CSS3](https://en.wikipedia.org/wiki/CSS) for the styling and animations.
- [JS](https://developer.mozilla.org/en-US/docs/Web/JavaScript) timed message functions.
- [Balsamiq](https://balsamiq.com/) for wireframing.
- [GitHub](https://github.com/) as a remote repository.
- [gitpod.io](https://www.gitpod.io) was used as IDE and  git version control.
- [Heroku](https://www.heroku.com/) to deploy the website/app.
- [Chrome](https://www.google.com/intl/en_ie/chrome/),  [Firefox](https://www.mozilla.org/en-US/firefox/new/),
[Brave Browser](https://brave.com/),
[Edge](https://www.microsoft.com/en-us/edge) and [Opera](https://www.opera.com/) for browser testing the responsiveness.
- [Chrome Developer Tools](https://developer.chrome.com/docs/devtools/) for testing screen sizes and using [Lighthouse](https://developers.google.com/web/tools/lighthouse).
- [Favicon.io](https://favicon.io/favicon-generator/) to create a favicon.
- [Markdown Monster](https://markdownmonster.west-wind.com/) for writing my readme.
- [Grepper Chrome extension](https://www.codegrepper.com/) for finding code.
- [Wave Chrome extension](https://wave.webaim.org/) to check web accessibility.
- [accessibilitytest.org](https://accessibilitytest.org/) to check web accessibility score.
- [Pesticide Chrome extension](https://chrome.google.com/webstore/detail/pesticide-for-chrome-with/neonnmencpneifkhlmhmfhfiklgjmloi) during development.
- [Unicorn Revealer Chrome extension](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB) during development.
- [Multi Device Website Mockup Generator](https://techsini.com/multi-mockup/index.php) for testing and to make responsive image.
- [Django Secret Key Generator](https://djecrety.ir/) 
- [Blur image](https://www.befunky.com/create/)
- [Image converter](https://ezgif.com/jpg-to-webp)
- [Bootstrap 4](https://getbootstrap.com/docs/4.0/getting-started/introduction/)
- [Django-bootstrap-datepicker](https://django-bootstrap-datepicker-plus.readthedocs.io/en/latest/index.html)
- [Django-phonenumber-field](https://github.com/stefanfoulis/django-phonenumber-field)


## Tools and tips

[What's the best way to store a phone number in Django models?](https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-a-phone-number-in-django-models) 

# Credits
  
  [Dental procedures](https://www.nhs.uk/live-well/healthy-teeth-and-gums/dental-treatments/) 

# Contact

# Acknowledgments


