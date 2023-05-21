# BlaBla. The conversations app #

## **UX Design** ##
I desinged this app with a mobile first approch as social media apps are mainly used by mobile.

The conversation posts are displayed in a card and this theme is consistant on all pages.

I went with a dark theme for this app as it is easier and more pleasing to look at.

### **Theme colours:** ###
**Background: #333333** - This is a dark grey colour and gives the over all dark theme

**App Logo: #33C8FF** - This is what I call BlaBla Blue, it is a light blue that contrasts well ontop of the dark grey background, this colour is also used for the app buttons like "create new conversation", "login/logout" ect.. This ties the overall theme together nicely

**Conversation cards** - These cards are styled with Bootstrap card-bg-dark, this colour is a slightly darker grey than the background and gives a nice contrast.


## **Features** ##
* Register a new account.
* Log in and Log out of user accounts.
* Create a conversation post.
* Attach images to a conversation post.
* Like and unlike a conversation post.
* Leave a comment on a conversation post.
* Edit existing conversation posts.
* Delete conversation posts.


## **Technologies used** ##
* **Django** - This is the framework used for the app.
* **Gunicorn** - HTTP server.
* **Psycopg2** - Allows connextion to SQL databse.
* **Cloudinary** - Database used for storing images.
* **AllAuth** - User authentication.
* **Crispyforms** - Handles forms.
* **Unittest** - Bulit in python tester.
* **ElephantSQL** - Database.
* **Heroku** - Deployment of app.

## **Testing** ##
### **Responsive testing** ###
Manually tested the resposiveness of the app and found no areas to be sluggish.

### **Browser compatibility** ###
Tested app running on Google chrome, Microsoft Edge and Firefox. All working as designed.

### **Code validation** ###
**Lighthouse testing outcomes** -
![picture alt](/README_images/BlaBla_lighthouse_report.PNG "Lighthouse report")

**HTML validater**
Using W3C validater my app retuned 2 faults for the placeholder image being //:0 saying it is an empty host, I used this as a workaround as I could not remove the image field as a required field for the model. This will be corrected in future updates.
[Validatder link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fblabla-baz.herokuapp.com%2F "HTML validater")


### **User stories testing** ###
Manually tested all functions described in my user stories, all user story requirements are working as designed.

You can see the user stories in the projects tab of this repo.

### **Python unittest** ###
Inside tests.py file there unittesting for all the view functions to insure that they are working as designed. The testcase is set up by created a post and creating a user. Creating a user is needed as some views are only displayed for authenticated users. tests.py makes sure the correct templates are being displayed and the edit and delete views are doing there job.

**Please note! When carrying out the unittesting you must comment out the default DATABASE in settings.py and comment in the local DATABASE used for testing (Refernace image below)**

![picture alt](/README_images/settings.py_testing_database.PNG "Testing Database")

To run these tests run this in the command line - python3 manage.py test

![picture alt](/README_images/unittest.PNG "Lighthouse report")

### **Manual testing** ###
I carried out manual testing of all functions of the app, made sure lnks went where they are meant too and comments and likes were displayed as should, during this testing I found when creating a new post the image was not being uploaded to the model, I found the fix was to add the enctype="multipart/form-data" attribute was needed to handle this.

### **Design flaws** ###
* The comment icon has a btn Bootstrap class but is not a button, this may give the user the expression it can be clicked. This is because the Like icon is a button the user can click but this gave it different properties and looked off when beside the comment icon. using the btn class on the comment icon gave the icon the same properties and they now look uniform. In a future update I would like to make the comment icon take you to make a new comment when clicked.

## **Deployment** ##
This app was deployed using heroku.
1. Created a new app in Herkoku.
2. Linked up my Github repo.
3. Set my enviroment varibles in Heroku.
4. Add Procfile and requirments.txt to the project.
5. Tunred DEBUG to Flase.
6. Pushed my finished code to Heroku.
7. Deployed app.


## **Future updates** ##
* Allow user to see all there draft posts and publish them if they wish.
* Users can gain follwers.
* A function for users to be able to block other users and not see any posts or comments from them.
* Function to be able to upload videos.