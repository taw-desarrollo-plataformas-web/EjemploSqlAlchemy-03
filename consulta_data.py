from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

# se importa la clase(s) del 
# archivo genera_tablas
from crear_base import Docente 

# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite

engine = create_engine('sqlite:///demobase.db')


Session = sessionmaker(bind=engine)
session = Session()

print("EJEMPLOS DE CONSULTAS")

print("Ejemplo 1")
print("""Obtener todos los registros de 
la entidad docentes """)
docentes = session.query(Docente).all() # [docente1, docente2, docente3]

# Se recorre la lista a través de un ciclo
# repetitivo for en python
print("Presentación de todos los Docentes")

print("--------------------------------")
for s in docentes:
    print("%s" % (s))
    print("---------")

print("--------------------------------")

print("Ejemplo 2")
print("""Obtener todos los registros de 
la tabla docentes que tengan como valor en 
el atributo especifico """)

docentes_dos = session.query(Docente).filter(Docente.ciudad=="Loja").all()

print("--------------------------------")
print(docentes_dos)
print("--------------------------------")

print("Ejemplo 3")
print("--------------------------------")
print("""Obtener todos los registros de·
la tabla Docente ordenados por el atributo especifico""")

docentes_tres = session.query(Docente).order_by(Docente.nombre).all()

print("--------------------------------")
print(docentes_tres)
print("--------------------------------")


print("Ejemplo 4")
print("""Obtener todos los registros de·
la tabla Docente que tengan el atributo ciudad un valor de Loja y 
se ordenen por el atributo de la clase Docente nombre""")

docentes = session.query(Docente).filter(Docente.ciudad=="Loja").order_by(Docente.nombre).all()
print("--------------------------------")
print(docentes)
print("--------------------------------")


print("Ejemplo 6")
print("""Obtener todos los registros de·
la tabla Docente que tengan el atributo ciudad igual a None y 
se ordenen por el atributo de la clase Docente nombre""")

docentes = session.query(Docente).filter(Docente.ciudad!=None).order_by(Docente.nombre).all()

print("--------------------------------")
print(docentes)
print("--------------------------------")


print("Ejemplo 7")
print("""Obtener todos los registros de·
la tabla Docente que tengan el atributo ciudad igual a Loja y además valor 
del atributo nombre sea diferente de None. 
Finalmente que se ordenen por el atributo de la clase Docente nombre""")

docentes = session.query(Docente).filter(Docente.ciudad=="Loja", Docente.nombre!=None).order_by(Docente.nombre).all() 

print("--------------------------------")
print(docentes)
print("--------------------------------")


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


print("Ejemplo 9")
print("""Uso de and_
Obtener todos los registros de·
la tabla Docente que tengan dentro del valor del atributo ciudad  
la cadena "oja" y 
el atributo nombre sea diferente de None. 
Finalmente que se ordenen por el atributo de la clase Docente nombre""")

docentes = session.query(Docente).filter(and_(Docente.ciudad.like("%oja%"), Docente.nombre!=None)).order_by(Docente.nombre).all()  

print("--------------------------------")
print(docentes)
print("--------------------------------")

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


print("Ejemplo 11")
print("""Uso de or_
Obtener todos los registros de·
la tabla Docente que tengan el valor de apellido igual a Minga  
o que el apellido sea Garcia
Finalmente que se ordenen por el atributo de la clase Docente nombre""")


docentes = session.query(Docente).filter(or_(Docente.apellido=="Minga", Docente.apellido=="García")).order_by(Docente.nombre).all() 

print("--------------------------------")
print(docentes)
print("--------------------------------")







