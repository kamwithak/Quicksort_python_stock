import urllib

# select parameters
symbolslist = ["goog","amzn","aapl","yhoo","dell","msft"]
stock_data_list = {}

symbol = "msft"
start = ["09","15","2008"]
end = ["09","26","2013"]

class StockData:
    def __init__(self,record):
        record_arr =  record.split(",")
      
        self.date = record_arr[0]
        self.open = record_arr[1]
        self.high = record_arr[2]
        self.low = record_arr[3]
        self.close = record_arr[4]
        self.volume = int(record_arr[5])
        self.adj_close = record_arr[6]

def printRecord(r,s):
    myfile = open(s+"_data.txt","a")
    myfile.write(str(r.date)+" "+str(r.open)+" "+str(r.high)+" "+str(r.low)+" "+str(r.close)+" "+str(r.adj_close)+" "+str(r.volume)+"\n")
    myfile.close()


def getArray(symbol):
    #parameterize the url
    text = urllib.urlopen("http://ichart.finance.yahoo.com/table.csv?s="+symbol+"&a="+start[0]+"&b="+start[1]+"&c="+start[2]+"&d="+end[0]+"&e="+end[1]+"&f="+end[2]+"&g=d&ignore=.csv").read()

    records = text.split("\n")  #splits on new line character, creates an array

    records.pop(0) # don't want the header info
    records.pop(-1)# last line is blank..

    stock_array = []
    for record in records: #import data in to arrays of class objects
        stock_array.append(StockData(record))  
    return stock_array

def quickSort(stockdata):  #swap class objects not elements
    lower = []
    pivots = []
    upper = []
    if len(stockdata) <= 1:
        return stockdata
    else:
        pivot = stockdata[0]
        for i in stockdata: #i is an object
            if i.close < pivot.close:
                lower.append(i)
            elif i.close > pivot.close:
                upper.append(i) 
            else:
                pivots.append(i)
        lower = quickSort(lower)
        upper = quickSort(upper)
        return lower + pivots + upper


def quickSortVolume(stockdata):
    lower = []
    pivots = []
    upper = []
    if len(stockdata) <= 1:
        return stockdata
    else:
        pivot = stockdata[0]
        for i in stockdata:
            if i.volume < pivot.volume:
                lower.append(i)
            elif i.volume > pivot.volume:
                upper.append(i)
            else:
                pivots.append(i)
        lower = quickSortVolume(lower)
        upper = quickSortVolume(upper)
        return lower + pivots + upper


#created a list of data objects
for s in symbolslist:
    stock_data_list[s] = getArray(s)
    close_sorted = quickSort(stock_data_list[s]) #change symbol to change output
    myfile = open(s+"_data.txt","a")

    myfile = open(s+"_data.txt","a")
    myfile.write("100 Lowest Close "+s+"\n")
    myfile.close()
    
    for t in close_sorted[0:100]:
        printRecord(t,s)
        
    myfile = open(s+"_data.txt","a")
    myfile.write("100 highest close "+s+"\n")
    myfile.close()
    
    for t in close_sorted[-100:]:
        printRecord(t,s)

    volume_sorted = quickSortVolume(stock_data_list[s])

    myfile = open(s+"_data.txt","a")
    myfile.write("100 Lowest Volume "+s+"\n")
    myfile.close()
    
    for t in volume_sorted[0:100]:
        printRecord(t,s)
    myfile = open(s+"_data.txt","a")
    myfile.write("100 highest Volume "+s+"\n")
    myfile.close()
    
    for t in volume_sorted[-100:]:
        printRecord(t,s)
    
#the stock achieves the 17th highest price at the 17th element..

def binSearch(price,stockdata):
    upper = len(stockdata)-1
    lower = 0
    mid = (upper-lower)/2
    found = False
    while upper!= lower and  found ==False:
        if upper == lower:
            found = True
        if price < stockdata[mid].close: #change to volume for finding 5th highest volume day
            upper = mid
            mid = (upper-lower)/2
        if price>stockdata[mid].close:
            lower = mid
            mid = (upper-lower)/2
    print "the date the 17th hghest price occurs",stockdata[upper].date  #change to close for problem 3.2         
      
#binSearch(close_sorted[17].close,stock_data_list[symbol]) # pass 5th highest volume day

def percentile(num):
    for i in close_sorted[-(len(close_sorted)/100)*(100-num):]:
        printRecord(i)
#percentile(75)     to get 75th percentile and above

