from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, LargeBinary, DateTime, Boolean
from sqlalchemy.orm import relationship
import datetime


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    icon = Column(LargeBinary, nullable=True)
    name = Column(String)
    phone_number = Column(String(10), nullable=False, unique=True)
    otp = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    is_active = Column(Boolean, default=True)


class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    vehicle_number = Column(String(50), nullable=False, unique=True)
    vehicle_make = Column(String(50), nullable=False)
    vehicle_model = Column(String(50), nullable=False)

    user = relationship('User', backref='vehicles')


class Wallet(Base):
    __tablename__ = 'wallets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    balance = Column(Integer, nullable=False, default=0)
    wallet_number = Column(String(50), nullable=False, unique=True)

    user = relationship('User', backref='wallets')
