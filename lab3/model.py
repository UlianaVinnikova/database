import datetime
from db import Base, Session, engine
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, ForeignKey, Table

s = Session()

tables = {
    1: 'customer',
    2: 'seller',
    3: 'things',
    4: 'order',
    5: 'order_item',
}

class Customer(Base):
    __tablename__ = 'customer'
    customerID = Column(Integer, primary_key=True)
    name = Column(String)
    gender = Column(String)

    order = relationship("Order")

    def __init__(self, customerID, name, gender):
        self.customerID = customerID
        self.name = name
        self.gender = gender

    def __repr__(self):
        return f"<Customer(customerID={self.customerID}, name={self.name}, gender={self.gender})>"


class Seller(Base):
    __tablename__ = 'seller'
    sellerID = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)

    order = relationship("Order")

    def __init__(self, sellerID, name, surname):
        self.sellerID = sellerID
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"<Seller(sellerID={self.sellerID}, name={self.name}, surname={self.surname})>"


class Things(Base):
    __tablename__ = 'things'
    barcode = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Numeric)

    order_itemID = Column(Integer, ForeignKey('order_item.order_itemID'))

    def __init__(self, barcode, name, price, order_itemID):
        self.barcode = barcode
        self.name = name
        self.price = price
        self.order_itemID = order_itemID

    def __repr__(self):
        return f"<Things(barcode={self.barcode},name={self.name}, price={self.surname})>"


class Order(Base):
    __tablename__ = 'order'
    ordernumber = Column(Integer, primary_key=True)
    ordertime = Column(TIMESTAMP)

    customerID = Column(Integer, ForeignKey('customer.customerID'))
    sellerID = Column(Integer, ForeignKey('seller.sellerID'))

    order_item = relationship("Order_Item")

    def __init__(self, ordernumber, ordertime, customerID, sellerID):
        self.ordernumber = ordernumber
        self.ordertime = ordertime
        self.customerID = customerID
        self.sellerID = sellerID

    def __repr__(self):
        return f"<Order(ordernumber={self.ordernumber}, ordertime={self.ordertime}, customerID={self.customerID}, sellerID={self.sellerID})>"


class Order_Item(Base):
    __tablename__ = 'order_item'
    order_itemID = Column(Integer, primary_key=True)
    count = Column(Integer)

    ordernumber = Column(Integer, ForeignKey('order.ordernumber'))

    things = relationship("Things")

    def __init__(self, order_itemID, count, ordernumber):
        self.order_itemID = order_itemID
        self.count = count
        self.customerID = ordernumber

    def __repr__(self):
        return f"<Order_Item(order_itemID={self.order_itemID}, count={self.count}, ordernumber={self.ordernumber})>"


class Model:
    def __init__(self):
        self.session = Session()
        self.connection = engine.connect()

    @staticmethod
    def show_customer():
        return s.query(Customer.customerID, Customer.name, Customer.gender).all()

    @staticmethod
    def show_seller():
        return s.query(Seller.sellerID, Seller.name, Seller.surname).all()

    @staticmethod
    def show_things():
        return s.query(Things.barcode, Things.name, Things.price, Things.order_itemID).all()

    @staticmethod
    def show_order():
        return s.query(Order.barcode, Order.name, Order.price, Order.customerID, Order.sellerID).all()

    @staticmethod
    def show_order_item():
        return s.query(Order_Item.order_itemID, Order_Item.count, Order_Item.ordernumber).all()

    @staticmethod
    def insert_table1(customerID: int, name: str, gender: str) -> None:
        customer = Customer(customerID=customerID, name=name, gender=gender)
        s.add(customer)
        s.commit()

    @staticmethod
    def insert_table2(sellerID: int, name: str, surname: str) -> None:
        seller = Customer(sellerID=sellerID, name=name, surname=surname)
        s.add(seller)
        s.commit()

    @staticmethod
    def insert_table3(barcode: int, name: str, price: float, order_itemID: int) -> None:
        things = Things(barcode=barcode, name=name, price=price, order_itemID=order_itemID)
        s.add(things)
        s.commit()

    @staticmethod
    def insert_table4(ordernumber: int, ordertime: datetime.datetime, customerID, sellerID) -> None:
        order = Order(ordernumber=ordernumber, ordertime=ordertime, customerID=customerID, sellerID=sellerID)
        s.add(order)
        s.commit()

    @staticmethod
    def insert_table5(order_itemID: int, count: int, ordernumber: int) -> None:
        order_item = Order_Item(order_itemID=order_itemID, count=count, ordernumber=ordernumber)
        s.add(order_item)
        s.commit()

    @staticmethod
    def delete_table1(customerID) -> None:
        customer = s.query(Customer).filter_by(customerID=customerID).one()
        s.delete(customer)
        s.commit()

    @staticmethod
    def delete_table2(sellerID) -> None:
        seller = s.query(Seller).filter_by(sellerID=sellerID).one()
        s.delete(seller)
        s.commit()

    @staticmethod
    def delete_table3(barcode) -> None:
        things = s.query(Things).filter_by(barcode=barcode).one()
        s.delete(things)
        s.commit()

    @staticmethod
    def delete_table4(ordernumber) -> None:
        order = s.query(Order).filter_by(ordernumber=ordernumber).one()
        s.delete(order)
        s.commit()

    @staticmethod
    def delete_table5(order_itemID) -> None:
        order_item = s.query(Order_Item).filter_by(order_itemID=order_itemID).one()
        s.delete(order_item)
        s.commit()

    @staticmethod
    def update_table1(customerID: int, name: str, gender: str) -> None:
        s.query(Customer).filter_by(customerID=customerID).update({Customer.name: name, Customer.gender: gender})
        s.commit()

    @staticmethod
    def update_table2(sellerID: int, name: str, surname: str) -> None:
        s.query(Seller).filter_by(sellerID=sellerID).update({Seller.name: name, Seller.surname: surname})
        s.commit()

    @staticmethod
    def update_table3(barcode: int, name: str, price: float) -> None:
        s.query(Things).filter_by(barcode=barcode).update({Things.name: name, Things.price: price})
        s.commit()

    @staticmethod
    def update_table4(ordernumber: int, ordertime: datetime.datetime) -> None:
        s.query(Order).filter_by(ordernumber=ordernumber).update({Order.ordertime: ordertime})
        s.commit()

    @staticmethod
    def update_table5(order_itemID: int, count: int) -> None:
        s.query(Order_Item).filter_by(order_itemID=order_itemID).update({Order_Item.count: count})
        s.commit()