"Python Turtle Graphics window shows nothing"

The Turtle.py code do not contains any error but the python graphics return a black screen
Following the next steps to resolve the issue:

The main problem is related to the version of python 3.10.0 and lower.

Check if you already have python 3.11.0 --> open a terminal python --version 

Close all the think that you have opened and restart your PC.

Create a new folder on Desktop called for example: Turtle

Then open Visual Studio Code and create a new file called Turtle.py 

copy paste the code 

Open the terminal from visual studio and launch the following command: 

check that you are in the correct path

/Desktop/Turtle

if not:

----------------------------------------------
ls

----------------------------------------------
cd Desktop

----------------------------------------------
cd Turtle

----------------------------------------------
pyenv uninstall 3.11.0

----------------------------------------------
brew install tk

----------------------------------------------
CFLAGS="-I$(brew --prefix tk)/include" \
LDFLAGS="-L$(brew --prefix tk)/lib" \
pyenv install 3.11.0

----------------------------------------------
pyenv virtualenv 3.11.0 turtlenv

----------------------------------------------
pyenv activate turtlenv

With the steps above you have create a new enviroment with the python 3.11 installed and if you run again the code now you can see that it's working!

