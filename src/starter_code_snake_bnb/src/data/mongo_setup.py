import mongoengine

alias_core = 'core'
db = 'snake_db'
connection_string = u'mongodb://SoundsSelect:beatsbyer@testcluster-9feub.azure.mongodb.net/test?retryWrites=true&w=majority'


# connection string:
# mongodb+srv://SoundsSelect:<password>@testcluster-9feub.azure.mongodb.net/test?retryWrites=true&w=majority

def global_setup():
    mongoengine.register_connection(
        alias=alias_core,
        name=db,
        username='SoundsSelect',
        password='beatsbyer',
        host=connection_string,
    )
