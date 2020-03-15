'''
Title: Assignmen08.py
Desc: Assignnment 08 - Working with classes
DBiesinger, 2020-Jan-01, created file
DBiesinger, 2020-Jan-01, added pseudocode to complete assignment 08
Jeffrey Shen, 2020-Mar-11, created initial code for main body
Jeffrey Shen, 2020-Mar-12, created initial code for classes
Jeffrey Shen, 2020-Mar-14, edited properties, methods, fields inside classes
Jeffrey Shen, 2020-Mar-15, added docstrings and debugged
'''

''' -- DATA -- '''
strChoice = '' # User input
strFileName = 'CDInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD

    methods:
        user_add: user adds an index to the CD inventory
        user_del: user selects and deletes an index from the CD inventory

    """

    """--Attributes--"""
    def __init__(self, cd_id, cd_title, cd_artist):
        self.__cd_id = cd_id
        self.__cd_title = cd_title
        self.__cd_artist = cd_artist

    """--Properties--"""
    @property
    def cd_id(self):
        return self.__cd_id
    @property
    def cd_title(self):
        return self.__cd_title
    @property
    def cd_artist(self):
        return self.__cd_artist
        
    @cd_id.setter
    def cd_id(self, value):
        self.__cd_id = value
    
    @cd_title.setter
    def cd_title(self, value):
        self.__cd_title = value
    
    @cd_artist.setter
    def cd_artist(self, value):
       self.__cd_artist = value

    """--Methods--"""
    @staticmethod
    def user_add(cd_id, title, artist, table):
        """Adds CD title and artist from user input

        Args:
            cd_id (string): string representing the ID of the album
            cd_title (string): string representing the Title of the album
            cd_artist (string): string representing the Artist
            table (list of dicts): 2d structure, list of dictionaries containing cd information

        Returns:
            table (list of dicts): 2d structure, list of dictionaries containing cd information
        """
        dicRow = {'ID': cd_id, 'Title': title, 'Artist': artist}
        table.append(dicRow)
        return table

    @staticmethod
    def user_del(id_to_delete, table):
        """Deletes ID from user input

        Args:
            id_to_delete (string): id representing the cd to remove from inventory
            table (list of dicts): 2d structure, list of dictionaries containing cd information

        Returns:
            table (list of dicts): 2d structure, list of dictionaries containing cd information
        """
        intRowNr = -1
        blnCDRemoved = False
        for row in table:
            intRowNr += 1
            if row['ID'] == id_to_delete:
                del table[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')
        return table

''' -- PROCESSING -- '''
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """

    """--Methods--"""
    @staticmethod
    def read_file(filename, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name using pickle module (binary)

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime
        """
        try:
            objFile = open(filename, 'r')
            table.clear()  # this clears existing data and allows to load data from file
            for line in objFile:
                data = line.strip().split(',')
                dicRow = {'ID': data[0], 'Title': data[1], 'Artist': data[2]}
                table.append(dicRow)
            objFile.close()
        except FileNotFoundError:
            print("The file {} could not be loaded".format(filename))
        return table
    
    @staticmethod
    def save_file(filename, table):
        """Writes file data using pickle module

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        try:
            with open(filename, 'a+') as f:
                for row in table:
                    txt_line = ", ".join([str(value) for value in row.values()]) + '\n'
                    f.write(txt_line)
        except Exception:
            print('General Error')

''' -- PRESENTATION (Input/Output) -- '''
class IO:
    """Processes input/output actions:

    properties:

    methods:
        print_menu: menu selection for CD inventory manipulation
        menu_choice: process user selection from menu
        show_inventory: display current CD inventory table
        get_user_input: user input for adding an index to CD inventory
        del_input: user input to delete index in CD inventory

    """
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """
        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')
    
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x
        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table

        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.
        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')

    @staticmethod
    def get_user_input():
        """ Gets ID, Artist, and Album information from the user

        Args:
            None.

        Return:
            cd_id (int): integer representing the ID of the album
            title (string): string representing the Title of the album
            artist (string): string representing the Artist
        """
        # continue to loop if user input is returning an error
        while True:
            try:
                cd_id = int(input('Enter ID: '))
                title = input('What is the CD\'s title? ').strip()
                artist = input('What is the Artist\'s name? ').strip()
                return cd_id, title, artist
            except ValueError as e:
                print('Not an integer')
                print('Build in error info:')
                print(type(e), e, e.__doc__, sep='\n')
                print() # extra space for layout
                IO.show_inventory(lstOfCDObjects)

    @staticmethod
    def del_input():
        """ Gets ID that user wants to delete.

        Args:
            None.

        Return:
            strIDDel.
        """
        # continue to loop if user input is returning an error
        while True:
            try:
                strIDDel = int(input('Which ID would you like to delete? ').strip())
                return strIDDel
            except ValueError as e:
                print('Not an integer')
                print('Build in error info:')
                print(type(e), e, e.__doc__, sep='\n')
                print() # extra space for layout
                IO.show_inventory(lstOfCDObjects)

''' -- Main Body of Script -- '''
# Load data from file into a list of CD objects on script start
lstOfCDObjects = FileIO.read_file(strFileName, lstOfCDObjects)

while True:
    IO.print_menu()
    strChoice = IO.menu_choice()
    if strChoice == 'x':
        break

    # process load inventory
    elif strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileIO.read_file(strFileName, lstOfCDObjects)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.

    # process add a CD
    elif strChoice == 'a':
        # Ask user for new ID, CD Title and Artist
        cd_id, title, artist = IO.get_user_input()
        lstOfCDObjects = CD.user_add(cd_id, title, artist, lstOfCDObjects)
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.

    # process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.

    # process delete a CD
    elif strChoice == 'd':
        # get user input for which CD to delete
        IO.show_inventory(lstOfCDObjects)
        strIDDel = IO.del_input()
        # search thru table and delete CD
        lstOfCDObjects = CD.user_del(strIDDel, lstOfCDObjects)
        # show updated table
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.

    # process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            FileIO.save_file(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    else:
        print('General Error')