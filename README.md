# MEPIC GALLERY
- MEPIC is a platform where users can display their photos for others to see, they can share the photos by coping the photo link and also add different categories of photo. Their friends can like the photos too.

## Author
- Loise Muthoni

## Requirements

The following command installs all the application requirements
>``pip freeze -r requirements.txt``


## Installations

Run 
``git clone https://github.com/loisemuthoni/mepic.git``

or download the zip file from github.

After extracting the files, 

1. Navigate to the project folder
>`` cd MEPIC.`` 

2. Creating a virtual environment
>``virtualenv virtual.``

3. Activating the virtual environment
>``source virtual/bin/activate.``

4. Running the application

>``python3 manage.py server``

5. Running tests

 > ``python3 manage.py test.``


## User Stories
- As a user, I would like to view different photos that interest me.
-  As a user, I would like to click on a single photo to expand it and also view the details of the photo.
-  As a user, I would like to search for different categories of photos.
-  As a user, I would like to copy a link to the photo to share with my friends.
-  As a user, I would like to view photos based on the location they were taken.


## Behavior Driven Development
<img src="landing.png">
The application should display photos.
When a user clicks on a photo, the photo should expand and the details of the photo to be displayed on a modal within the main page.
-  When a user enters a search term on the search input and submits it, then they should be able to get a result of what they are looking for or if the term does not exist, they should get a message to inform them.
- When a user clicks on the copy button, then they should be able to have the image link copied to their machine clipboard.

## Technologies Used
- Python
- Django
- PostgreSQL

## Contact
- Email: loisemburu01@gmail.com

## Licence and Copyright
MIT License

Copyright (c) 2020 Loise Muthoni

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

