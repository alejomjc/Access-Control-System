# Sistema de Control de Acceso

Este proyecto se creó con la finalidad de aplicar a una vacande de desarrollador web back-end

## Como usar

1. Se debe clonar el repositorio en un entorno con python 3.8 instalado
2. Una vez clonado, se debe ejecutar el comando pip install -r requirements.txt para instalar las dependencias necesarias para ejecutar el proyecto.
3. Como base de datos, se usa postgresSQL, se debe crear una DB con nombre CDA y restaurar con el archivo localizado en /RestauracionDB/DB-CDA
Opcional a ello se puede usar cualquier otra, pero harian falta los datos de parametrización.
4. luego, solo se debe correr el comando python manage.py runserver.

## Funcionalidades Correctas
1. CRUD de Empresa, Usuarios, Puntos de Acceso, Horarios de Acceso.
2. El usuario superuser puede crear empresas y usuarios para empresas
3. El usuario administrador de cada empresa, puede crear los puntos y horarios de su propia empresa, y no las de otras empresas. Adicional, solo tiene acceso a estos modulos.
4. El usuario administrador de la empresa, solo puede invitar usuarios, no puede crearlos.


## Funcionalidades Incompletas
1. Las funcionalidades dependientes de correo electrónico no son funcionales, debido a problemas de autenticación con servidores SMTP.
2. Conexión REST
3. Asignación de accesos a usuarios invitados

## Vista Previa de la Web
![image](https://user-images.githubusercontent.com/37114980/164785407-f5b2abba-c736-4c5b-9756-9f0d2565c0b6.png)
![image](https://user-images.githubusercontent.com/37114980/164785513-29e78f20-d8e8-46b2-8643-0e0f139aad69.png)
![image](https://user-images.githubusercontent.com/37114980/164785535-38b7c5d6-9de9-42b9-b15b-77c36043140b.png)
![image](https://user-images.githubusercontent.com/37114980/164785589-f78b949c-4bad-46d2-8c35-ceaae12532bf.png)



