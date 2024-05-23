from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

# se importa la clase(s) del
# archivo genera_tablas
from crear_base import Docente, Ciudad

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
la entidad Ciudad""")
ciudades = session.query(Ciudad).all() # 

print("Presentación de las ciudades")

print("--------------------------------")
for s in ciudades:
    print("%s" % (s))
    print("---------")
