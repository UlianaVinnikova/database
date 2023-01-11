import psycopg2

def connection():

    return psycopg2.connect(
        user="postgres",
        password="123",
        host="localhost",
        port="5432",
        database="postgres",
    )

def disconnect(connection):
    connection.commit()
    connection.close()

def validate_table(table):
    incorrect = True
    while incorrect:
        if table.isdigit():
            table = int(table)
            if 1 <= table <= 5:
                incorrect = False
            else:
                print("\nERROR!\nIncorrect input,try again!")
        else:
            print("\nERROR!\nIncorrect input,try again!")
    return table