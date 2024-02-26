from langchain.tools import tool

class RepositoryTools():

    staticmethod
    def all():
        return [
            RepositoryTools.clone_repository,
            RepositoryTools.create_feature_branch,
            RepositoryTools.run_project,
            RepositoryTools.commit,
            RepositoryTools.push,
        ]

    def __init__(self, repository):
        self.repository = repository

    @tool("Clone the repository")
    def clone_repository(self, user_id);
        """Useful to create a new working directory for the repository to isolate a single user."""
        pass

    @tool("Create a feature branch")
    def create_feature_branch(self, user_id, session_id, issue_id):
        """Useful to isolate work and changes in a repository for a given user, session and issue."""
        pass

    @tool("Run the project")
    def run_project(self):
        """Useful to test the runnabilty of the project."""
        pass

    @tool("Commit changes")
    def commit(self):
        """Useful to package all changes with a summary."""
        pass

    @tool("Pull and merge changes")
    def pull_and_merge(self, from_branch='main'):
        """Useful to merge changes from another branch."""
        pass

    @tool("Push changes")
    def push(self):
        """Useful to publish a set of commits to the remote branch of the repository."""
        pass

    @tool("Reset working directory")
    def reset_working_direcotry(self):
        """Useful to start a fresh work session from the main branch."""
        pass

