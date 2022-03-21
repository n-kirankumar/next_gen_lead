from config.next_gen_lead_config import *

class Table22(Base):
    __tablename__ = "table22"
    date = Column("date",Date)
    Name = Column("name", String)
    Mob = Column("mob", String, primary_key=True)
    Email = Column("email", String)
    Full_addr = Column("full_addr", String)


