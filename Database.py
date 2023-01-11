from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, update

# Här skapas en superklass som innehåller anslutningen till och själva motorn för databasen


class Database1:

    engine = create_engine('sqlite:///mydb39.db')
    Session = sessionmaker(bind=engine)
    Base = declarative_base()

# Subklass till Database1 ärver Base


class Medlem(Database1.Base):
    # Skapar ett table med sju stycken attribut per objekt
    __tablename__ = 'medlemmar'

    id = Column(Integer, primary_key=True)
    förnamn = Column(String)
    efternamn = Column(String)
    gatuadress = Column(String)
    postnummer = Column(Integer)
    postadress = Column(String)
    avgift = Column(String)

    def __init__(self, förnamn, efternamn, gatuadress, postnummer, postadress, avgift):
        self.förnamn = förnamn
        self.efternamn = efternamn
        self.gatuadress = gatuadress
        self.postnummer = postnummer
        self.postadress = postadress
        self.avgift = avgift

# Skapar tablet medlemmar i databasen

    @classmethod
    def create_database_table(cls):
        Database1.Base.metadata.create_all(Database1.engine)




