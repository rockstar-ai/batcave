import snowflake.connector
import sys
import time
import emoji
domain="visualbi"
welcome="Connecting to "+domain +" Snowflake......\n"
for char in welcome:
    sys.stdout.write(char)
    time.sleep(0.2)
con = snowflake.connector.connect(
  user='*******',
  password='*************',
  account=domain+'.east-us-2.azure',
  warehouse='SF_TRYOUTS_WH',
  database='SF_TRYOUTS',
  schema='COE_TRYOUTS'
)
complete="Connection Successful.... "
for char in complete:
    sys.stdout.write(char)
    time.sleep(0.2)
success=(emoji.emojize('\nWelcome to '+domain+' snowflake :thumbsup:', use_aliases=True))
for char in success:
    sys.stdout.write(char)
    time.sleep(0.2)
tablename="std_table"
createtable="\nBeginning to Create table - "+tablename
for char in createtable:
    sys.stdout.write(char)
    time.sleep(0.2)

# cur = con.cursor().execute("SELECT * FROM TEST_STAGE_WORKING")
# ret = cur.fetchmany(3)
# print(ret)
# while len(ret) > 0:
#     ret = cur.fetchmany(8)
#     print(ret)

con.cursor().execute(
    "CREATE OR REPLACE TABLE "+tablename+ " (std_id integer, std_firstname string, std_lastname string)")

print("\n"+tablename + " Successfully created....")

con.cursor().execute(
    "INSERT INTO " +tablename+" (std_id , std_firstname , std_lastname ) VALUES (012, 'John', 'Doe'), (022, 'Alex','Wilkins')")

print(tablename + " Successfully loaded....\n")

print("Printing the schema of "+tablename)
cur1 = con.cursor()
cur1.execute("SELECT * FROM "+tablename)
print(','.join([col[0] for col in cur1.description]))

print("Closing Connection")
con.close()