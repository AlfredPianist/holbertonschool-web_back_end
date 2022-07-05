#!/usr/bin/env python3
"""Client unit tests"""

from parameterized import parameterized, parameterized_class
import unittest
from unittest.mock import patch, PropertyMock
import client
import fixtures


class TestGithubOrgClient(unittest.TestCase):
    """Class testing GithubOrgClient class"""

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json', return_value={})
    def test_org(self, org, get_json):
        """Test org"""
        test_class = client.GithubOrgClient(org)
        self.assertEqual(test_class.org, get_json.return_value)
        get_json.assert_called_once()

    def test_public_repos_url(self):
        """Test _public_repos_url"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock,
                   return_value={'repos_url': 'https://example.org/'}
                   ) as org:
            test_class = client.GithubOrgClient('example')
            self.assertEqual(test_class._public_repos_url,
                             org.return_value['repos_url'])

    @patch('client.get_json',
           return_value=[{'name': 'org_1'}, {'name': 'org_2'}])
    def test_public_repos(self, get_json):
        """Test public_repos"""
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock,
                   return_value={'repos_url': 'https://example.org/'}
                   ) as _public_repos_url:
            test_class = client.GithubOrgClient('example')
            test_result = test_class.public_repos('standard_license')
            self.assertEqual([org['name'] for org in get_json.result_value],
                             test_result)
            get_json.assert_called_once()
            _public_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license, has_license):
        """Test has_license"""
        test_class = client.GithubOrgClient('example')
        self.assertEqual(test_class.has_license(repo, license),
                         has_license)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    fixtures.TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Class testing integration of GithubOrgClient class"""

    @classmethod
    def setUpClass(cls):
        """Setup requests.get patcher"""
        cls.get_patcher = patch('requests.get')
        cls.requests_get = cls.get_patcher.start()
        cls.requests_get.return_value.json.side_effect = [
            cls.org_payload, cls.repos_payload,
            cls.expected_repos, cls.apache2_repos
        ]

    @classmethod
    def tearDownClass(cls):
        """Tear down requests.get patcher"""
        cls.get_patcher.stop()

    def public_repos(self):
        """Test public_repos"""
        test_class = client.GithubOrgClient('example')
        self.assertEqual(test_class.public_repos('test'), [])
        self.assertEqual(test_class.public_repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos based on license"""
        test_class = client.GithubOrgClient('example')
        self.assertEqual(test_class.public_repos(license="apache-2.0"),
                         self.apache2_repos)
