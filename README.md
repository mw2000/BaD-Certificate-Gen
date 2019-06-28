# Introduction:
This is an automation script to generate certificates for Blockchain at Davis club.

# Motivation:
Being assigned with a task of making certificates for students who completed the BaD DApp development curriculum for fall quarter, I created this script to make my life easier after attempting to do the task manually.

# Requirements:
It is required that you have python 3.x and pip (specifically pip3) installed on your system

# Dependencies:
- **os**
- **io**
- **textwrap**
- **PyPDF2**
- **reportlab**

# Installation:
For installatiion of the dependencies, run the following command
~~~
python3 setup.py
~~~

# Usage
- **Step 1:** Write the names of the reciepients in the names.txt file, each name separated by a new line
- **Step 2:** Write the msg in the msg.txt file
- **Step 3:** Run the following command
~~~
python3 gen.py
~~~
- **Step 4:** View and export your certificates generated in the 'Generated' folder

# Contributors:
- Mihir Wadekar