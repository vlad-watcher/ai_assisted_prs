import os 
import jira

def get_jira_ticket_description(jira_ticket):
    """
    Return description for provided jira ticket

    Args:
        jira_ticket (_type_): JIRA issue key

    Returns:
        (str): Ticket description
    """
    jira_server = 'https://planetwatchers.atlassian.net/'
    jira_username = os.getenv("JIRA_EMAIL")
    jira_password = os.getenv("JIRA_API_KEY")

    try:
        jira_client = jira.JIRA(server=jira_server, basic_auth=(jira_username, jira_password))
        issue = jira_client.issue(jira_ticket)
    except jira.exceptions.JIRAError as e:
        print(e)
        return ""

    return issue.fields.description