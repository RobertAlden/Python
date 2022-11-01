cd %CD%/components
call .\env\Scripts\activate
cd ..
start chrome http://127.0.0.1:5000/
call python app.py
