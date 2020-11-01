#### Its a Django application system should pre install the python to run this application

##### There is a setup shell script is available in the project directory, I have make it according to mac, in case it is not working please follow the steps below. Run following command in project directory to make it run
    sh setup.sh
     
##### Install virtual env
    python3 -m pip install --user virtualenv

##### Install virtual env
    virtualenv assignment
##### Activate virtual env
    source assignment/bin/activate

##### Install project dependencies
    pip3 install -r requirement.txt

##### Running unittest cases
    python manage.py test

##### Running the application
    python manage.py runserver
    
