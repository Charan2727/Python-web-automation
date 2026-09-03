*** Settings ***
Documentation    Loop operations using range function


*** Test Cases ***
Test For Loop
    FOR    ${INDEX}    IN RANGE    1    11    2
        log    ${INDEX}    WARN
    END

