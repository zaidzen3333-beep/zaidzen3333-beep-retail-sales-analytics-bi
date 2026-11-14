Table,Field,Description
Sales,Order Number,Unique ID for each order
Sales,Line Item,Identifies individual products purchased as part of an order
Sales,Order Date,Date the order was placed
Sales,Delivery Date,Date the order was delivered
Sales,CustomerKey,Unique key identifying which customer placed the order
Sales,StoreKey,Unique key identifying which store processed the order
Sales,ProductKey,Unique key identifying which product was purchased
Sales,Quantity,Number of items purchased
Sales,Currency Code,Currency used to process the order
=====================================================================
=====================================================================
Customers,CustomerKey,Primary key to identify customers
Customers,Gender,Customer gender
Customers,Name,Customer full name
Customers,City,Customer city
Customers,State Code,Customer state (abbreviated)
Customers,State,Customer state (full)
Customers,Zip Code,Customer zip code
Customers,Country,Customer country
Customers,Continent,Customer continent
Customers,Birthday,Customer date of birth
=====================================================================
=====================================================================
Products,ProductKey,Primary key to identify products
Products,Product Name,Product name
Products,Brand,Product brand
Products,Color,Product color
Products,Unit Cost USD,Cost to produce the product in USD
Products,Unit Price USD,Product list price in USD
Products,SubcategoryKey,Key to identify product subcategories
Products,Subcategory,Product subcategory name
Products,CategoryKey,Key to identify product categories
Products,Category,Product category name
=====================================================================
=====================================================================
Stores,StoreKey,Primary key to identify stores
Stores,Country,Store country
Stores,State,Store state
Stores,Square Meters,Store footprint in square meters
Stores,Open Date,Store open date
=====================================================================
=====================================================================
Exchange Rates,Date,Date
Exchange Rates,Currency,Currency code
Exchange Rates,Exchange,Exchange rate compared to USD
========================================================================
========================================================================
========================================================================
DATA REPORT_v01 :
------------------------------------------------------------------------
SALES : rows : 62 884  , columns : 9
CUSTOMERS : rows : 15 266 , columns : 10
PRODUCTS : rows : 2517 , columns : 10
STORS : rows : 67  , columns :5
EXCHANGE_PATH  : rows : 11215  , columns : 3
------------------------------------------------------------------------
SALES : 

               Data Type  Unique Values  Missing Values
Order Number      int64          26326               0
Line Item         int64              7               0
Order Date          str           1641               0
Delivery Date       str           1492           49719
CustomerKey       int64          11887               0
StoreKey          int64             58               0
ProductKey        int64           2492               0
Quantity          int64             10               0
Currency Code       str              5               0
========================================================
CUSTOMERS:
              Data Type  Unique Values  Missing Values
CustomerKey     int64          15266               0
Gender            str              2               0
Name              str          15118               0
City              str           8258               0
State Code        str            467              10
State             str            512               0
Zip Code          str           9505               0
Country           str              8               0
Continent         str              3               0
Birthday          str          11270               0
========================================================
PRODUCTS : 
              Data Type  Unique Values  Missing Values
ProductKey         int64           2517               0
Product Name         str           2517               0
Brand                str             11               0
Color                str             16               0
Unit Cost USD        str            480               0
Unit Price USD       str            426               0
SubcategoryKey     int64             32               0
Subcategory          str             32               0
CategoryKey        int64              8               0
Category             str              8               0
========================================================
STORS : 
            Data Type  Unique Values  Missing Values
StoreKey          int64             67               0
Country             str              9               0
State               str             67               0
Square Meters   float64             36               1
Open Date           str             25               0
========================================================
EXCHANGE_RATES :
            Data Type  Unique Values  Missing Values
Date           str           2243               0
Currency       str              5               0
Exchange   float64           3473               0
========================================================
DATA QUALITY REPORT: SALES

              Data Type  Missing Count  Missing Percentage  Unique Values  \
Order Number      int64              0                0.00          26326   
Line Item         int64              0                0.00              7   
Order Date          str              0                0.00           1641   
Delivery Date       str          49719               79.06           1492   
CustomerKey       int64              0                0.00          11887   
StoreKey          int64              0                0.00             58   
ProductKey        int64              0                0.00           2492   
Quantity          int64              0                0.00             10   
Currency Code       str              0                0.00              5   

               Duplicate Count  
Order Number             36558  
Line Item                62877  
Order Date               61243  
Delivery Date            61391  
CustomerKey              50997  
StoreKey                 62826  
ProductKey               60392  
Quantity                 62874  
Currency Code            62879  
----------------------------------------------------------
CUSTOMERS :


                Data Type  Missing Count  Missing Percentage  Unique Values  \
CustomerKey     int64              0                0.00          15266   
Gender            str              0                0.00              2   
Name              str              0                0.00          15118   
City              str              0                0.00           8258   
State Code        str             10                0.07            467   
State             str              0                0.00            512   
Zip Code          str              0                0.00           9505   
Country           str              0                0.00              8   
Continent         str              0                0.00              3   
Birthday          str              0                0.00          11270   

             Duplicate Count  
CustomerKey                0  
Gender                 15264  
Name                     148  
City                    7008  
State Code             14798  
State                  14754  
Zip Code                5761  
Country                15258  
Continent              15263  
Birthday                3996 

PRODUCTS : 
               Data Type  Missing Count  Missing Percentage  Unique Values  \
ProductKey         int64              0                 0.0           2517   
Product Name         str              0                 0.0           2517   
Brand                str              0                 0.0             11   
Color                str              0                 0.0             16   
Unit Cost USD        str              0                 0.0            480   
Unit Price USD       str              0                 0.0            426   
SubcategoryKey     int64              0                 0.0             32   
Subcategory          str              0                 0.0             32   
CategoryKey        int64              0                 0.0              8   
Category             str              0                 0.0              8   

                Duplicate Count  
ProductKey                    0  
Product Name                  0  
Brand                      2506  
Color                      2501  
Unit Cost USD              2037  
Unit Price USD             2091  
SubcategoryKey             2485  
Subcategory                2485  
CategoryKey                2509  
Category                   2509  
-----------------------------------------------------------------
STORS :               Data Type  Missing Count  Missing Percentage  Unique Values  \
StoreKey          int64              0                0.00             67   
Country             str              0                0.00              9   
State               str              0                0.00             67   
Square Meters   float64              1                1.49             36   
Open Date           str              0                0.00             25   

               Duplicate Count  
StoreKey                     0  
Country                     58  
State                        0  
Square Meters               30  
Open Date                   42  
-------------------------------------------------------------
EXCHANGE_PATH :
         Data Type  Missing Count  Missing Percentage  Unique Values  \
Date           str              0                 0.0           2243   
Currency       str              0                 0.0              5   
Exchange   float64              0                 0.0           3473   

          Duplicate Count  
Date                 8972  
Currency            11210  
Exchange             7742  
===============================
sales: 0 completely duplicated rows
customers: 0 completely duplicated rows
products: 0 completely duplicated rows
stores: 0 completely duplicated rows
exchange_rates: 0 completely duplicated rows
=======================================
Customers primary key candidate:
True
Products primary key candidate:
True