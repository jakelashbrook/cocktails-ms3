<h1 align="center" id="your-tail">What's your tail?</h1>

[Insert website screenshot here ]

See the current [Deployed Version](https://whats-your-tail.herokuapp.com/) of the app.

---
## README Sections 
<a href="#ux">User Experience</a>  

<a href="#features">Site Features</a>  

<a href="#tech">Incorporated Technologies</a>  

<a href="#test">Testing</a>  

<a href="#deploy">Deployment</a>  

<a href="#credits">Credits</a>

---

<h2 align="center">An Introduction</h2> 

We've all had those long days or weeks at work where it get's to 4 o'clock and we're staring at the clock thinking 
about what beverage we're going to treat ourselves to when we get home. We all know it's naughty, and definitely not 
good for our bodies if not enjoyed in moderation- but that doesn't stop us from wanting to partake on a journey of creativity 
and discovery when it comes to enjoying a nice cold beverage after a hard day in the office.

What's your tail? Is a website built around Cocktails, a centre for people to express their creativity and share their ideas 
and recipes with a like-minded community. Whether you want some inspiration, or you want to inspire others with a mouthwatering 
concoction of your own discovery or creation- this is the place to be!

What's your tail is my third Milestone project for submission to the Code Institute Full Stack Web Development Diploma that 
I am currently enrolled as a student on. 

---

<h1 id="ux" align="center">User Experience</h1>

## Project Criteria 
- Design and make a website using HTML, CSS, JS/jQuery, Python+Flask and MongoDB.
- Fully incorporate CRUD functionality within the site.
- Allow users to manage and edit a common dataset.

## Specific Site Goals 
- Create a site that allows users to add, update, and delete their own recipes from the recipe.
- Allow users to like other users recipes.
- Make the site easy and intuitive to navigate and use.

## Website User Stories 

#### First Time User Goals:
- As a first time user, I want to be able to easily search for recipes based on keyword ingredients I would like to use. 
- As a first time user, I want to see a selection of recipes to easily browse through for inspiration.
- As a first time user, I want to be able to easily use the site regardless of the device being used to access it. 
- As a first time user, I want to be able to select specific categories of recipes. For example, Alcohol or Non-Alcoholic Mocktails.
- As a first time user, I want to be able to register for an account and contribute my own recipes.
- As a first time user, I want to be able to intuitively use the site and navigate to specific areas.  

#### Registered Account Goals:
- As a registered user, I want to be able to share my recipes with the website for other users to enjoy.
- As a registered user, I want to be able to modify or delete my recipes.
- As a registered user, I want to be able to easily login to and manage my account. 
- As a registered user, I want to be able to sign out of my account with ease.
- As a registered user, I want to be able to like other recipes that I have enjoyed or wish to try. 

#### Admin Account Goals: 
- As the admin user, I want to be able to delete any recipes that do not fit with the site theme of Cocktails.
- As the admin user, I want to be able to add new categories of Cocktails.
- As the admin user, I want to be able to remove any categories that do not serve a purpose. 
- As the admin user, I want to be able to remove any accounts that do not adhere to posting the correct content. 

## Design

#### Colour Scheme 
I used the [Coolors](coolors.co) to search for different colours to use within the app. Here is a list of the colours and their respective hex codes:  
- #009688 :  Shade of Green
- #F5F3F7 : Offshade of White/Gray
- #D7D6D6 : Lighter Shade of Gray
- #A1A1A5 : Darker Shade of Gray
- #210124 : Lighter Shade of Black

I also decided to include a light and dark mode using Black and White Marble Images. The idea is that it would
give the website a bar vibe and fit with the app focus of Cocktails.


#### Typography  
The fonts used within the app are all from the [Google Fonts Library](https://fonts.google.com/). Within this project I
used [Yomogi](https://fonts.google.com/specimen/Yomogi?query=yomo), [Tourney](https://fonts.google.com/specimen/Tourney?query=tourn), and [Montserrat](https://fonts.google.com/specimen/Montserrat?query=montserrat). The default backup font
is sans-serif.

#### Icons 
In this project, I will use the Font Awesome Library due to the wide variety of icons it offers. You can take a look at their library [here](https://fontawesome.com/)

#### Images 
Due to users being able to use images URL's when creating their own recipes, Images will come from a variety of sources in the end. 
However, I will use the recipe images from [bbcgoodfood.com](https://www.bbcgoodfood.com/) for this project as the majority of cocktail recipes have been sourced from there. Any additional credits will be listed in the credits section. It also 
worth noting that the backgrounds for Light/Dark mode will be image based as mentioned above.

## Wireframes 

You can see the original Wireframes [here](), I decided to make a dedicated PDF so as not to overfill
this document. Obviously since originally designing them the site has evolved and changed out of 
necessity due to knowledge of implementation and time scales available to work with. The main differences
are:

## Information Architecture  

<h1 id="features" align="center">Site Features</h1>

## Current App Features 

### General Features
- A crisp and simple design, easy for the user to understand.
- The Cocktails are showcased simply on the homepage and it's own page, and are easy to explore using the
categorised buttons or the search functionality.
- The site is easy to navigate using the Navigation system, Call to Action buttons and the Top/Bottom floating
buttons.
- The site provides a light/dark mode for viewing in whichever is preferable to the user.
- CRUD Functionality
    - Users can Sign Up, Sign In, Logout, Upload Cocktails, Edit their Cocktail Recipes, Read uploaded Cocktails and Delete their Accounts/ Recipes.
    - The admin can do all of the above, Aswell as Add/Edit/Delete Categories, Remove Users, View Promotions info etc.

### Page Features & Functionality  

- **Base.html**
    - Navigation
        - Search Cocktails
    - Footer
    - Top/Bottom Buttons

- **Homepage**
    - Love This Site
    - Sign up for Promotions
    - Shop Now
    - Popular Cocktails
    - Social Media Links
- **Cocktails**
    - All Cocktails
    - Category Buttons for Cocktails
- **Register/Login/Logout**
    - Sign up to app.
    - Login to website with user credentials.
    - Logout of website and return to login page.  
- **My Profile**
    - My Uploaded Cocktails
    - Deativate My Account

## Admin Page Features & Functionality
- **Manage Categories**
    - View, Edit Or Delete existing categories.
    - Add new category
- **Manage Users**
    - View existing users
    - Remove users
- **Promotions List**
    - View email addresses of people who have signed up for promotions.
- **Manage Cocktail Recipes**
    - View, Edit and Delete existing Cocktails.

## Features To Implement Later
- **Cocktails Pagination**
    - Originally I planned to include this straight away, but after much reading and not having enough Cocktails on the
    App yet for it to seem worthy to invest time in pagination I decided to go with a top/bottom button for the time being
    until there is more Cocktails included within the app. This decision was made due to timings and the fact that all of 
    the site content is relatable so therefore easy to scroll through. When a user needs a specific recipe, the search function is available and easily accesible using the 'Back to top' button.
- **Upgrade Promotions Feature**
    - Long term, make it so the site automatically responds to the email address users sign up. There could also be 
    more useful expansions to be added at a later date should they become relevant to the sites requirements.
- **Add change username option**
    - I think this would be a cool feature to have, as I often find myself wishing I could change my username 
    after making one.
- **Add ability to change password**
    - For security purposes, being able to change your password as often as needed is something that I think 
    should become a priority for a future release. Obviously at the moment, the site doesn't hold any sensitive
    data- but this could change as the site grows.
- **Upgrade the love/like system to individual recipes**
    - Originally I aimed to incorporate a like system for individual recipes, but due to the amount of 
    time I was left to work with I decided to compromise and have a love button for the website in general
    and then expand on it within a later release.
- **Upgrade the Bottom button to vanish when close to footer**
    - This is something I need to look more into at a later date. I'm currently unsure of how to make this happen
    but will only need to take the concept further if pagination is not added into the second release as i believe
    this would take away the need for the facility.

<h1 id="tech" align="center">Incorporated Technologies</h1>  

## Languages Used  
- [HTML5](https://html.spec.whatwg.org/)
- [CSS3](http://www.w3.org/Style/CSS/Overview.en.html)
- [Javascript](https://www.javascript.com/)
- [Python3](https://www.python.org/download/releases/3.0/)

## Frameworks, Libraries & Resources Used  
- [Bootstrap](https://getbootstrap.com/)
- [Flask](https://flask.palletsprojects.com/)
- [Jinja 2](https://palletsprojects.com/p/jinja/)
- [Google Fonts](https://fonts.google.com/)
- [Font Awesome](https://fontawesome.com/)
- [jQuery](https://jquery.com/)
- [MongoDB](https://account.mongodb.com/)
- [Heroku](https://id.heroku.com/login)
- [Werkzeug](https://werkzeug.palletsprojects.com/)

## Testing Tools & Utilities  
- [W3C HTML Validator](https://validator.w3.org/)
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
- [JShint Javascript Validator](https://jshint.com/)
- [PEP8 Python Validator](http://pep8online.com/)
- [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)

<h1 id="testing" align="center">Testing</h1>  

## Validation Results  

## Testing the App

<h1 id="deploy" align="center">Deployment</h1>

The master branch of this repository is the most current version and has been used for the deployed version of the site.

## Essential Requirements  
- [GitHub Account](https://werkzeug.palletsprojects.com/)
- An IDE that Supports Python3 for the core code.
- PIP for package installation.
- Git for version control.
- [MongoDB Account](https://account.mongodb.com/)  
    - MongoDB is the database that the users will store all of the data they create in the app within.
    - These Collections should be created within the cluster that will be used for the app:
        - Categories
        - Recipes
        - Users
        - Promotions
        - Loved
    - A document within Recipes should be created using the following fields:  

        |Key | Value | Type|
        |--- | --- | ---|
        |category_name | Unassigned | String|
        |recipe_name | Unassigned | String|
        |prep_time | Unassigned | String|
        |img_url | Unassigned | String|
        |ingredients | Unassigned | Array|
        |garnish | Unassigned | String|
        |method_step_one | Unassigned | String|
        |method_step_two | Unassigned | String|
        |inspiration | Unassigned | String|
        |method_step_one | Unassigned | String|
        |eat_with | Unassigned | String|
        |author | Unassigned | String|
        |created_by | Unassigned | String|

    - The MongoDB Cluster is apart of the AWS EU/Ireland Package. You can find out more [here](https://aws.amazon.com/)


- [Heroku Account](https://heroku.com)
    - See below for more information on how to deploy the app to Heroku.

## To Clone This App  

**To make your own local clone using GitHub Desktop, please follow these steps:**   
1. Log in to your [GitHub Account](https://github.com/) and go to this [repository](https://github.com/jakelashbrook/cocktails-ms3).
2. Click on the Grey Button in the top right corner of the page with the text “Code” just left of the Green Gitpod button.
3. Next click on the “Open with GitHub Desktop”  option and follow the prompts in the GitHub Desktop Application to clone the app.

## Work with the Local Copy  


**To make your own local copy using HTTPS, please follow these steps:**   
1. Log in to your [GitHub Account](https://github.com/) and go to this [repository](https://github.com/jakelashbrook/cocktails-ms3).
2. Click on the Grey Button in the top right corner of the page with the text “Code” just left of the Green Gitpod button.
3. In the Clone area select HTTPS the option, copy the clone URL for the repository.
4. In your chosen IDE, Open Git Bash.
5. Change the current working directory to the location where you would like the cloned directory to be stored.
6. Type git clone, and then paste the URL you copied in Step 3.
7. Now press Enter and your local clone should have been created.
8. Create a file called env.py to hold your app's environment variables, which should contain the following:
        import os

        os.environ.setdefault("IP", "0.0.0.0")
        os.environ.setdefault("PORT", "5000")
        os.environ.setdefault("SECRET_KEY", "<app secret key>")
        os.environ.setdefault("MONGO_URI", "mongodb+srv://<username>:<password>@<cluster_name>-ofgqg.mongodb.net/<database_name>?retryWrites=true&w=majority")
        os.environ.setdefault("MONGO_DBNAME", "<database name>")
9. It's vital to make sure that your Environment Variables are not pushed to GitHub so that the app's security is not
compromised! Double check you have included your env.py file within the .gitignore file before making any commits to Git.
10. If all the above steps have been followed correctly, you should now be able to run the app using this CLI Command:  

        python3 app.py

## How to Deploy to Heroku  
1. First things first, you should set up a local workspace at [Heroku.com](https://heroku.com).
    - In the terminal view of your chosen IDE, type: **pip3 freeze -- local > requirements.txt**. By typing this 
    command Heroku will know which files to install from your local development environment.
    - Aswell as the requirements.txt file, you will also need to create a Procfile. Heroku will use this file 
    as a kind of gateway to your project. In the terminal of your IDE, type: **python app.py > Procfile**. This 
    command will create the Procile for you.

Make sure that you push these files to your master branch so that they can be accessed by the Heroku app when it's
set up.

2. Now that you've set up your requirements.txt and Procfile, you need to set up your Heroku account (if you don't 
already have one). Inside your account, Create an app and then select the appropriate region relevant to your location.

3. Next we will deploy our GitHub Branch to Heroku which will host our app for us, however unlike Gitpod- Heroku will
only host the code that has been committed to the branch and not any code that is within the Gitpod workspace but uncommitted
to the master branch. 
    - Under the **Deploy** Tab at the top of the page, scroll down and within the **Deployment Method** area, 
    select **GitHub**.
        - Once selected, search the appropriate repository that you wish to connect to Heroku. When it appears,
        click **Connect** and Heroku will start automatically deploying the master branch as a Heroku app.

4. Now that the app is connected to the relevant repository, we need to set up some important Configuration Variables.
Click on the **Settings** Tab at the end of the App Nav, And then scroll down to the **Config. Vars** area and select
**Reveal Config Vars**. Inside this area you will enter the appropriate variables from your **env.py** file, these 
will include the keys named **IP, PORT, SECRET_KEY, MONGO_URI, MONGO_DBNAME**, you will need to supply the values.

5. Once all of these steps have been taken, we can now set up **Automatic Deployment** so Heroku will automatically 
check for updates to the master branch and update the Heroku App. Head back to the **Deploy** tab and select the 
**Automatic Deploys** area, and then click the **Enable Automatic Deploys** button. 

6. If you scroll down to the bottom of the **Deploy** Tab you will also notice an option for **Manual Deploy**.
Click the **Manual Deploy** Button and it will start building your app. I find it often useful to do a Manual Deploy
after any big pushes containing lots of new or changed code.

Now that all of the steps are complete, Heroku is connected to the repositorys Master Branch and will continue to 
recieve the code using the required file packages. You should now be able to select **Open App** in the top righthand
corner of the page.



<h1 id="credits" align="center">Credits</h1>  

## Code and Resources
- Light/ Dark Mode Inspired by [this article](https://css-tricks.com/a-complete-guide-to-dark-mode-on-the-web/) from CSS Tricks, but also [Stack Overflow](https://stackoverflow.com/) for help inspiring the end method used.
- The Top/Bottom buttons were inspired from my milestone 2 project [Discover Penwith](https://github.com/jakelashbrook/discover-penwith) and then updated/edited to fit the purpose of this project. I was originally inspired by [W3 Schools](https://www.w3schools.com/) for this concept as written in my code comments.
- [Bootstrap](https://getbootstrap.com/) for all the components and utilities used to make the development of this app much faster.
- The [Task Manager Project](https://github.com/Code-Institute-Solutions/TaskManagerAuth) for inspiring and educating me before building this milestone project, Thank You Tim Nelson!

## Content 
- [BBC Good Food](https://www.bbcgoodfood.com/recipes/collection/cocktail-recipes) for start up Cocktail Content. 
- [Olive Magazine](https://www.olivemagazine.com/drink/best-ever-cocktail-recipes/) for some Cocktail Content.


## Ackowledgements 
- My Code Institute Mentor Antonio Rodriguez, for always being on hand to encourage and motivate me towards finding valid solutions.
- My partner, for putting up with me when stressed and in study mode.
- The Code Institute Tutors, for steering me in the right directions to finding solutions for myself when needed.
