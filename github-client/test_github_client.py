import unittest
from unittest.mock import patch
from github_client import GithubApiClient

class TestGithubApiClient(unittest.TestCase):

    def setUp(self):
        self.client = GithubApiClient(token="FAKE_TOKEN")

    @patch('requests.get')
    def test_fetch_users_from_team(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.json.return_value = [{'login': 'user1'}, {'login': 'user2'}]
        team_name = "sample_team"
        users = self.client.fetch_users_from_team(team_name)
        self.assertIsNotNone(users)
        self.assertEqual(users, ['user1', 'user2'])

    @patch('requests.get')
    def test_fetch_last_activity(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.json.return_value = [{'created_at': "2023-07-28T10:10:10Z"}]
        username = "sample_user"
        repo_name = "sample_repo"
        last_activity = self.client.fetch_last_activity(username, repo_name)
        self.assertIsNotNone(last_activity)

if __name__ == "__main__":
    unittest.main()
