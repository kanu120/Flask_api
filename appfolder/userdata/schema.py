from ast import Return, Str
from pickle import FALSE, TRUE
from tkinter.tix import INTEGER
from tokenize import String

from sympy import false, true


#def check(uname):
   # try:
    #    if (int(uname)):
    #        return false
    #except:
    #    return true #if conversion into integer throws an error it means username is a string and is valid

from marshmallow import fields, Schema


class UserSchema(Schema):
    '''User DB Schema'''
   

    username = fields.String(attribute='username')
    password = fields.String(attribute='password')
    email = fields.String(attribute='emailid')
    