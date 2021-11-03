# Sistema de gestión de donaciones de sangre

Requisitos
--------------
* PostgresSQL 10+
* Python 3.8+

Instalación
--------------

1. Clonar el proyecto o descargarlo como zip
    * Usando HTTP 
        ```sh
        git clone https://github.com/areyesarean/SistemaTesis.git
        ```
    * Usando SSH 
        ```sh
        git clone git@github.com:areyesarean/SistemaTesis.git
        ```

2. Crear un entorno virtual de Python 3.8+ en la carpeta del proyecto, al mismo nivel de las carpetas udg

    * crear el entorno ejecutando 
        ```sh
        python -m venv venv
        ```
      Esto crea una carpeta venv con todos los archivos necesarios. Para más información visite [**Python Docs**](https://docs.python.org/3/tutorial/venv.html)
    * Activar el entorno virtual ejecutando 
        ```sh
        cd venv/bin/script/activate
        ```
    
3. Despues de creado el entorno virtual y activado, es necesario satisfacer previamente algunas dependencias de la librerías usadas en el proyecto.

    * Instalar las dependencias con el comando:
        ```sh 
        pip install -r udg/requirements.txt
        ```
4. Crear en postgres un rol de nombre postgres y password Admin123*
5. Crear la base de datos con nombre bloodbank y propietario el usuario previamente creado

8. Generar la estructura de la base de datos ejecutando: 
    ```sh 
    python udg/manage.py migrate
    ```
   * Para crear un usuario inicial ejecutar:
    ```sh
    python udg/manage.py createsuperuser
    ```
   y siga las intrucciones

9. Finalmente ejecutar el servidor de desarrollo: 
    ```sh
    python udg/manage.py runserver
    ```
    Nota: el 8000 es el puerto por defecto, en caso de estar en uso se puede utilizar otro puerto libre
    ```sh
    python udg/manage.py runserver numero_puerto
    ```
    Verifique que el puerto esté disponible: [IANA](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)

