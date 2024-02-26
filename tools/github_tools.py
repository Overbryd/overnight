from github import Github
from github import Auth
from langchain.tools import tool

class GithubTools():

    @tool("Get issues from a Github repository")
    def get_issues(self, repo):
        return repo.get_issues()
