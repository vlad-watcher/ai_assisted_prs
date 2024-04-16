
PROMPT_START_TEMPLATE = """
I'm going to provide you object that contains information about task with relevant PR and JIRA ticket.
The format of data will be json like in example:

{
    "pr_number": "Number of PR",
    "link_to_pr": "Link to PR",
    "pr_title": "Title of PR",
    "commits:": ["Commit message 1", "Commit message 2", "Commit message 3"],
    "jira_description": "Description of JIRA ticket"
}

Respond in a JSON format with keys: 'project_name', 'pr_number', 'link_to_pr', 'description', 'changes'
Where:
 - description is a meaningful and detailed description based on PR and/or JIRA ticket how you understand it. If you have problem with this description, use original pr title value.
 - changes is a list of what you think was done based on commit messages
 - project_name is a name of the project
 - pr_number is a number of PR
 - link_to_pr is a link to PR


Here's the information:
"""