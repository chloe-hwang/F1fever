# F1fever 

This project is designed to create a safe space for Formula 1 Fans to bet on which driver will win a given Grand Prix, and does NOT require real money to be wagered.

Users can select a Grand Prix race to bet on, and input their bets on who will the winner be. Users can also choose to invite other players to place wagers via email. 

After the Grand Prix race, this project will showcase the results of the race, such as driver rankings and race times. 


# Getting Started 
This project requires Python version 3.8 or above 

create and activate virtual environment 
```sh 
conda create -n formula-env python=3.8
conda activate formula-env
```

# Requirements  
Packages and other requirements are listed on the requirements.txt file
```sh 
pip install -r requirements.txt
```

You might have to use 
```sh
pip3 install -r requirements.txt
```

# Running the Web App (Locally)
You can run it from the root directory like this:
```sh
FLASK_APP=web_app flask run
```


# Deploying to Heroku 
Use the command-line to create a new application server, specifying a unique name (e.g. "formula1fever" but yours will need to be different):
```sh
heroku create formula1fever
```

Verify the app has been created:
```sh
heroku apps
``` 

Also verify this step has associated the local repo with a remote address called "heroku":
```sh
git remote -v
```

"Deploy" the application's source code to the Heroku server:
```sh
git push heroku main
```

# Running Tests 
Pytest is a mature full-featured Python testing tool that helps you write better programs.
```sh
pytest
```




# Authors 
Chloe Hwang 
Hyun Bong Jeung 
Asia Rupert 

