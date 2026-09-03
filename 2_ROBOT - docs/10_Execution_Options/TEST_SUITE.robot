*** settings ***
Documentation   To know how many options to run ro bobot file

*** Variables ***
${ONE}     99

*** Test Cases **
Testcase:1
    Sleep     0s
    Log    TestCase 1 ==> ${ONE}   ERROR

Testcase:2
    Sleep     0s
    Log    TestCase 2    ERROR


Testcase:3
    Sleep     0s
    Log    TCase 3    ERROR


