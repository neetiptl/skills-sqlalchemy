"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

-------------------------------------------------------------------
Start here.


Part 2: Write queries

# Get the brand with the **id** of 8.
car = Model.query.filter_by(id=8).first()
car.brand_name

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
car = db.session.query(Model).filter(Model.brand_name == 'Chevrolet', Model.name == 'Corvette').all()

# Get all models that are older than 1960.
models = Model.query.filter(Model.year < 1960).all()
# Get all brands that were founded after 1920.
brands = Brand.query.filter(Brand.founded >1920).all()
# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like('Cor%')).all()
# Get all brands with that were founded in 1903 and that are not yet discontinued.
Brand.query.filter(Brand.founded==1903, Brand.discontinued== None).all()
# Get all brands with that are either discontinued or founded before 1950.
Brand.query.filter((Brand.discontinued != None)|(Brand.founded<1950)).all()
# Get any model whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name!='Chevrolet').all()
# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    x = Model.query.filter_by(year=year).all()
    for car in x:
        print car.name, car.brand_name, car.brand.headquarters
     
get_model_info(1960)

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''
    
     x = Brand.query(Brand.name).all()
    for model in brand:
        print "Brand: {}, Models: {}"

# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    pass


def get_models_between(start_year, end_year):
    pass

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
# <flask_sqlalchemy.BaseQuery object at 0x10a969bd0> ==> object containing 
#  <Model id=1 name=Ford founded=1903 headquarters=Dearborn, MI discontinued=None >

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
# An association table is a table that contains common fields 
#from 2 other tables in the same database. It is used to create 
#a many-to-many relationship between tables.
