import requests
from datetime import datetime

class GithubApiClient:
    """
    A GitHub API client that fetches data from the GitHub API.
    """

    BASE_URL = "https://api.github.com"

    def __init__(self, token):
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }

    def fetch_users_from_team(self, team_name):
        # For the sake of simplicity, we'll assume the team is under a known organization
        url = f"{self.BASE_URL}/orgs/ministryofjustice/teams/{team_name}/members"
        response = requests.get(url, headers=self.headers, timeout=5)
        response.raise_for_status()

        users = [user['login'] for user in response.json()]
        return users

    def fetch_last_activity(self, username, repo_name):
        # For simplicity, we'll fetch the user's events and extract the latest one
        url = f"{self.BASE_URL}/users/{username}/events/repos/ministryofjustice/{repo_name}"
        response = requests.get(url, headers=self.headers, timeout=5)
        response.raise_for_status()

        if not response.json():
            return None

        latest_event = response.json()[0]
        return datetime.strptime(latest_event["created_at"], "%Y-%m-%dT%H:%M:%SZ")

