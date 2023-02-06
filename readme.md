Video de explicación:
    * https://www.loom.com/share/39ae3cbbcce64bc4b4a479984619501f

Caracteristicas:
    1. En esta app seremos capaces de manejar una mini base de datos 'estudiantil'
    2. Podremos añadir, buscar, eliminar, visualizar y modificar:
        a. (Profesores, estudiantes, carreras y tareas según la carrera)
    3. Solo se podra modificar y eliminar si eres un usuario
    4. No estara permitido el acceso a la lista de estudiantes y de tareas a menos que estes registrado
    5. Puedes agregar un avatar a tu perfil

Instrucciones:
    1. Crea una carpeta contenedora 
    2. Abrir consola y ubicarse en la carpeta creada
    3. Crea y activa el ambiente virtual con virtual env desde la terminal
    4. Clonar el proyecto 
    5. Entrar en la carpeta recien clonada

Instalar las dependencias:
    1. pip install -r requirements.txt

Entrar al panel aministrativo de Django:
    1. En consola, siguiendo el siguiete comando, crear un super usuario:
        a. python manage.py createsuperuser
    2. Acceder con el usuario y contraseña recien creadas en:
        a. 127.0.0.1:8000/admin o en 
        b. http://localhost:8000/admin

Desde 'localhost:8000/admin' o 'http://127.0.0.1:8000/admin' se puede:
    1. Añadir, modificar o eliminar perfiles 