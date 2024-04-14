from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Person(Base):
    __tablename__ = 'people'

    ssn = Column('ssn', Integer, primary_key=True)
    firstname = Column('firstname', String)
    lastname = Column('lastname', String)
    gender = Column('gender', CHAR)
    age = Column('age', Integer)

    def __init__(self, ssn, first, last, gender, age):
        self.ssn = ssn
        self.firstname = first
        self.lastname = last
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f'({self.ssn}) {self.firstname} {self.lastname} ({self.gender}, {self.age})'

class Thing(Base):
    __tablename__ = 'Things'

    tid = Column('tid', Integer, primary_key=True)
    description = Column('description', String)
    owner = Column(Integer, ForeignKey('people.ssn'))

    def __init__(self, tid, description, owner):
        self.tid = tid
        self.description = description
        self.owner = owner

    def __repr__(self):
        return f'({self.tid}) {self.description} ({self.owner})'

engine = create_engine('sqlite:///mydb.db', echo=True)

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

# person1 = Person(12312, 'Mike', 'Smith', 'M', 35)
# session.add(person1)
# session.commit()

# p1 = Person(12452, 'Anna', 'Blue', 'F', 48)
# p2 = Person(11312, 'Bob', 'Blue', 'M', 35)
# p3 = Person(12341, 'Angela', 'Colt', 'F', 22)

# session.add(p1)
# session.add(p2)
# session.add(p3)
# session.commit()

# t1 = Thing(1, 'Car', p1.ssn)
# t2 = Thing(2, 'Hot Cross Bun', p2.ssn)
# t3 = Thing(3, 'Cold Cross Bun', p2.ssn)
# t4 = Thing(4, 'Cat', p3.ssn)
# t5 = Thing(5, 'Calendar', person1.ssn)
# t6 = Thing(6, 'Laptop', p1.ssn)
# t7 = Thing(7, 'Kendama', p3.ssn)
# t8 = Thing(8, 'License Plate', person1.ssn)

# session.add(t1)
# session.add(t2)
# session.add(t3)
# session.add(t4)
# session.add(t5)
# session.add(t6)
# session.add(t7)
# session.add(t8)
# session.commit()


# results = session.query(Person).all() # select * from people

results = session.query(Thing, Person).filter(Thing.owner == Person.ssn).filter(Person.firstname == 'Anna').all() # filter with where

for r in results:
    print(r)