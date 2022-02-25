# PythonFramework
This is a demo python with selenium test automation framework

@Sangrambadi - 04/02/2022

this skeleton framework can run the tests parallaly using selnium grid

Mobile, IE and Chrome features are already added, stil You can extend the framework.

Command line arguments can be passed to run a feature file with a specific tag name.

  - Create a folder named tools on your dektop
  - add a .bat file(local_grid) with content as:
  
    CD C:\Users\{your_username}\Desktop\tools
  START "SELENIUM HUB" java -jar selenium-server-standalone-3.141.59.jar -role hub -timeout 360
  START "SELENIUM NODE - CHROME-5 INSTANCES" java -Dwebdriver.chrome.driver="D:\chrome\chromedriver2_42.exe" -jar selenium-server-standalone-3.141.59.jar -role node -hub http://localhost:4444/grid/register -browser browserName=chrome,maxInstances=5,maxSession=5,platform=WINDOWS
  START "SELENIUM NODE IE -1 INSTANCE" java -Dwebdriver.ie.driver="D:\ie\IEDriverServer3_14_0.exe" -jar selenium-server-standalone-3.141.59.jar -role node -hub http://localhost:4444/grid/register -browser browserName="internet explorer",maxInstance=1,maxSession=1,platform=WINDOWS
  
  
  - Put the java standalone server jar file(selenium-server-standalone-3.141.59) in side tools folder
  - Put the Chrome/IE driver details correctly in above batch file
  - once done start the grid by running the local_grid.bat file
  - Import the framework on your Pycharm
  - Click the edit configuration (near Play button on pycharm)
  - Click Python from Add new configuration Menu
  - you will see configuration pop up
  - Give the script path to parallel_runner.py file
  - in parameters you pass the feature file name as -feature {feature file name} -tag {tag_name}
  - That's it you run your first program
  - Now you have framework ready, you can extend it with your own requirements
  - 



