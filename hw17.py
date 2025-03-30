
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/inventory"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category", back_populates="products")

class Supplier(Base):
    __tablename__ = 'suppliers'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    products = relationship("Product", back_populates="category")

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    order_number = Column(String)


Base.metadata.create_all(engine)

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

# Функции для добавления, удаления и редактирования элементов
def add_item(item):
    session.add(item)
    session.commit()
    print(f"Добавлен элемент: {item}")

def remove_item(item):
    session.delete(item)
    session.commit()
    print(f"Удален элемент: {item}")

def edit_item(old_item, new_item):
    if isinstance(old_item, Product):
        old_item.name = new_item.name
        old_item.category_id = new_item.category_id
    elif isinstance(old_item, Supplier):
        old_item.name = new_item.name
    elif isinstance(old_item, Category):
        old_item.name = new_item.name
    elif isinstance(old_item, Order):
        old_item.order_number = new_item.order_number
    session.commit()
    print(f"Отредактирован элемент: от {old_item} до {new_item}")

# Пример использования
product = Product(name="Продукт A", category_id=1)
supplier = Supplier(name="Поставщик 1")
category = Category(name="Категория X")
order = Order(order_number="Заказ #1")

add_item(product)
add_item(supplier)
add_item(category)
add_item(order)

# Редактирование
edited_product = Product(name="Продукт B", category_id=1)
edit_item(product, edited_product)

# Удаление
remove_item(supplier)

session.close()