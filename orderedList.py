## OrderedList ADT for Item (refer to Item in item.py)

class OrderedList():
    
    ## constructor
    def __init__(self):
        self.orderedList = []
        self.freeID = []
        self.countID = 0
    
    ## add(itemName, itemQuantity, itemPrice, itemDescription) this function adds items and assigns an ID to the item and returns the ID
    ## String Int Float String -> Int
    def add(self, itemName, itemQuantity, itemPrice, itemDescription):
        tempID = self.countID
        if self.freeID.len() != 0:
            self.freeID.sort()
            tempID = freeID.pop(0)
        else:
            tempID = self.countID
            self.countID += 1
        self.orderedList.append([tempID, itemName, itemQuantity, itemPrice, itemDescription])
        return tempID
        
    ## searchByID(itemID) this function searches item by ID and returns it
    ## Int -> Item
    def searchByID(self, itemID):
        for i in self.orderedList:
            if i[0] == itemID:
                return i

    ## searchByName(itemName) this function searches item by name and returns a list of matching items
    ## String -> []
    def searchByName(self, itemName):
        itemList = []
        for i in self.orderedList:
            if i[1] == itemName:
                itemList.append(i)
        return itemList


    ## removeByID(itemID) this function removes item by ID
    ## Int -> None
    def removeByID(self, itemID):
        tempItem = self.searchByID(itemID)
        self.freeID.append(tempItem[0])
        self.orderedList.remove(self.searchByID(itemID))
            
    ## removeByName(itemName) this function removes all items of specified name
    ## Int -> None
    def removeByName(self, itemName):
        for i in self.orderedList:
            if i[1] == itemName:
                self.orderedList.remove(i)
    
    ## isEmpty() this function checks if orderedList is empty
    ## None -> Bool
    def isEmpty(self):
        return self.orderedList.len() == 0