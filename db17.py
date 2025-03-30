from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.exc import IntegrityError


DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/inventory"


Base = declarative_base()


class Category(Base):
   __tablename__ = 'categories'
   id = Column(Integer, primary_key=True)
   name = Column(String, nullable=False)

class Supplier(Base):
   __tablename__ = 'suppliers'
   id = Column(Integer, primary_key=True)
   name = Column(String, nullable=False)
   address = Column(String)

class Product(Base):
   __tablename__ = 'products'
   id = Column(Integer, primary_key=True)
   name = Column(String, nullable=False)
   price = Column(Numeric(10, 2), nullable=False)
   stock_quantity = Column(Integer, nullable=False)
   category_id = Column(Integer, ForeignKey('categories.id'))
   supplier_id = Column(Integer, ForeignKey('suppliers.id'))

   category = relationship("Category")
   supplier = relationship("Supplier")

class SupplyOrder(Base):
   __tablename__ = 'supply_orders'
   id = Column(Integer, primary_key=True)
   product_id = Column(Integer, ForeignKey('products.id'))
   supplier_id = Column(Integer, ForeignKey('suppliers.id'))
   quantity = Column(Integer, nullable=False)


def init_db17():
   engine = create_engine(DATABASE_URL)
   Base.metadata.create_all(engine)


def get_all_products(session):
   return session.query(Product).all()

def get_all_suppliers(session):
   return session.query(Supplier).all()

def get_product_full_info_by_id(session, product_id):
   return session.query(Product).filter(Product.id == product_id).first()

def create_product(session, name, price, stock_quantity, category_id, supplier_id):
   new_product = Product(name=name, price=price, stock_quantity=stock_quantity, category_id=category_id, supplier_id=supplier_id)
   session.add(new_product)
   try:
       session.commit()
   except IntegrityError:
       session.rollback()
       raise

def search_product(session, query):
   return session.query(Product).filter(Product.name.ilike(f"%{query}%")).all()