# [The Farmer’s Market](https://github.com/prakashsharmacs24/python-fmart)

A Farmer’s checkout application provides options to manage orders/cart details for given products and offers.



## Maintained by [Prakash Kumar](https://github.com/prakashsharmacs24)

## Built With
* [Python](https://www.python.org/) - Programing language
* [Docker](https://www.docker.com/) - Application platform

Installation
------------

* Clone the project repository

  ```bash
  git clone --depth=1 https://github.com/prakashsharmacs24/python-fmart
  cd python-fmart
  ```

* Start Application

  * Build application images using Makefile
  ```bash
  make build
  ```


  * Run application image using Makefile


  ```bash
  make run
  ```

* Run the unit test cases and produce coverage.

  * Build image for unit testing
  ```bash
  make build-test
  ```

  * Run Test cases

  ```bash
  make test
  ```

  * Results
    Name | Stmts |  Miss | Cover | Missing
    ------------ | -------------| ------------- | -------------| -------------
    cart/__init__.py | 2  | 0 | 100% | 
    cart/cart.py | 90  | 0 | 100% | 
    cart/items.py | 1  | 0 | 100% | 
    ------------ | -------------| ------------- | -------------| -------------
    TOTAL| 93  | 0 | 100% | 


Details
------------

**Available Products**

Product Code |     Name     |  Price  
------------ | ------------ | ------------
CH1      |   Chai       |  $3.11  
AP1      |   Apples     |  $6.00
CF1      |   Coffee     | $11.23  
MK1      |   Milk       |  $4.75  
OM1      |   Oatmeal    |  $3.69  



**Available Cart Rules**

1. BOGO -- Buy-One-Get-One-Free Special on Coffee. (Unlimited)
2. APPL -- If you buy 3 or more bags of Apples, the price drops to $4.50.
3. CHMK -- Purchase a box of Chai and get milk free. (Limit 1)
4. APOM -- Purchase a bag of Oatmeal and get 50% off a bag of Apples

Actions
------------

**Available commands**

* add: Add an item by product code in cart
* del: Remove an item by product code from the cart
* stop: Exit from add or del prompt
* print: Show Cart items
* clear: Reinitialize the cart
* exit: Exit from the application

# License

MIT License

Copyright (c) 2020 prakashkumar(<mailto:prakashsharmacs24@gmail.com>)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
