#!/usr/local/env python
# -*- coding: utf-8 -*-

from .base import Base
from app.models import User

class UserService(Base):
    __model__ = User

users = UserService()