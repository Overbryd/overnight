from langchain.tools import tool

class CodingTools():

    staticmethod
    def all():
        return [
            CodingTools.plan_implementation_steps,
            CodingTools.run_project,
        ]

    @tool("List files")
    def list_files(self, directory, file_ending=None):
        """Useful to list files in a directory, optionally by file ending."""
        pass

    @tool("Write code")
    def write_code(self, current_code=None, acceptance_criteria):
        """Useful to write code or amend current code to meet the acceptance criteria."""
        pass

    @tool("Write a file")
    def write_file(self, file, content):
        """Useful to write a file with the given content."""
        pass

    @tool("Run the project")
    def run_project(self):
        """Useful to test the runnabilty of the project."""
        pass

