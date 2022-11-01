cd %CD%/components/
call virtualenv env
call .\env\Scripts\activate
call pip install -r requirements.txt
cd ..
start chrome http://127.0.0.1:5000/
call python app.py
