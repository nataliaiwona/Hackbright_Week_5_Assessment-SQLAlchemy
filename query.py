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

# -------------------------------------------------------------------
# Part 2: Write queries


# # Get the brand with the **id** of 8.
# Brand.query.get(8)

# # Get all models with the **name** Corvette and the **brand_name** Chevrolet.
# Model.query.filter_by(name="Corvette", brand_name="Chevrolet").all()

# # Get all models that are older than 1960.
# Model.query.filter(Model.year < 1960).all()

# # Get all brands that were founded after 1920.
# Brand.query.filter(Brand.founded > 1920).all()

# # Get all models with names that begin with "Cor".
# Model.query.filter(Model.name.like('Cor%')).all()

# # Get all brands that were founded in 1903 and that are not yet discontinued.
# Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()

# # Get all brands that are either 1) discontinued (at any time) or 2) founded
# # before 1950.
# Brand.query.filter(Brand.discontinued != None, Brand.founded < 1950).all()

# # Get all models whose brand_name is not Chevrolet.
# Model.query.filter(Model.brand_name != "Chevrolet").all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    model_year_info = db.session.query(Model.name, Model.brand_name, 
                      Brand.headquarters).join(Brand).filter(
                      Model.year == year).all()

    for name, brand_name, headquarters in model_year:
        print "Model name is {0}, brand is {1}. {1}'s headquarters are located in {2}.".format(
            name, brand_name, headquarters)


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brand_summary = db.session.query(Model.brand_name,
                    Model.name).order_by(Model.brand_name).all()

    for brand_name, name in brand_summary:
        print "Brand: {} | Model: {}".format(brand_name, name)

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of
# ``Brand.query.filter_by(name='Ford')``?

# Returned value: [<Brand id=1 name=Ford founded=1903 headquarters=Dearborn, MI discontinued=None>]
# Datatype: Object list

# 2. In your own words, what is an association table, and what *type* of
# relationship does an association table manage?

# An association table is a many to many relationship. Ex. we have two tables
# that do not share any foreign keys, but we need to be able to access the data
# within each respective table. Enter the association table. This table does not have
# any "important" data. It is merely a tool used to associate the other two tables
# to each other. These tables are usually named by smashing the other two table names
# together. 

# I like to think of it as Jane and Bobby don't know each other, but they both know
# Tom. Tom's only job is to introduce J & B and show they can relate to each other. 
# Otherwise, we don't care about Tom.
# Sorry, Tom.

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    
    result = Brand.query.filter((Brand.name == "mystr") | 
            (Brand.name.like('%mystr%'))).all()
    return result


def get_models_between(start_year, end_year):
    
    result = Model.query.filter(Model.year >= start_year, 
                                Model.year < end_year).all()
    return result





