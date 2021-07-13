#!/usr/bin/python3
#     Revision: 0.0.1     Modtime: 03/10/21 02:30 pm     Author: Mustafa Al Ogaidi
#
#   Python module:
#
#      GFS_DBI
#
#   Description:
#
#      Wrapper to the Perl standard DataBase Interface that allows for
#      driver-specific defaults for database connection.
#
#   Copyright (C) 2021, WSI Corporation
#
#   These coded instructions, statements, and computer programs contain
#   unpublished proprietary information of WSI Corporation, and are
#   protected by Federal copyright law.  They may not be disclosed
#   to third parties or copied or duplicated in any form, in whole or
#   in part, without the prior written consent of WSI Corporation.
#
#------------------------------------------------------------------------------

import sys,os,re
import fileinput,subprocess,inspect
import psycopg2
from psycopg2 import pool
from os import environ

class GFS_DBI:
   #
   #  Default member values assuming the database is PostgreSQL
   #
   __connection_pool = None

   if environ.get('GFS_DB_DRIVER') is not None:
      designated_driver=os.environ['GFS_DB_DRIVER']
   default_driver='Pg'
   if environ.get('PGDATABASE') is not None:
      default_database={'Pg': os.environ['PGDATABASE']}
      database = default_database
   if environ.get('PGHOST') is not None:
      default_hostname={'Pg': os.environ['PGHOST']}
      host = default_hostname
   if environ.get('PGUSER') is not None:
      default_user={'Pg': os.environ['PGUSER']}
      user = default_user
   default_password={'Pg': ''}
   password = default_password

   @classmethod
   def initialise(cls):
      cls.__connection_pool = pool.SimpleConnectionPool(1, 
                                                       10, 
                                                       database="gfsv10",
                                                       user="postgres",
                                                       password="RDS4Gris",
                                                       host="skybase-2-dev.cv9bnu4vuygm.us-east-1.rds.amazonaws.com")
      print("cls.__connection_pool = ", cls.__connection_pool)
      if not cls.__connection_pool:
        return None
      else:
        return "Connected"


   @classmethod
   def get_connection(cls):
      return cls.__connection_pool.getconn()

   @classmethod
   def return_connection(cls, connection):
      cls.__connection_pool.putconn(connection)

   @classmethod
   def close_all_connection(cls):
      cls.__connection_pool.closeall()
  
class CursorFromConnectionFromPool:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):    # where with begin
        self.connection = GFS_DBI.get_connection()
        if self.connection != None:
           self.cursor = self.connection.cursor()
           return self.cursor
        return None

    def __exit__(self, exception_type, exception_value, exception_traceback):  # return connection when with end
        if exception_value is not None:     # e.g. TypeError, AttributeError, ValueError
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        GFS_DBI.return_connection(self.connection)


if __name__ == "__main__":
   GFS_DBI.initialise()
   with CursorFromConnectionFromPool() as cursor:
      cursor.execute('select * from timezones limit 10')  # here the email is inside tuple
      user_data = cursor.fetchall()  # this function is retrieve only one
      # return new object :)
      #print("email= " + user_data[1] + "first_name= " + user_data[2] + "last_name= " + user_data[3] + "id= " + user_data[0])
      print(user_data)