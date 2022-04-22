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
