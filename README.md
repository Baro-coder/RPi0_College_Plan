# RPi0_College_Plan

## Description

**Python Web Scrapping** program developed to download lessons plan
from WAT WCY website.

Program uses *BeutifulSoup* and *requests* python modules
to get website source code and parse it into prepared data structures.
Next all the data is being stored to csv file to future use by external
programs.

Program is prepared for Raspberry Pi use with Raspbian OS.

---

## Cron

To automate the operation of the sccript, the program call
is specified in **crontab**.

### **Example cron record**

```code
# Execute everyday at 04:00 AM
# - Download College Plan from WAT WCY Website
# - Store data to csv file
# - Redirected streams: out, err

0 4 * * * /bin/bash /home/pi/.Private/college_plan.sh run > /home/pi/.Private/college_plan.log 2> /home/pi/.Private/college_plan.err.log
```
