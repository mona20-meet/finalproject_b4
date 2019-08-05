from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Coupons(Base):


	__tablename__= "coupons"
	company= Column(String)
	catagory=Column(String, primary_key=True)
	number=Column(Integer)
	location=Column(String)
	def __repr__(self):
		return ("company: {}\n"
				"catagory: {} \n"
				"number of people: {} \n"
				"location: {}").format(
					self.company, self.catagory, self.number, self.location)

coupon1 = Coupons(company='pizza hut',catagory='food',number='5',location='tel aviv')

