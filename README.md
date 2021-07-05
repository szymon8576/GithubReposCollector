Simple Python app that allows you to list repositories (name and number of stars) and get the sum of stars in all repositories of any GitHub user.

App is built with [Python 3.8](https://www.python.org/), [Flask](https://palletsprojects.com/p/flask/) and [PyGithub library](https://github.com/PyGithub/PyGithub).

Result is returned via HTML in JSON format.

## Installation and running:

1. Clone repository:
```
git clone https://github.com/szymon8576/GithubReposCollector
```
2. Change current directory to app directory:
```
cd GithubReposCollector
```
3. Install requirements:
```
pip install -r requirements.txt
```
4. Set FLASK_APP variable value to app.py:
```
set FLASK_APP=app.py
```
6. Run app:
```
py app.py
```

## Usage:
```
http://127.0.0.1:5000/get_data/[username]
```

### Example usage:
```
http://127.0.0.1:5000/get_data/Allegro
```

### Example result:
```
{
  "username": "Allegro", 
  "stargazers_total": 13104, 
  "repos": {
    "akubra": 79, 
    "allegro-api": 132, 
    "allegro-tech-labs-iot": 1, 
    "allegro-tech-labs-microservices": 6, 
    "allegro.tech": 20, 
    "allRank": 289, 
	
    ...

    "vaas-registration-hook": 2, 
    "vending-machine-kata": 5, 
    "warsztaty-podstawy-ml-03-2019": 2
  }
}
```
## Developments plans:
1. Store results in database and use them for tracking programming trends and for commercial analysis
2. Collect more information such as used languages, number of commits
3. More reliable error handling and debugging

## Additional information

My application uses public access token to communicate with GithubAPI - this means that there is a limit of 60 GitHubAPI-requests per hour. To lift it, you should generate a private access token using your GitHub account.
