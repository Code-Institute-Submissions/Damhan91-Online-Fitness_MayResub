# Online Fitness

## Content
Introduction\
User experience\
Colors\
User stories\
Testing\
Deploying to github pages\
Validation\
Tech used\
Credits

## Introduction
The idea for this project was based around fitness industry and personnel training, which is something that I enjoy. With most jobs now being able to work remotely, personal trainers shouldn't be restricted to people in their local area. Having this website will allow a personal trainer to guide and train their clients on diet and exercises that are not from their local area. The website also shares fitness blogs, where users can share their thoughts and ideas on each blog. To be able to see this content the use must first register and sign up to the website. For the user, it can be very over whelming for new people getting into fitness. This website condenses that information into easily read and easy to understand instructions to help the user achieve their goals.
### WireFrames of project
 ![Wireframe](https://github.com/Damhan91/Online-Fitness/blob/main/static/images/Home%20Page.JPG)
 ![Wireframe](https://github.com/Damhan91/Online-Fitness/blob/main/static/images/Login.JPG)
 ![Wireframe](https://github.com/Damhan91/Online-Fitness/blob/main/static/images/Register.JPG)
 ![Wireframe](https://github.com/Damhan91/Online-Fitness/blob/main/static/images/Loged%20In.JPG)
 ![Wireframe](https://github.com/Damhan91/Online-Fitness/blob/main/static/images/Wireframe%201.JPG)
 ![Wireframe](https://github.com/Damhan91/Online-Fitness/blob/main/static/images/Wireframe.JPG)
 
## User Experince
![Wireframe](https://github.com/Damhan91/Online-Fitness/blob/main/static/images/Website%20home.JPG)
![Wireframe](https://github.com/Damhan91/Online-Fitness/blob/main/static/images/website%20register.JPG)
![Wireframe](https://github.com/Damhan91/Online-Fitness/blob/main/static/images/Website%20sign%20in.JPG)
![Wireframe](https://github.com/Damhan91/Online-Fitness/blob/main/static/images/Website%20Logged%20In.JPG)

The user experience I wanted the user to be able to look and find the information as quickly as possible. The website is easy and straight forward to register and sign up to and I wanted the main content of the website to only accessible to registered users.

## Design
For the design of the website, I went with three main colours. Black and grey with white writing. I wanted the writing and information to be the thing that captures the users attention and not getting distracted by an array of different colours. The white writing looks best against the dark background and really stands out.

Images\
For images I used them where i felt it they were needed and added to the aesthetic of the website. I initially had a large hero image covering the top half of the webpage, but I removed this as I felt it gave a bad user experience because each time you would have to scroll down to view the content

## User Stories

As a developer I wanted the user to have one wbsite the user can go to for information about fitness. When I started going to the gym and taking an interest in fitness it was very overwhelming the amount of infomraiton that is out there and you are not sure what to follow. This website allows the user one website to follow the advice of a personel trainer to help them on their own to achieve their fitness goals.There is also a helpful blog section that the user can read. the user can also create, delete and edit their own comments.
![Wireframe](https://github.com/Damhan91/Online-Fitness/blob/main/static/images/Exercises.JPG)
![Wireframe](https://github.com/Damhan91/Online-Fitness/blob/main/static/images/Nutrition.JPG)
![Wireframe](https://github.com/Damhan91/Online-Fitness/blob/main/static/images/Blogs.JPG)
![Wireframe](https://github.com/Damhan91/Online-Fitness/blob/main/static/images/comments.JPG)

Possible features to add

Subscription based system\
Private messenger between the user and the Personal Trainer\
Online classes\
Reply to comments\
Shop for fitness products like protein etc

## Testing
All the HTMl and CSS code works as expected  and as well as going through the website manually, I have tested the HTML, CSS and Django code using third party validations such as Pep8 for Django and W3C validationf for HTML and CSS.

## Validation 
Links to validation below\
[Django 1](https://github.com/Damhan91/Online-Fitness/blob/main/static/images/Django%20code.JPG)\
[Django 2](https://github.com/Damhan91/Online-Fitness/blob/main/static/images/Django%20code2.JPG)\
[HTML](https://github.com/Damhan91/Online-Fitness/blob/main/static/images/html.JPG)\
[CSS](https://github.com/Damhan91/Online-Fitness/blob/main/static/images/css.JPG)\
[Lighthouse](https://github.com/Damhan91/Online-Fitness/blob/main/static/images/lighthouse.JPG)
## Bugs
After a user comments on one of the blogs, if the press the back button in the top left hand of the webpage, it will remove the comment. This only happens when they add a new comment.
## Deploying to Heroku
Go onto Heroku\
Login to my account.\
Click create new app.\
I choose a name for my project and the region that I am in (Eu).\
Go to setting.\
Click on reveal config vars\
Add in CLOUDINARY_URL, DATABASE_URL and your secret_key\
Go to resources and search for Postgres, and install the Heroku Postgres\
Go to Deploy\
Connect to github login.\
Search for the project you wish to connect. Once found click the connect button
After this I click the deploy button at the bottom.\
Link to Online Fitness can be found [Here](https://onlinefitnessdjango.herokuapp.com/)
## Tech used
Github\
Gitpod\
Django\
Heroku\
Pep8 validation
## Credits
I would like to have a shout out to my old mentor Felipe for helping me with the direction of the project when I first started. I would also like to thank my new mentor Jack, who helped my when I was struggling and gave me great guidance.
## Edited for Resubmission
### User Stories

#### User Stories for Users

As I user I would like to  | So I can
------------- | -------------
Find workouts | So I know what workouts to do.
Find diets    | I know what I need to eat.
Read blogs  | Find out the latest tips and advice for better performance and diet.
Comment on blogs  | To share my thoughts and ideas to other users.
Edit and Delete comments | Being able to ewdit or delete my own comments.



### Testing
#### Website Testing
- Each navigation link works as intended, including the logout
- The navigation collapses as intended on mobile devices.
- Only loged in users are able to view the excersises, diet and blog content.
- Authenticated user are able to delete and edit their own comments on each blog.
- The likes and comment icon, increase in number each time a like or comment is added.
- When a comment in edited or delted the user is brought back to the blog.
