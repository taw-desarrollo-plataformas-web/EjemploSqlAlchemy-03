<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** github_username, repo_name, twitter_handle, email, project_title, project_description
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/taw-desarrollo-plataformas-web/EjemploSqlAlchemy-02">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Ejemplo de uso de la SqlAlchemy</h3>

  <p align="center">
Es un repositorio académico que permite ejemplificar el proceso de creación de entidades, ingreso y consulta de información a través de la SqlAlchemy.
    <br />
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Índice</h2></summary>
  <ol>
    <li>
      <a href="#sobre-el-proyecto">Sobre el proyecto</a>
     </li>
    <li>
      <a href="#Inicio-del-proyecto">Inicio del proyecto</a>
      <ul>
        <li><a href="#prerrequisitos">Prerrequisitos</a></li>
        <li><a href="#instalacion">Instalación</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## Sobre el proyecto

Es un repositorio académico que permite ejemplificar el proceso de creación de entidades, ingreso y consulta de información a través de la SqlAlchemy.

Here's a blank template to get started:
**To avoid retyping too much info. Do a search and replace with your text editor for the following:**
`github_username`, `repo_name`, `twitter_handle`, `email`, `project_title`, `project_description`


<!-- GETTING STARTED -->
## Inicio del proyecto

Para poder usar el presente proyecto, tomar en consideración lo siguiente:

### Prerrequisitos

* Instalar Python 3.x
* Instalar SQLAlchemy
  ```
  	pip install SQLAlchemy
  ```

### Installation

* Opción a. Clonar el repositorio
   ```sh
   git clone https://github.com/taw-desarrollo-plataformas-web/EjemploSqlAlchemy-02
   ```
o

* Opción b. Descargar la carpeta comprimida del repositorio


<!-- USAGE EXAMPLES -->
## Usos

* En el archivo consulta_data.py se detallan algunas consultas generadas con SqlAlchemy

```python
print("Ejemplo 1")
print("""Obtener todos los registros de 
la entidad docentes """)
docentes = session.query(Docente).all() # [docente1, docente2, docente3]
```

```python
print("Ejemplo 2")
print("""Obtener todos los registros de 
la tabla docentes que tengan como valor en 
el atributo especifico """)

docentes_dos = session.query(Docente).filter(Docente.ciudad=="Loja").all()

```
```python
print("Ejemplo 4")
print("""Obtener todos los registros de·
la tabla Docente que tengan el atributo ciudad un valor de Loja y 
se ordenen por el atributo de la clase Docente nombre""")

docentes = session.query(Docente).filter(Docente.ciudad=="Loja").order_by(Docente.nombre).all()
print("--------------------------------")
print(docentes)
print("--------------------------------")
```

```python
print("Ejemplo 7")
print("""Obtener todos los registros de·
la tabla Docente que tengan el atributo ciudad igual a Loja y además valor 
del atributo nombre sea diferente de None. 
Finalmente que se ordenen por el atributo de la clase Docente nombre""")

docentes = session.query(Docente).filter(Docente.ciudad=="Loja", Docente.nombre!=None).order_by(Docente.nombre).all() 

print("--------------------------------")
print(docentes)
print("--------------------------------")

```
print("Ejemplo 8")
print("""Obtener todos los registros de·
la tabla Docente que tengan dentro del valor del atributo ciudad  
la cadena "oja" y 
el atributo nombre sea diferente de None. 
Finalmente que se ordenen por el atributo de la clase Docente nombre""")

docentes = session.query(Docente).filter(Docente.ciudad.like("%oja%"), Docente.nombre!=None).order_by(Docente.nombre).all() 
print("--------------------------------")
print(docentes)
print("--------------------------------")


```python

print("Ejemplo 10")
print("""Uso de in_
Obtener todos los registros de·
la tabla Docente que tengan el valor del atributo apellido  
en la lista dada ["Minga", "Borrero"]
Finalmente que se ordenen por el atributo de la clase Docente nombre""")


docentes = session.query(Docente).filter(Docente.apellido.in_(['Minga', 'Borrero', "Elizalde"])).order_by(Docente.nombre).all()
 
print("--------------------------------")
print(docentes)
print("--------------------------------")


```

<!-- LICENSE -->
## Licencia

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contacto

René Elizalde - [@twitter_handle](https://twitter.com/reroes) - rrelizalde@utpl.edu.ec

Project Link: [https://github.com/taw-desarrollo-plataformas-web/EjemploSqlAlchemy-02](https://github.com/taw-desarrollo-plataformas-web/EjemploSqlAlchemy-02)


