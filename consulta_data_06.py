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

# Se recorre la lista a través de un ciclo
# repetitivo for en python
print("Presentación de todos los Docentes")



print("Ejemplo 6")
print("""Obtener todos los registros de·
la tabla Docente que tengan el atributo ciudad diferente a None y
se ordenen por el atributo de la clase Docente nombre""")

docentes = session.query(Docente).filter(Docente.ciudad!=None)\
        .order_by(Docente.nombre).all()

print("--------------------------------")
for s in docentes:
    print("%s" % (s))
    print("---------")

print("--------------------------------")
