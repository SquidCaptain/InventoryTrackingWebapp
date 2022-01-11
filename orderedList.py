## OrderedList ADT for Item (refer to Item in item.py)
## Items are lists [itemID, itemName, itemAmount, itemCost, itemDescription] [Int, String, Int, Int, String]

class OrderedList():
    
    ## constructor
    def __init__(self):
        self.orderedList = []
        self.freeID = []
        self.countID = 0
    
    ## add(item) this function adds items without their IDs and assigns an ID to the item and returns the ID
    ## [] -> Int
    def add(self, item):
        tempID = self.countID
        if self.freeID.len() != 0:
            self.freeID.sort()
            tempID = freeID.pop(0)
        else:
            self.countID += 1
        self.orderedList.append(item.insert(tempID ,0))
        return tempID
        
    ## searchByID(itemID) this function searches item by ID and returns it
    ## Int -> Item
    def searchByID(self, itemID):
        for i in self.orderedList:
            if i[0] == itemID:
                return i

    ## searchByName(itemName) this function searches item by name and returns a list of matching items that
    ##                          contains a substring of the name
    ## String -> []
    def searchByName(self, itemName):
        itemList = []
        for i in self.orderedList:
            if itemName in i[1]:
                itemList.append(i)
        return itemList


    ## removeByID(itemID) this function removes item by ID
    ## Int -> None
    def removeByID(self, itemID):
        tempItem = self.searchByID(itemID)
        self.freeID.append(tempItem[0])
        self.orderedList.remove(self.searchByID(itemID))
            
    ## removeByName(itemName) this function removes all items of exact specified name
    ## Int -> None
    def removeByName(self, itemName):
        for i in self.orderedList:
            if itemName == i[1]:
                self.orderedList.remove(i)
    
    ## isEmpty() this function checks if orderedList is empty
    ## None -> Bool
    def isEmpty(self):
        return self.orderedList.len() == 0