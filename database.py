import sqlalchemy
import os

from sqlalchemy import create_engine, text

db_connection_string = os.environ['DB_CONNECTION_STRING']



# SQLAlchemy engine object that connects to a MySQL database using the PyMySQL driver.
# format
# mysql+pymysql://<username>:<password>@<host>/<dbname>
# installed pymysql


engine = create_engine(db_connection_string, 
                      connect_args={
                        "ssl":{
                          "ssl_ca": "/etc/ssl/cert.pem"
                        }
                      })

# print(sqlalchemy.__version__)


# helper function 
def load_jobs_from_db():
    with engine.connect() as conn:  # Connect to the database using the engine
        result = conn.execute(text("select * from jobs"))  # Execute SQL query to select all rows from the 'jobs' table
        jobs = []
        for row in result.all():  # Iterate over the result rows
            jobs.append(dict(row._asdict()))  # Convert each row to a dictionary and append to the 'jobs' list
        return jobs  # Return the list of job dictionaries


  
#   print("type(result):", type(result))
#   result_all = result.all()
#   print("type(result.all()):",type(result_all))
#   # print(result_all[0])
#   first_result = result_all[0]
#   print("type(first_result):", type(first_result))

# # convert row object to dictionary
#   first_result_dict = result_all[0]._asdict()
#   # or first_result_dict = result_all[0]._mapping
  
#   print("type(first_result_dict):", type(first_result_dict))
#   print(first_result_dict)
 