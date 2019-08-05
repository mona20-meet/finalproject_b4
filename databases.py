from model import Base, Coupons

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_coupon(company,catagory,number,location):
	new_coupon= Coupons(company=company,catagory=catagory,number=number,location=location)
	session.add(new_coupon)
	session.commit()

def query_all_coupons():
	articles= session.query(
		Coupons).all()
	return articles


def query_coupon_by_catagory(catagory):
	coupon = session.query(
		Coupons).filter_by(
		catagory=catagory).first()
	return coupon


