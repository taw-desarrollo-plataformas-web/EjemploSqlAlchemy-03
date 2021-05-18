from sqlalchemy import create_engine

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///demobase.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String

class Docente(Base):

    __tablename__ = 'docentes'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    ciudad = Column(String, nullable=False) # este atributo no puede ser nulo
    

    def __repr__(self):
        return "Docente: nombre=%s apellido=%s ciudad:%s" % (
                          self.nombre, 
                          self.apellido, 
                          self.ciudad)

Base.metadata.create_all(engine)


