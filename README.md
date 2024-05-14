# Access Control System

This project was created with the purpose of applying for a back-end web developer vacancy.

## How to Use

1. Clone the repository in an environment with Python 3.8 installed.
2. Once cloned, execute the command `pip install -r requirements.txt` to install the necessary dependencies to run the project.
3. PostgreSQL is used as the database. You must create a database named CDA and restore it with the file located in /RestauracionDB/DB-CDA. Alternatively, you can use any other database, but the configuration data will be required.
4. Then, just run the command `python manage.py runserver`.
5. To create a super administrator user, execute the command `python manage.py createsuperuser` as the application requires authentication from the start of its execution.

## Correct Functionalities
1. CRUD of Company, Users, Access Points, Access Schedules.
2. The superuser can create companies and users for companies.
3. The administrator user of each company can create the access points and schedules for their own company, not for other companies. Additionally, they only have access to these modules.
4. The company's administrator user can only invite users, not create them.

## Update
1. REST requests to validate an employee's access to the company.

To use the service, it is necessary to make a GET request to the URL http://127.0.0.1:8002/api/consultar-acceso with the project running, and send the following parameters. In addition to this, the database copy named Restore_CDA_REST must be restored, which contains the necessary data and parameterization ready for API consumption.
- company
- username
- headquarters

Where company is the name of the company, username is the name.surname, and headquarters is the name of the headquarters where the query is made.
Access is calculated with the current system time, if correct, it returns the headquarters data, otherwise, it returns False.

## Incomplete Functionalities
1. Email-dependent functionalities are not functional due to authentication issues with SMTP servers.
2. Assignment of accesses to invited users

## Preview of GET request by Postman
![image](https://user-images.githubusercontent.com/37114980/165379043-2b2a5572-5c68-426f-8228-60d0cf24efe5.png)

## Web Preview
![image](https://user-images.githubusercontent.com/37114980/164785407-f5b2abba-c736-4c5b-9756-9f0d2565c0b6.png)
![image](https://user-images.githubusercontent.com/37114980/164785513-29e78f20-d8e8-46b2-8643-0e0f139aad69.png)
![image](https://user-images.githubusercontent.com/37114980/164785535-38b7c5d6-9de9-42b9-b15b-77c36043140b.png)
![image](https://user-images.githubusercontent.com/37114980/164785589-f78b949c-4bad-46d2-8c35-ceaae12532bf.png)




