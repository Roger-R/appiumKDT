# appiumKDT
 
#### Summary
- This is a project provides KDT ability for appium testing
- Low coding goal, testers modify Excel Case File in "/caseFile" only
- etc.

#### Setup Guide(Android)
1. PC install Appium Desktop
2. PC install Android SDK
3. Device install target APP (My Observatory)
4. Device enable Developer Mode
5. Device connect to PC
6. PC start Appium Desktop Server 
7. Use Pytest to run demo case: test_appiumDemo.py

#### Package Structure
- caseFile
- core

#### Design Description
- TODO: scan all files in path "/caseFile"
- etc.

#### Excel Case Template
| id | CaseDesc | Keyword | eleType | elePath | param1 | param2 | param3 | param4 |
|----| ---      | ---     | ---     | ---     | ---    | ---    | ---    | ---    |
|only >0 will run|nullable|start| |appium server url| | | | |
|only >0 will run|nullable|implicitily| | |int| | | |
|only >0 will run|nullable|click|By enums, uiautomator|element locator|null if locates single element, int if locates multiple elements| | | |
|only >0 will run|nullable|swipe| | |start x cornate|start y cornate|end x cornate|end y cornate|
|only >0 will run|nullable|sleep| | |int| | | |
    