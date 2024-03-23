#!/usr/bin/python3

""" creates the State “California” with the City “San Francisco”
    from the database hbtn_0e_100_usa
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """ Main function
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2],
                                   argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = State(name="California")
    city = City(name="San Francisco")

    state.cities.append(city)
    session.add(state)
    session.add(city)

    session.commit()
    session.close()


if __name__ == "__main__":
    main()
