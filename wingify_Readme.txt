Creating an online store 

1. Create a virtual environment let suppose 'env' using command line 'virtualenv env'
2. Give all permissions to env
3. Activate the environment
4. Install all libraries used in this project u will find out in requirement.txt 
   executing command pip install -R requirement.txt
5. install postgres database
6. run postgres server create database lets suppose 'create database wingifydb --password'
7. enter password for database
8. grant permission to user you have created in postgres
9. all the database settings in project directory settings.py
10. Environment activate and go to project directory from terminal
11. Run command python manage.py makemigrations 
12. Run command python manage.py migrate
13. after migrations done it creates schema in database on the basis of models
14. run server using command python manage.py runsever

-------------Setup done---------------------------

15. create a dummy user from django admin  authentication token will create when you save the user.
16. or you can create run python manage.py createsuperuser
17. Token created automatically by using post save signal


Token(or login API) API:
Request:
	Method - Post
	parameters: username, password
	request url: http://127.0.0.1:8000/api-token-auth/

Response:
	status: 200 OK
	body: token

Sample : attached screenshot


Get Product or Search:
Request:
	Method - GET
	header - Authorization:token {{token}}
	request url: http://127.0.0.1:8000/store/get_product/?q=''

Response:
	status: 200 OK
	body: data

Sample : attached screenshot

Add Product API:
Request:
	Method - POST
	parameters: name, sku_id, quantity, price
	header - Authorization:token {{token}}
	request url: http://127.0.0.1:8000/store/add_product/

Response:
	status: 201 Created
	body: There is no body in POST

Sample : attached screenshot

Edit Product API:
Request:
	Method - PUT
	parameters: name, sku_id, quantity, price
	header - Authorization:token {{token}}
	request url: http://127.0.0.1:8000/store/edit_product/{{id}}

Response:
	status: 200 OK

Sample : attached screenshot

Delete Product API:
Request:
	Method - DELETE
	parameters: id
	header - Authorization:token {{token}}
	request url: http://127.0.0.1:8000/store/delete_product/

Response:
	status: 200 OK

Sample : attached screenshot





