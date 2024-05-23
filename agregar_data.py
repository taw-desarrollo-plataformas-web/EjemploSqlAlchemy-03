from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from crear_base import Docente, Ciudad
# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///demobase.db')


Session = sessionmaker(bind=engine)
session = Session()

ciudad1 = Ciudad(nombre="Loja", region="Sierra")
ciudad2 = Ciudad(nombre="Cuenca", region="Sierra")
ciudad3 = Ciudad(nombre="Guayaquil", region="Costa")
ciudad4 = Ciudad(nombre="Esmeraldas", region="Costa")
ciudad5 = Ciudad(nombre="Zamora", region="Oriente")
ciudad6 = Ciudad(nombre="Puyo", region="Oriente")

# se crea un objetos de tipo Docente 
docente1 = Docente(nombre="Tony", apellido="García", \
        ciudad=ciudad1)

docente2 = Docente(nombre="Luis", apellido="Borrero", \
        ciudad=ciudad2)

docente3 = Docente(nombre="Ana", apellido="Salcedo", \
        ciudad=ciudad3)

docente4 = Docente(nombre="Monica", apellido="Valenzuela", \
        ciudad=ciudad4)

docente5 = Docente(nombre="Luz", apellido="Murillo", \
        ciudad=ciudad5)

docente6 = Docente(nombre="José", apellido="Hidalgo", \
        ciudad=ciudad6)

docente7 = Docente(nombre="Marco", apellido="Dávila", \
        ciudad=ciudad6)

docente8 = Docente(nombre="Hilda", apellido="Sarango", \
        ciudad=ciudad1)




# se agrega los objetos
# a la sesión
# a la espera de un commit
# para agregar un registro a la base de 
# datos
session.add(docente1)
session.add(docente2)
session.add(docente3)
session.add(docente4)
session.add(docente5)
session.add(docente6)
session.add(docente7)
session.add(docente8)
session.add(ciudad1)
session.add(ciudad2)
session.add(ciudad3)
session.add(ciudad4)
session.add(ciudad5)
session.add(ciudad6)

# se confirma las transacciones
session.commit()


