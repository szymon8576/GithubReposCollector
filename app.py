from flask import Flask
from github import Github, GithubException

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

g = Github()


@app.route('/get_data/<username>')
def get_data(username):
    """
    Function that fetches info about desired GitHub user
    :param username: desired username
    :return: dictionary containing username, list of his repos and numbers of stars
    """

    try:
        user = g.get_user(username)
    except GithubException as err:
        return f"An error occured while fetching {username} repos data: {err.data['message']}", err.status

    repos_list = {'username': username, 'stars_total': 0, 'repos': {}}

    for repo in user.get_repos():
        repos_list['repos'][repo.name] = repo.stargazers_count
        repos_list['stars_total'] += repo.stargazers_count

    return repos_list, 200

if __name__ == '__main__':
    app.run()
