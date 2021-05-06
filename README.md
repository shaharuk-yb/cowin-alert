# cowin-alert
Get the alert sound whenever vaccine is available.

Created by: https://github.com/gurushant-yb (https://www.linkedin.com/in/gurushant-jidagi-911a4413)

## How to use:

This app will make siren sound when there is any vaccine availability in a given pin codes

1. Open main.py and add pin codes in at line number main.py:63, add only those pin codes which are nearby to your location.
2. Create python environment & use these commands to run app 
```
    pip install -r requirements.txt
    nohup Python -W ignore main.py > output.txt &
```
3. Pass correct date to crawl_cowin(main.py:67) method , format is dd-mm-yyyy
4. It prints the pin code(in output.txt) and starts siren noise and exits
