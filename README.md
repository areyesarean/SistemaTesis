# Sistema de gestión de donaciones de sangre

Copyright (2020) Universidad de Granma

This file is part of Faculty Activity Management System.

SGDS is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

CTI is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with CTI.  If not, see <http://www.gnu.org/licenses/>.

------------------------------------------------------------------------------------

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
    * si no se ha instalado python3-venv, instalalarlo ejecutando 
        ```sh 
        sudo apt-get install python3-venv
        ```
    * crear el entorno ejecutando 
        ```sh
        python3 -m venv venv
        ```
      Esto crea una carpeta venv con todos los archivos necesarios. Para más información visite [**Python Docs**](https://docs.python.org/3/tutorial/venv.html)
    * Activar el entorno virtual ejecutando 
        ```sh
        cd venv/bin/Script/activate
        ```
    
3. Despues de creado el entorno virtual y activado, es necesario satisfacer previamente algunas dependencias de la libreria django_auth_ldap usada en el proyecto.

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

