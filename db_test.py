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

print("test 2:create then check domain")
dbm.new_domain("tabley")
newdom = dbm.check_domain("tabley")
if newdom is None:
    wrong += 1
    print("newdom is incorrectly none")
else:
    correct += 1
    print("newdom is correctly not none:")
    print(newdom)
dbm.delete_domain("tabley")

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
dbm.new_article({"url": "testsite.com/article", 'domain': 'test_domain'})
newart_cr = dbm.check_article("testsite.com/article")
if newart_cr is None:
    wrong += 1
    print("newart incorrectly didn't create")
else:
    correct += 1
    print("newart correctly created")
    print(newart_cr)
dbm.delete_article("testsite.com/article")

print("test of creation of article review ")
dbm.new_review({'domain': 'test_domain', 'url':'testsite.com/articles', 'score': 4})
dbm.new_review({'domain': 'test_domain', 'url':'testsite.com/articles', 'score': 3})
print("attempted to create review")
dbm.update_domain("test_domain")

print("ending test protocol")
print("{} passed tests and {} wrong".format(correct, wrong))
