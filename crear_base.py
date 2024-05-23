from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///demobase.db')

Base = declarative_base()


from sqlalchemy import Column, Integer, String

class Ciudad(Base):

    __tablename__ = 'ciudades'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    region = Column(String)
    docentes = relationship("Docente", back_populates="ciudad")
    

    def __repr__(self):
        return "Ciudad: nombre=%s región:%s" % (
                          self.nombre, 
                          self.region)



class Docente(Base):

    __tablename__ = 'docentes'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    ciudad_id = Column(Integer, ForeignKey('ciudades.id')) 
    ciudad  = relationship("Ciudad", back_populates="docentes")
    

    def __repr__(self):
        return "Docente: nombre=%s apellido=%s ciudad:%s" % (
                          self.nombre, 
                          self.apellido, 
                          self.ciudad)



Base.metadata.create_all(engine)


