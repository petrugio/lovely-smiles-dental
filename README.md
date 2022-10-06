# Planning 

Significant amount of time  was devoted to planing the layout and structure of the agile board.  
Having a meeting by myself and changing the hat from product owner to user and then to developer was decided to use Github projects as a agile tool for the ***Lovely smiles dental*** PP4 project. 
From the time remaining to submit a working project was decided to split the development into 5 iteration each lasting 1 week.

After the project scope was clearly defined, following the process of creating milestones/epics, I added User Stories and Tasks to the Backlog and prioritized them using **M.o.S.C.o.W prioritization technique** and assigned them to the appropriate milestone/epic and iteration



<hr>


 # User Experience



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
   
   
## Credits
  
  [Dental procedures](https://www.nhs.uk/live-well/healthy-teeth-and-gums/dental-treatments/) 
  
 
## Tools
[What's the best way to store a phone number in Django models?](https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-a-phone-number-in-django-models) 

[Django Secret Key Generator](https://djecrety.ir/) 

[Bootstrap 4](https://getbootstrap.com/docs/4.0/getting-started/introduction/)



## Bugs   

### Bugs and issues fixed
Error with dependencies in Django 4
[Fix](https://pypi.org/project/backports.zoneinfo) 

Error: That port is already in use
[Fix](https://stackoverflow.com/questions/27066366/django-development-server-how-to-stop-it-when-it-run-in-background)
