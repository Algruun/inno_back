from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Table, Float
from sqlalchemy.orm import relationship

from database import Base

# order_items_table = Table('order_items', Base.metadata,
#                           Column('order_id', Integer, ForeignKey('order.id')),
#                           Column('pizza_id', Integer, ForeignKey('pizza.id'))
#                           )


# class User(Base):
#     __tablename__ = "users"
#
#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)
#
#     items = relationship("Item", back_populates="owner")


class Pizza(Base):
    __tablename__ = "pizza"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float)
    sku = Column(String)
    is_active = Column(Boolean, default=True)
    updated_at = Column(DateTime)


# class Order(Base):
#     __tablename__ = "order"
#
#     id = Column(Integer, primary_key=True, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))
#     created_at = Column(DateTime)
#
#     items = relationship("Child", secondary=order_items_table)
#     owner = relationship("User", back_populates="order")
