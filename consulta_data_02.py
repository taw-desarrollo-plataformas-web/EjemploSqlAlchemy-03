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


print("Ejemplo 2")
print("""Obtener todos los registros de
la tabla docentes que tengan como valor en
el atributo especifico """)

docentes_dos = session.query(Docente).filter(Docente.ciudad=="Loja").all()

print("--------------------------------")
for s in docentes_dos:
    print("%s" % (s))
    print("---------")
print("--------------------------------")
