# Selenium Hybrid Framework
# (Python, Selenium, Pytest, Page Object Model, HTML Reports)
#-----------------------------------------------------------
"""
What is a framework?
    Framework is an organized way of maintaining automation files.
    In the framework, all the files will communicate each other to perform a certain task.

Objective/Goals:
    1) Re-usability
    2) Maintainability

Types:
    1) Built-in frameworks
        pytest, robot framework, unittest etc...

    2) Customized/user defined framework
        Datadriven framework, Keyword-driven framework, Hybrid-driven framework

Phases:
    1) Analyze application, technology and skill set of a team, choose test cases

        100 TC's
        ---------
        Re-test cases(test data)
        Regression test cases
        TC's can be automatable

        100 % automation?
            Whatever test cases are automatable if we can automate these test cases that mean 100 % automation?

    2) Design and implementation of framework
    3) Execution
    4) Maintenance (Version control system)

eCommerce Application…
    https://www.nopcommerce.com/en/demo

Frontend    https://demo.nopcommerce.com/
Backend     https://admin-demo.nopcommerce.com/
"""

# Step 1: Create new Project and install Required Packages/plugins
"""
selenium: Selenium Libraries
pytest:         Python UnitTest framework
pytest-html:    Pytest HTML Reports
pytest-xdist:   Run Tests Parallel
openpyxl:       MS Excel Support
allure-pytest:  To generate allure reports
"""
# Step 2: Create Folder Structure
"""
Project Name
    |
    pageObjects(Package)
    |
    testCases(Package)
    |
    utilities(Package)
    |
    TestData(Folder)
    |
    Configurations(Folder)
    |
    Logs(Folder)
    |
    Screenshots(Folder)
    |
    Reports(Folder)
    |
    Run.bat
"""
# Step 3: Automating Login Test Case
"""
3.1: Create LoginPage Object Class under 'pageObjects'
3.2: Create LoginTest under 'testCases'
3.3: Create conftest.py under 'testCases'
"""

# Step 4: capture screenshots on failures
"""
4.1: Update Login Test with Screenshots under 'testCases'
"""

# Step 5: Read common value from an ini file.
"""
5.1: Add 'config.ini' file in 'Configurations' folder
5.2: Crate 'readProperties.py' utility file under utilities package to read common data
5.3: Replace hard coded value in Login test case.
"""

# Step 6: Adding logs to test cases
"""
6.1: Add 'customLogger.py' file under utilities package
6.2: Add logs to Login test case.
"""

# Step 7: Run Tests on Desired Browser/Cross Browser/parallel
"""
7.1: update 'contest.py' with required Fixtures which will accept command line argument(browser name)
7.2: Pass browser name as argument in command line

To Run tests on desired browser
pytest -s -v testCases/test_login.py --browser chrome
pytest -s -v testCases/test_login.py --browser firefox

To Run tests parallel
pytest -s -v  n=3 testCases/test_login.py --browser chrome
pytest -v -s n=3 testCase/test_longin.py --browser firefox
"""

# Step 8: Generate pytest HTML Reports
"""
8.1: Update 'conftest.py with pytest hooks
8.2 To Generate HTML report run below command
    pytest -s -v -n=3 --html=Reports\\report.html testCases/test_login.py --browser chrome
"""

# Step 9: Automating Data Driven Test Case
"""
9.1: Prepare test data in Excel sheet, place the excel file inside the TestData folder.
9.2: Create "ExcelUtils.py' utility class under utilities package.
9.3: Create LoginDataDrivenTest nuder testCases.
9.4: Run the test case
"""
# Step 10: Adding new testcases
"""
1) Add new customer
2) Search customer by email
3) Search customer by name
"""

# Step 11: Grouping Tests
"""
11.1: Grouping markers(Add markers to every test methods)
        @pytest.mark.sanity
        @pytest.mark.regression
        
11.2: Add Markers entries in pytest.ini file
    [pytest]
    markers =   
        sanity
        regression
        
11.3: Select groups at run time
    -m "sanity
    -m "regression"
    -m "sanity and regression"
    -m "sanity or regression"
    
    Run commands
    ------------
    pytest -s -v -m "sanity" --html=./Reports/report.html .\testCases\ --browser chrome
    pytest -s -v -m "regression" --html=./Reports/report.html .\testCases\ --browser chrome
    pytest -s -v -m "sanity and regression" --html=./Reports/report.html .\testCases\ --browser chrome
    pytest -s -v -m "sanity or regression" --html=./Reports/report.html .\testCases\ --browser chrome
"""

# 12: Run Tests in Command Prompt & run.bat file
"""
12.1: Create run.bat file

    pytest -s -v -m "sanity" --html=./Reports/report.html .\testCases\ --browser chrome

12.2: Open command prompt as Administration and then run run.bat file
"""

# 13: Push the Code to Git & GitHub Repository
"""
1st Round
---------
Initial step(only one time)
    1) git init -> Create an empty git repository (Local repository)
    
    2) git remote add origin "link of GitHub repository"
    
Before doing commit first time we need to execute these below commands
    git config --global user.name "lukesh"
    git config --global user.email "adelukesh@gmail.com"
    
    3) git status
    4) git add -A  -> add all the files in to staging/indexing area
    

note:- To update git software which is already install in your local machine 
       The command you have to run in cmd -> git update-git-for-windows
       
echo "# TutorialsNinjaWebApplication-Automation" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/lukesh7385/TutorialsNinjaWebApplication-Automation.git
git push -u origin main

git remote add origin https://github.com/lukesh7385/TutorialsNinjaWebApplication-Automation.git
git branch -M main
git push -u origin main
"""