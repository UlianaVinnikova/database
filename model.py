import controller
import time

tables = {
    1: 'customer',
    2: 'seller',
    3: 'things',
    4: 'order',
    5: 'order_item',
}

class Model:

    @staticmethod
    def show_table(table):
        connection = controller.connection()
        cursor = connection.cursor()
        table_name = '''"''' + tables[table] + '''"'''
        print('\nTable ', tables[table])
        show = f'SELECT * FROM public.{table_name}'
        print("SQL query: ", show)
        cursor.execute(show)
        records = cursor.fetchall()
        cursor.close()
        controller.disconnect(connection)
        return records

    @staticmethod
    def insert_table1(customer_ID, customer_name, customer_gender):
        connection = controller.connection()
        cursor = connection.cursor()
        go_on= True
        while go_on:
            notice = "'This customerID already exists'"
            insert = """DO $$ BEGIN IF NOT EXISTS (SELECT "customerID" FROM "customer" WHERE "customerID" = {})
                     THEN INSERT INTO "customer"("customerID", "name", "gender") VALUES ({},{},{}); RAISE NOTICE {}; ELSE RAISE NOTICE {}; END IF; END $$;
                     """.format(customer_ID, customer_ID, customer_name, customer_gender, "'added'", notice)
            go_on = False
        #print("SQL query: ", insert)
        cursor.execute(insert)
        connection.commit()
        print(connection.notices)
        cursor.close()
        controller.disconnect(connection)

    @staticmethod
    def insert_table2(seller_ID, seller_name, seller_surname):
        connection = controller.connection()
        cursor = connection.cursor()
        go_on = True
        while go_on:
            notice = "'This sellerID already exists'"
            insert = """DO $$ BEGIN IF NOT EXISTS (SELECT "sellerID" FROM "seller" WHERE "sellerID" = {})
                     THEN INSERT INTO "seller"("sellerID", "name", "surname") VALUES ({},{},{}); RAISE NOTICE {}; ELSE RAISE NOTICE {}; END IF; END $$;
                     """.format(seller_ID, seller_ID, seller_name, seller_surname, "'added'", notice)
            go_on = False
        #print("SQL query: ", insert)
        cursor.execute(insert)
        connection.commit()
        print(connection.notices)
        cursor.close()
        controller.disconnect(connection)

    @staticmethod
    def insert_table3(things_barcode, things_name, things_price, things_order_itemID):
        connection = controller.connection()
        cursor = connection.cursor()
        go_on = True
        while go_on:
            notice = "'This barcode already exists'"
            insert = """DO $$ BEGIN IF NOT EXISTS (SELECT "order_itemID" FROM "order_item" WHERE "order_itemID" = {})
                     AND NOT EXISTS (SELECT "barcode" FROM "things" WHERE "barcode" = {}) THEN
                     INSERT INTO "things"("barcode", "name", "price", "order_itemID") VALUES ({},{},{},{}); RAISE NOTICE {}; ELSE RAISE NOTICE {}; END IF; END $$;
                     """.format(things_order_itemID, things_barcode, things_barcode, things_name, things_price, things_order_itemID, "'added'", notice)
            go_on = False
        print("SQL query: ", insert)
        cursor.execute(insert)
        connection.commit()
        print(connection.notices)
        cursor.close()
        controller.disconnect(connection)

    @staticmethod
    def insert_table4(order_ordernumber, order_ordertime, order_customerID, order_sellerID):
        connection = controller.connection()
        cursor = connection.cursor()
        go_on = True
        while go_on:
            notice = "'This ordernumber already exists'"
            insert = """DO $$ BEGIN IF NOT EXISTS (SELECT "cusromerID" FROM "customer" WHERE "customerID" = {})
                     AND NOT EXISTS (SELECT "sellerID" FROM "seller" WHERE "sellerID" = {}) AND NOT EXISTS (select "ordernumber" from "order" where "ordernumber" = {}) THEN
                     INSERT INTO "order"("ordernumber", "ordertime", "customerID", "sellerID") VALUES ({},{},{},{}); RAISE NOTICE {}; ELSE RAISE NOTICE {}; END IF;
                     END $$;""".format(order_customerID, order_sellerID, order_ordernumber, order_ordernumber, order_ordertime, order_customerID, order_sellerID, "'added'", notice)
            go_on = False
        print("SQL query: ", insert)
        cursor.execute(insert)
        connection.commit()
        print(connection.notices)
        cursor.close()
        controller.disconnect(connection)

    @staticmethod
    def insert_table5(orderItem_order_itemID, orderItem_count, orderItem_ordernumber):
        connection = controller.connection()
        cursor = connection.cursor()
        go_on = True
        while go_on:
            notice = "'This order_itemID already exists'"
            insert = """DO $$ BEGIN IF NOT EXISTS (SELECT "ordernumber" FROM "order" where "ordernumber" = {})
                     AND NOT EXISTS (SELECT "order_itemID" FROM "order_item" WHERE "order_itemID" = {}) THEN
                     INSERT INTO "order_item"("order_itemID", "count", "ordernumber") VALUES ({},{},{}); ''RAISE NOTICE {}; ELSE RAISE NOTICE {}; END IF;
                     END $$;""".format(orderItem_ordernumber, orderItem_order_itemID, orderItem_order_itemID, orderItem_count, orderItem_ordernumber, "'added'", notice)
            go_on = False
        print("SQL query: ", insert)
        cursor.execute(insert)
        connection.commit()
        print(connection.notices)
        cursor.close()
        controller.disconnect(connection)

    @staticmethod
    def delete_table1(customer_ID):
        connection = controller.connection()
        cursor = connection.cursor()
        go_on = True
        while go_on:
            delete = f'DELETE FROM "customer" WHERE "customerID" = {customer_ID};' \
                     f'DELETE FROM "order" WHERE "customerID" = {customer_ID};'
            go_on = False
        print("SQL query: ", delete)
        cursor.execute(delete)
        connection.commit()
        print(connection.notices)
        cursor.close()
        controller.disconnect(connection)

    @staticmethod
    def delete_table2(seller_ID):
        connection = controller.connection()
        cursor = connection.cursor()
        go_on = True
        while go_on:
            delete = f'DELETE FROM "seller" WHERE "sellerID" = {seller_ID};' \
                     f'DELETE FROM "order" WHERE "sellerID" = {seller_ID};'
            go_on = False
        print("SQL query: ", delete)
        cursor.execute(delete)
        connection.commit()
        print(connection.notices)
        cursor.close()
        controller.disconnect(connection)

    @staticmethod
    def delete_table3(things_barcode):
        connection = controller.connection()
        cursor = connection.cursor()
        go_on = True
        while go_on:
            delete = f'DELETE FROM "things" WHERE "barcode" = {things_barcode};'
            go_on = False
        print("SQL query: ", delete)
        cursor.execute(delete)
        connection.commit()
        print(connection.notices)
        cursor.close()
        controller.disconnect(connection)

    @staticmethod
    def delete_table4(order_ordernumber):
        connection = controller.connection()
        cursor = connection.cursor()
        go_on = True
        while go_on:
            delete = f'DELETE FROM "order_item" WHERE "ordernumber" = {order_ordernumber};' \
                     f'DELETE FROM "order" WHERE "ordernumber" = {order_ordernumber};'
            go_on = False
        print("SQL query: ", delete)
        cursor.execute(delete)
        connection.commit()
        print(connection.notices)
        cursor.close()
        controller.disconnect(connection)

    @staticmethod
    def delete_table5(orderItem_order_itemID):
        connection = controller.connection()
        cursor = connection.cursor()
        go_on = True
        while go_on:
            delete = f'DELETE FROM "things" WHERE "order_itemID" = {orderItem_order_itemID};' \
                     f'DELETE FROM "order_item" WHERE "order_itemID" = {orderItem_order_itemID};'
            go_on = False
        print("SQL query: ", delete)
        cursor.execute(delete)
        connection.commit()
        print(connection.notices)
        cursor.close()
        controller.disconnect(connection)

    @staticmethod
    def update_table1(customer_ID, set):
        connection = controller.connection()
        cursor = connection.cursor()
        restart = True
        while restart:
            notice = "'There is nothing to update'"
            update = """DO $$ BEGIN IF EXISTS (SELECT "customerID" FROM "customer" WHERE "customerID" = {}) THEN
                     UPDATE "customer" SET {} WHERE "customerID" = {}; RAISE NOTICE {}; ELSE RAISE NOTICE {}; END IF;
                     END $$;""".format(customer_ID, set, customer_ID, "'updated'", notice)
            restart = False
            pass
        print("SQL query: ", update)
        cursor.execute(update)
        connection.commit()
        print(connection.notices)
        cursor.close()
        controller.disconnect(connection)
        pass

    @staticmethod
    def update_table2(seller_ID, set):
        connection = controller.connection()
        cursor = connection.cursor()
        restart = True
        while restart:
            notice = "'There is nothing to update'"
            update = """DO $$ BEGIN IF EXISTS (SELECT "sellerID" FROM "seller" WHERE "sellerID" = {}) THEN
                     UPDATE "seller" SET {} WHERE "sellerID" = {}; RAISE NOTICE {}; ELSE RAISE NOTICE {}; END IF; END $$;
                     """.format(seller_ID, set, seller_ID, "'updated'", notice)
            restart = False
            pass
        print("SQL query: ", update)
        cursor.execute(update)
        connection.commit()
        print(connection.notices)
        cursor.close()
        controller.disconnect(connection)
        pass

    @staticmethod
    def update_table3(things_barcode, set):
        connection = controller.connection()
        cursor = connection.cursor()
        restart = True
        while restart:
            notice = "'There is nothing to update'"
            update = """DO $$ BEGIN IF EXISTS (SELECT "barcode" FROM "things" WHERE "barcode" = {})
                     THEN UPDATE "things" SET {} WHERE "barcode" = {}; RAISE NOTICE {}; ELSE RAISE NOTICE {}; END IF; END $$;
                     """.format(things_barcode, set, things_barcode, "'updated'", notice)
            restart = False
            pass
        print("SQL query: ", update)
        cursor.execute(update)
        connection.commit()
        print(connection.notices)
        cursor.close()
        controller.disconnect(connection)
        pass

    @staticmethod
    def update_table4(order_ordernumber, set):
        connection = controller.connection()
        cursor = connection.cursor()
        restart = True
        while restart:
            notice = "'There is nothing to update'"
            update = """DO $$ BEGIN IF EXISTS (SELECT "ordernumber" FROM "order" WHERE "ordernumber" = {}) 
                     THEN UPDATE "order" SET {} WHERE "ordernumber" = {}; RAISE NOTICE {}; ELSE RAISE NOTICE {}; END IF; END $$;
                     """.format(order_ordernumber, set, order_ordernumber, "'updated'", notice)
            restart = False
            pass
        #print("SQL query: ", update)
        cursor.execute(update)
        connection.commit()
        print(connection.notices)
        cursor.close()
        controller.disconnect(connection)
        pass

    @staticmethod
    def update_table5(orderItem_order_itemID, set):
        connection = controller.connection()
        cursor = connection.cursor()
        restart = True
        while restart:
            notice = "'There is nothing to update'"
            update = """DO $$ BEGIN IF EXISTS (SELECT "order_itemID" FROM "order_item" WHERE "order_itemID" = {}) 
                     THEN UPDATE "order_item" SET {} WHERE "order_itemID" = {}; RAISE NOTICE {}; ELSE RAISE NOTICE {}; END IF; END $$;
                     """.format(orderItem_order_itemID, set, orderItem_order_itemID, "'updated'", notice)
            restart = False
            pass
        #print("SQL query: ", update)
        cursor.execute(update)
        connection.commit()
        print(connection.notices)
        cursor.close()
        controller.disconnect(connection)
        pass

    @staticmethod
    def select_num1(count):
        connection = controller.connection()
        cursor = connection.cursor()
        select = f"""SELECT "count", "name", "price" from (SELECT o."count", t."name", t."price"
                FROM "things" t LEFT JOIN "order_item" o ON o."order_itemID" = t."order_itemID"
                WHERE o."count" = '{count}' GROUP BY o."count", t."name", t."price") AS foo"""
        print("SQL query: ", select)
        beg = int(time.time() * 1000)
        cursor.execute(select)
        end = int(time.time() * 1000) - beg
        records = cursor.fetchall()
        print(f'Time of request = {end} ms')
        cursor.close()
        controller.disconnect(connection)
        return records

    @staticmethod
    def select_num2(customerID):
        connection = controller.connection()
        cursor = connection.cursor()
        select = f"""SELECT "customerID", "ordernumber", "ordertime" FROM (SELECT c."customerID", o."ordernumber", o."ordertime"
                FROM "order" o LEFT JOIN "customer" c ON c."customerID" = o."customerID"
                WHERE c."customerID" = '{customerID}' GROUP BY c."customerID", o."ordernumber", o."ordertime") AS foo"""
        print("SQL query: ", select)
        beg = int(time.time() * 1000)
        cursor.execute(select)
        end = int(time.time() * 1000) - beg
        records = cursor.fetchall()
        print(f'Time of request = {end} ms')
        cursor.close()
        controller.disconnect(connection)
        return records

    @staticmethod
    def select_num3(sellerID):
        connection = controller.connection()
        cursor = connection.cursor()
        select = f"""SELECT "sellerID", "ordernumber", "ordertime" FROM (SELECT s."sellerID", o."ordernumber", o."ordertime"
                FROM "order" o LEFT JOIN "seller" s ON s."sellerID" = o."sellerID"
                WHERE s."sellerID" = '{sellerID}' GROUP BY s."sellerID", o."ordernumber", o."ordertime") AS foo"""
        print("SQL query: ", select)
        beg = int(time.time() * 1000)
        cursor.execute(select)
        end = int(time.time() * 1000) - beg
        records = cursor.fetchall()
        print(f'Time of request = {end} ms')
        cursor.close()
        controller.disconnect(connection)
        return records


    @staticmethod
    def random(table, count):
        connection = controller.connection()
        cursor = connection.cursor()
        go_on = True
        while go_on:
            if table == 1:
                for i in range(count):
                    cursor.execute(f"""INSERT INTO "customer" ("customerID", "name", "gender") 
                                     SELECT generate_series as customerID,
                                     chr(trunc(65 + random()*26)::int)||chr(trunc(65 + random()*26)::int)||chr(trunc(65 + random()*26)::int), 
                                     (array['F', 'M'])[floor(random() * 2 + 1)]
                                     FROM generate_series(5, {count}+5)""")
                go_on = False
            elif table == 2:
                for i in range(count):
                    cursor.execute(f"""INSERT INTO "seller" ("sellerID", "name", "surname") 
                                    SELECT generate_series as sellerID,
                                    chr(trunc(65 + random()*26)::int)||chr(trunc(65 + random()*26)::int), 
                                    chr(trunc(65 + random()*26)::int)||chr(trunc(65 + random()*26)::int)||chr(trunc(65 + random()*26)::int)
                                    FROM generate_series(5, {count}+5)""")
                go_on = False
            else:
                print("Please, enter valid number: ")
        print("Insertion of randomized data was successful!")
        connection.commit()
        cursor.close()
        controller.disconnect(connection)