#!/usr/bin/env python3
dbm = __import__('db_mgmt')

correct = 0
wrong = 0
print("into the test protocol")
print("test 1:")
newdom = dbm.check_domain("hello")
if newdom is None:
    correct += 1
    print("newdom is correctly none")
else:
    wrong += 1
    print("newdom is incorrectly not none:")
    print(newdom)

print("test 2:")
dbm.new_domain("tabley")
newdom = dbm.check_domain("tabley")
if newdom is None:
    wrong += 1
    print("newdom is incorrectly none")
else:
    correct += 1
    print("newdom is correctly not none:")
    print(newdom)

print("test 3:article check")
newart = dbm.check_article("url")
if newart is None:
    correct += 1
    print("newart is correctly none")
else:
    wrong += 1
    print("newart is incorrectly none")
    print(newart)

print("test 4: article creation")
dbm.new_article({"url":"testsite.com/articles"})
newart_cr = dbm.check_article("testsite.com/articles")
if newart_cr is None:
    wrong += 1
    print("newart incorrectly didn't create") 
else:
    correct += 1
    print("newart correctly created")
    print(newart_cr)
print("ending test protocol")
print("{} passed tests and {} wrong".format(correct, wrong))
