import re
def extract_jira_ticket_from_pr_title(gh_title: str) -> str:
    """
    Extract Jira ticket from PR title

    Args:
        gh_title (str): GitHub PR title
    """
    issue_key = ""
    keywords = ["scrum", "dops"]
    for keyword in keywords:
        if gh_title.startswith(keyword):
            regex = r"(?<={})\W*([A-Z0-9]+)".format(keyword)
            match = re.search(regex, gh_title)
            if match:
                issue_key = f"{keyword.upper()}-{match.group(1).upper()}"
                break
    return issue_key