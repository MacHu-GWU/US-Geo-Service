##encoding=utf-8

"""
Import Command
--------------
    from util.database import engine, zipcodes
"""

from angora.SQLITE import *
import os

def find_db_path():
    """find the database file (name = StandardZipcode.sqlite) in current dir and it's sub folder
    """
    cwd = os.getcwd()
    for current_dir, folder_list, fname_list in os.walk(cwd):
        for fname in fname_list:
            if fname == "StandardZipcode.sqlite":
                fullpath = os.path.join(current_dir, fname)
                abspath = os.path.abspath(fullpath)
                return abspath
    raise Exception("Cannot find StandardZipcode.sqlite database file")

metadata = MetaData()
datatype = DataType()
engine = Sqlite3Engine(find_db_path(), autocommit=False)
zipcodes = Table("zipcodes", metadata,
            Column("zipcode", datatype.text, primary_key=True),
            Column("city", datatype.text),
            Column("state", datatype.text),
            Column("la", datatype.real),
            Column("lg", datatype.real),
            )
metadata.create_all(engine)
