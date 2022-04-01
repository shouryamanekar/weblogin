NOTE : this program only works on pages where the id of login button does not changes when the page is refreshed.


Running the Code

1. Check your chrome version ( Its better to be on lastest version of Chrome )
2. Download the chromedriver same as your chrome version from the given link ( https://chromedriver.chromium.org/downloads )
   Note : version of chromedriver must match with your chrome version.
3. Extract the chromedriver on C drive.
   Note : [ C:\chromedriver ]
4. Open the python code on any editor.
5. Enter your login URL, Username and Password on line number 13. 
   [ login("Enter your Login URL link here", "username", "Enter your Username here", "password", 'Enter your Password here', "loginbutton id") ]
6. Now go to your login page and inspect the Username, Password and Login button.
7. Find for your Username, Password and Login button id.
   Note: The id of Username and Password are the lower case [username;password].It is difficulr to find the id of login button as every website has diffrent    name of login ( sign in, submit, enter, etc) and the id may vary in every website as some website change there login button id every time you refresh them. Generally the login button id are loginbutton , login , submit, etc.
8. Find the id's and put them in line 13 of the code and dont forget to add the URL.
9. Run the code

Creating the exe file

1. Install pyinstaller.
2. Write the following code in your console [ pyinstaller --onefile XYZ.py ]
   Note: put your filename instead of XYZ
3. Your exe file is ready
4. Check for your exe file in dist folder in same directory where the python file is saved.
5. Run the exe file.

Autostart the exe

1. Press windows key + r
2. Copy the run command Shell:common startup
3. It will reach C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup
4. Create the shortcut of the program you want to run in startup.
5. Copy the shortcut to the startup folder.
6. Restart the computer.
