import psycopg2
import controller
from model import Model

tables = {
    1: 'customer',
    2: 'seller',
    3: 'things',
    4: 'order',
    5: 'order_item',
}

class View:

    def __init__(self, table, records):
        self.table = table
        self.records = records

    @staticmethod
    def list():
        print('1: customer\n2: seller\n3: things\n4: order\n5: order_item\n')

    @staticmethod
    def attribute_list_for_update(table):
        if table == 1:
            print('1: name\n2: gender')

        elif table == 2:
            print('1: name\n2: surname')

        elif table == 3:
            print('1: name\n2: price')

        elif table == 4:
            print('1: ordertime')

        elif table == 5:
            print('1: count')

    def show(self):
        if self.table == 1:
            for row in self.records:
                print("-------------------")
                print("customerID = ", row[0])
                print("name = ", row[1])
                print("gender = ", row[2])
                print("-------------------")
        elif self.table == 2:
            for row in self.records:
                print("-------------------")
                print("sellerID = ", row[0])
                print("name = ", row[1])
                print("surname = ", row[2])
                print("-------------------")
        elif self.table == 3:
            for row in self.records:
                print("-------------------")
                print("barcode = ", row[0])
                print("name = ", row[1])
                print("price = ", row[2])
                print("order_itemID = ", row[3])
                print("-------------------")
        elif self.table == 4:
            for row in self.records:
                print("-------------------")
                print("ordernumber = ", row[0])
                print("ordertime = ", row[1])
                print("customerID = ", row[2])
                print("sellerID = ", row[3])
                print("-------------------")
        elif self.table == 5:
            for row in self.records:
                print("-------------------")
                print("order_otemID = ", row[0])
                print("count = ", row[1])
                print("ordernumder = ", row[2])
                print("-------------------")
        else:
            print("\nERROR!\nIncorrect input,try again!")

    def show_select(self):
        if self.table == 1:
            for row in self.records:
                print("-------------------")
                print("count = ", row[0])
                print("name = ", row[1])
                print("price = ", row[2])
                print("-------------------")
        elif self.table == 2:
            for row in self.records:
                print("-------------------")
                print("customerID = ", row[0])
                print("ordernumber = ", row[1])
                print("ordertime = ", row[2])
                print("-------------------")
        elif self.table == 3:
            for row in self.records:
                print("-------------------")
                print("sellerID = ", row[0])
                print("ordernumber = ", row[1])
                print("ordertime = ", row[2])
                print("-------------------")


class Menu:

    @staticmethod
    def mainmenu():
        exit = False
        while not exit:
            print("\nMENU\n1. Show one table\n2. Show all table\n3. Insert data\n4. Delete data\n5. Update data\n6. Exit\n")
            choice = input('Choose an option: ')
            if choice == '1':
                View.list()
                table = input('Choose the table number: ')
                table = controller.validate_table(table)
                if table == '1':
                    Model.show_customer()
                elif table == '2':
                    Model.show_seller()
                elif table == '3':
                    Model.show_things()
                elif table == '4':
                    Model.show_order()
                elif table == '5':
                    Model.show_order_item()

            elif choice == '2':
                Model.show_customer()
                Model.show_seller()
                Model.show_things()
                Model.show_order()
                Model.show_order_item()

            elif choice == '3':
                end_insert = False
                while not end_insert:
                    try:
                        View.list()
                        table = input('Choose the table number: ')
                        table = controller.validate_table(table)
                        if table == 1:
                            customer_ID = "'" + input("Customer ID = ") + "'"
                            customer_name = "'" + input("Customer name = ") + "'"
                            customer_gender = "'" + input("Customer gender = ") + "'"
                            Model.insert_table1(customer_ID, customer_name, customer_gender)
                        elif table == 2:
                            seller_ID = "'" + input("Seller ID = ") + "'"
                            seller_name = "'" + input("Seller name = ") + "'"
                            seller_surname = "'" + input("Seller surname = ") + "'"
                            Model.insert_table2(seller_ID, seller_name, seller_surname)
                        elif table == 3:
                            things_barcode = "'" + input("Things barcode = ") + "'"
                            things_name = "'" + input("Things name = ") + "'"
                            things_price = "'" + input("Things price = ") + "'"
                            things_order_itemID = "'" + input("Things order_itemID = ") + "'"
                            Model.insert_table3(things_barcode, things_name, things_price,things_order_itemID)
                        elif table == 4:
                            order_ordernumber = "'" + input("Order ordernumber = ") + "'"
                            order_ordertime = "'" + input("Order ordertime = ") + "'"
                            order_customerID = "'" + input("Order customerID = ") + "'"
                            order_sellerID = "'" + input("Order sellerID = ") + "'"
                            Model.insert_table4(order_ordernumber, order_ordertime, order_customerID, order_sellerID)
                        elif table == 5:
                            orderItem_order_itemID = "'" + input("Order_item order_itemID = ") + "'"
                            orderItem_count = "'" + input("Order_item count = ") + "'"
                            orderItem_ordernumber = "'" + input("Order_item ordernumber = ") + "'"
                            Model.insert_table5(orderItem_order_itemID, orderItem_count, orderItem_ordernumber)
                        else:
                            print('ERROR!\nIncorrect input, try again!')
                    except(Exception, psycopg2.Error) as error:
                        print('PostgreSQL ERROR! ',error)
                    incorrect = True
                    while incorrect:
                        answer = input("Do you want to continue working with the 'insert'?\nEnter 1 if yes or 2 if no: ")
                        if answer == '2':
                            end_insert = True
                            incorrect = False
                        elif answer == '1':
                            incorrect = False
                            pass
                        else:
                            print('ERROR!\nPlease, enter your answer!')

            elif choice == '4':
                end_delete = False
                while not end_delete:
                    try:
                        View.list()
                        table = input('Choose the table number: ')
                        table = controller.validate_table(table)
                        if table == 1:
                            customer_ID = "'" + input('Attribute to delete customerID = ') + "'"
                            Model.delete_table1(customer_ID)
                        elif table == 2:
                            seller_ID = "'" + input('Attribute to delete sellerID = ') + "'"
                            Model.delete_table2(seller_ID)
                        elif table == 3:
                            things_barcode = "'" + input('Attribute to delete barcode = ') + "'"
                            Model.delete_table3(things_barcode)
                        elif table == 4:
                            order_ordernumber = "'" + input('Attribute to delete ordernumber = ') + "'"
                            Model.delete_table4(order_ordernumber)
                        elif table == 5:
                            orderItem_order_itemID = "'" + input('Attribute to delete order_itemID = ') + "'"
                            Model.delete_table5(orderItem_order_itemID)
                        else:
                            print('ERROR!\nIncorrect input, try again!')
                    except(Exception, psycopg2.Error) as error:
                        print('PostgreSQL ERROR! ',error)
                    incorrect = True
                    while incorrect:
                        answer = input("Do you want to continue working with the 'delete'?\nEnter 1 if yes or 2 if no: ")
                        if answer == '2':
                            end_delete = True
                            incorrect = False
                        elif answer == '1':
                            incorrect = False
                            pass
                        else:
                            print('ERROR!\nPlease, enter your answer!')

            elif choice == '5':
                end_update = False
                while not end_update:
                    try:
                        View.list()
                        table = input('Choose the table number: ')
                        table = controller.validate_table(table)
                        if table == 1:
                            customer_ID = "'" + input('Attribute to update (where) customerID = ') + "'"
                            View.attribute_list_for_update(1)
                            in_restart = True
                            while in_restart:
                                answer = input('Choose the number of attribute: ')
                                if answer == '1':
                                    value = "'" + input('New value of attribute = ') + "'"
                                    set = '"name" = {}'.format(value)
                                    in_restart = False
                                elif answer == '2':
                                    value = "'" + input('New value of attribute = ') + "'"
                                    set = '"gender" = {}'.format(value)
                                    in_restart = False
                                else:
                                    print('Incorrect input, try again.')
                                Model.update_table1(customer_ID, set)
                        elif table == 2:
                            seller_ID = "'" + input('Attribute to update (where) sellerID = ') + "'"
                            View.attribute_list_for_update(2)
                            in_restart = True
                            while in_restart:
                                answer = input('Choose the number of attribute: ')
                                if answer == '1':
                                    value = "'" + input('New value of attribute = ') + "'"
                                    set = '"name" = {}'.format(value)
                                    in_restart = False
                                elif answer == '2':
                                    value = "'" + input('New value of attribute = ') + "'"
                                    set = '"surname" = {}'.format(value)
                                    in_restart = False
                                else:
                                    print('Incorrect input, try again.')
                                Model.update_table2(seller_ID, set)
                        elif table == 3:
                            things_barcode = "'" + input('Attribute to update (where) barcode = ') + "'"
                            View.attribute_list_for_update(3)
                            in_restart = True
                            while in_restart:
                                answer = input('Choose the number of attribute: ')
                                if answer == '1':
                                    value = "'" + input('New value of attribute = ') + "'"
                                    set = '"name" = {}'.format(value)
                                    in_restart = False
                                elif answer == '2':
                                    value = "'" + input('New value of attribute = ') + "'"
                                    set = '"price" = {}'.format(value)
                                    in_restart = False
                                else:
                                    print('Incorrect input, try again.')
                                Model.update_table3(things_barcode, set)
                        elif table == 4:
                            order_ordernumber = "'" + input('Attribute to update (where) ordernumber = ') + "'"
                            View.attribute_list_for_update(4)
                            in_restart = True
                            while in_restart:
                                answer = input('Choose the number of attribute: ')
                                if answer == '1':
                                    value = "'" + input('New value of attribute = ') + "'"
                                    set = '"ordertime" = {}'.format(value)
                                    in_restart = False
                                else:
                                    print('Incorrect input, try again.')
                                Model.update_table4(order_ordernumber, set)
                        elif table == 5:
                            orderItem_order_itemID = "'" + input('Attribute to update (where) order_itemID = ') + "'"
                            View.attribute_list_for_update(5)
                            in_restart = True
                            while in_restart:
                                answer = input('Choose the number of attribute: ')
                                if answer == '1':
                                    value = "'" + input('New value of attribute = ') + "'"
                                    set = '"count" = {}'.format(value)
                                    in_restart = False
                                else:
                                    print('ERROR!\nIncorrect input, try again!')
                                Model.update_table5(orderItem_order_itemID, set)
                            else:
                                print('ERROR!\nIncorrect input, try again!')
                    except(Exception, psycopg2.Error) as error:
                        print('PostgreSQL ERROR!',error)
                    incorrect = True
                    while incorrect:
                        answer = input("Do you want to continue working with the 'update'?\nEnter 1 if yes or 2 if no: ")
                        if answer == '2':
                            end_update = True
                            incorrect = False
                        elif answer == '1':
                            incorrect = False
                            pass
                        else:
                            print('ERROR!\nPlease, enter your answer!')

            elif choice == '6':
                print("The program is over!")
                break
            else:
                print("Please, choose a number from 1 to 8: ")