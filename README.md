# InternshipProject

To run project:
(you can use virtual enviroment)
1. Install python dependencies:
	pip install -r requirements.txt

2. Download ngrok:
	https://ngrok.com/download

3. Run "python APIManagment.py" in InternshipProject\Backend\

4. Run "./ngrok http http://127.0.0.1:5000"

5. Copy first "Forwarding" ngrok url (example: http://213f31513e31.ngrok.io)

6. In Internship\Frontend\my-app\App.js:
	paste ngrok url to "NGROK_URL" variable

7. Run "npm start" 

