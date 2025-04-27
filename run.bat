@echo off
set BROWSER=headless
@REM set BROWSER=chrome
rem set BROWSER=edge
rem set BROWSER=firefox


rem Run sanity tests
rem pytest -s -v -m "sanity" --html=./Reports/report.html .\testCases\ --browser %BROWSER%

rem Run regression tests
rem pytest -s -v -m "regression" --html=./Reports/report.html .\testCases\ --browser %BROWSER%

rem Run tests marked as both sanity and regression
rem pytest -s -v -m "sanity and regression" --html=./Reports/report.html .\testCases\ --browser %BROWSER%

rem Run tests marked as either sanity or regression
rem pytest -s -v -m "sanity or regression" --html=./Reports/report.html .\testCases\ --browser %BROWSER%


rem pytest -s -v -m "sanity" --alluredir=allureReports --html=./Reports/report.html .\testCases\ --browser %BROWSER%
rem pytest -s -v -m "regression" --alluredir=allureReports --html=./Reports/report.html .\testCases\ --browser %BROWSER%
rem pytest -s -v -m "sanity and regression" --alluredir=allureReports --html=./Reports/report.html .\testCases\ --browser %BROWSER%
@REM pytest -s -v -n=3 -m "sanity or regression" --alluredir=allureReports --html=./Reports/report.html .\testCases\ --browser %BROWSER%
pytest -s -v -n=3 --alluredir=allureReports --html=./Reports/report.html .\testCases\ --browser  %BROWSER%

cmd /k
