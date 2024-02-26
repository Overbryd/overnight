import shortuuid
from glob import glob
import yaml
from langchain.tools import tool

class ManagementTools():

    staticmethod
    def all():
        return [
            ManagementTools.get_issues,
            ManagementTools.create_issue,
            ManagementTools.get_issue,
            ManagementTools.update_issue,
            ManagementTools.comment_issue,
            ManagementTools.assign_issue,
            ManagementTools.close_issue,
        ]

    def __init__(self, repository):
        self.repository = repository

    @tool("Get all issues from the repository")
    def get_issues(self, author=None, assignee=None, state=None):
        """Useful to get a list of issues, optionally filtered by author, assignee, or state."""
        for name in glob(f'{self.repository}/issues/*.issue.yml'):
            with open(name) as f:
                issue = yaml.safe_load(f)
                if author and issue['author'] != author:
                    continue
                if assignee and issue['assignee'] != assignee:
                    continue
                if state and issue['state'] != state:
                    continue
                yield issue

    @tool("Create a new issue")
    def create_issue(self, author, title, body, acceptance_criteria):
        """Useful to note down a new task, bug or feature.
        The issue MUST have a title, body and a list of acceptance criteria.
        """
        issue_id = shortuuid.uuid()
        with open(f'{self.repository}/issues/{issue_id}.issue.yml', 'w') as f:
            yaml.dump({
                'issue_id': issue_id,
                'title': title,
                'body': body,
                'acceptance_criteria': acceptance_criteria,
                'author': author,
                'assignee': None,
                'state': 'open',
                'comments': [],
            }, f)

    @tool("Get a single issue from the repository")
    def get_issue(self, issue_id):
        """Useful to get a single known issue by its id."""
        with open(f'self.repository/issues/{issue_id}.issue.yml') as f:
            return yaml.safe_load(f)

    @tool("Update an issue")
    def update_issue(self, issue_id, assignee=None, state=None, title=None, body=None, acceptance_criteria=None):
        """Useful to update an issue, for example to change the assignee, state, title, body or acceptance_criteria."""
        issue = self.get_issue(issue_id)
        if assignee:
            issue['assignee'] = assignee
        if state:
            issue['state'] = state
        if title:
            issue['title'] = title
        if body:
            issue['body'] = body
        if acceptance_criteria:
            issue['acceptance_criteria'] = acceptance_criteria
        with open(f'self.repository/issues/{issue_id}.issue.yml', 'w') as f:
            yaml.dump(issue, f)

    @tool("Comment on an issue")
    def comment_issue(self, issue_id, author, comment):
        """Useful to add a comment to an issue, in order to ask a question,
        provide an answer or leave a message to another team member.
        Other team members can be tagged by @username."""
        comment_id = shortuuid.uuid()
        issue = self.get_issue(issue_id)
        issue['comments'].append({
            'comment_id': comment_id,
            'author': author,
            'comment': comment,
        })
        with open(f'self.repository/issues/{issue_id}.issue.yml', 'w') as f:
            yaml.dump(issue, f)

    @tool("Assign an issue to a user")
    def assign_issue(self, issue_id, assignee):
        """Delegate a task to a specific role in the team."""
        issue = self.get_issue(issue_id)
        issue['assignee'] = assignee
        with open(f'self.repository/issues/{issue_id}.issue.yml', 'w') as f:
            yaml.dump(issue, f)

    @tool("Close an issue")
    def close_issue(self, issue_id):
        """Mark an issue as completed by the definition of done.
        Before an issue can be closed, all acceptance criteria MUST be met.
        """
        issue = self.get_issue(issue_id)
        issue['state'] = 'closed'
        assert all([c['fulfilled'] == True for c in issue['acceptance_criteria']])
        with open(f'self.repository/issues/{issue_id}.issue.yml', 'w') as f:
            yaml.dump(issue, f)

