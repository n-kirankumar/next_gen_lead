from config.next_gen_lead_config import *


class Dealer(Base):
    __tablename__= "dealer"
    userName = Column("username",String, primary_key = True)
    passWord = Column("password",String)