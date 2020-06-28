# Your Gallery 
## Author  
  
>[Wanjiku-Karanja](https://github.com/3xistentialcrisis)  
  
# Description  
This is a Django personal gallery application that enables you to display your photos for others to see.
  
##  Live Link  
 Click [View Site](https://ur-gallery.herokuapp.com/)  to visit the site
  
## Screenshots 
###### Home page
 
<img src="https://raw.githubusercontent.com/3xistentialcrisis/Gallery/master/static/images/landingpage.png" width="900px" height="440px">
 
 ###### Search results
 <img src="https://raw.githubusercontent.com/3xistentialcrisis/Gallery/master/static/images/search.png" width="900px" height="440px"> 

 ###### Image Details 
 <img src="https://raw.githubusercontent.com/3xistentialcrisis/Gallery/master/static/images/images.png" width="900px" height="440px">
 
## User Story  
This app enables user to:

* View different photos that interest them  
* Click a single image to expand it and view the details of that photo  
* Search for images in different categories   
* Copy a link to the photo to share with their friends.  
* View photos based on the location they were taken.  

  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
 https://github.com/3xistentialcrisis/Gallery/.git 
```
##### Navigate into the folder and install requirements  
 ```bash 
cd Gallery pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
python3 -m venv virtual 
```  
```bash 
source virtual/bin/activate 
```

##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrations 
 ```bash 
python manage.py makemigrations album 
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python3.8 manage.py runserver 
``` 

##### Testing the application  
 ```bash 
 python3.8 manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.8](https://www.python.org/)  
* [Django 1.11.17](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
* Postgres
* Pip
* Html and CSS (Bootstrap)
  
## Known Bugs  
There are no known bugs at the time of deployment of this application 
  
## CodeBeat
[![codebeat badge](https://codebeat.co/badges/61881488-2da3-4522-be01-0226f8d1a6c6)](https://codebeat.co/projects/github-com-3xistentialcrisis-gallery-master) 

## License 
[![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](https://github.com/3xistentialcrisis/gallery/blob/master/LICENSE)

## Contact Information   
If you have any question or contributions, please email the administrator at [administrator@gallery.com] 
