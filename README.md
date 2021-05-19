<!--
*** Se usa como template - https://github.com/othneildrew/Best-README-Template
-->


[![PyPI download month](https://img.shields.io/pypi/dm/sqlalchemy.svg)](https://pypi.python.org/pypi/sqlalchemy/)



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/taw-desarrollo-plataformas-web/EjemploSqlAlchemy-02">
    <img src="https://www.sqlalchemy.org/img/sqla_logo.png" alt="Logo">
  </a>

  <h3 align="center">Ejemplo de uso de la SqlAlchemy</h3>

  <p align="center">
Es un repositorio académico que permite ejemplificar el proceso de creación de entidades, ingreso y consulta de información a través de la SqlAlchemy. 
 <a href="https://www.sqlalchemy.org/">SqlAlchemy</a>
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
    <li><a href="#usos">Usos</a></li>
    <li><a href="#licencia">Licencia</a></li>
    <li><a href="#contacto">Contacto</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## Sobre el proyecto

Es un repositorio académico que permite ejemplificar el proceso de creación de entidades, ingreso y consulta de información a través de la SqlAlchemy.


<!-- GETTING STARTED -->
## Inicio del proyecto

Para poder usar el presente proyecto, tomar en consideración lo siguiente:

### Prerrequisitos

* Instalar [Python](https://www.python.org/) 
* Instalar [SQLAlchemy](https://www.sqlalchemy.org/) 
  ```
  	pip install SQLAlchemy
  ```

### Instalación

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

``` python
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
```

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

René Elizalde - [@reroes](https://twitter.com/reroes) - rrelizalde@utpl.edu.ec

Project Link: [https://github.com/taw-desarrollo-plataformas-web/EjemploSqlAlchemy-02](https://github.com/taw-desarrollo-plataformas-web/EjemploSqlAlchemy-02)


