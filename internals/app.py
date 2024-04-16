import os
import json
from .tools.get_jira_ticket import get_jira_ticket_description
from .tools.github_integration import get_last_closed_pull_requests
from .tools.templates import (
    PROMPT_START_TEMPLATE
)
from .tools.gemini_ai import get_gemini_model
from .tools.extract_jira_ticket_from_pr import extract_jira_ticket_from_pr_title
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gh_repo", type=str, required=True, help="Github repository in format owner/repository")
    parser.add_argument("--prs", type=str, default="10", help="Number of PRs to process")
    parser.add_argument("--gemini_key", type=str, help="Gemini API key")

    args = parser.parse_args()

    if args.gemini_key:
        os.environ["GEMINI_KEY"] = args.gemini_key

    github_repo = args.gh_repo

    repo_name = github_repo.split("/")[1]

    repository_prs = get_last_closed_pull_requests(github_repository=github_repo, prs=args.prs)

    gemini_model = get_gemini_model()
    ai_answers = []

    for pr_number, pr in repository_prs.items():
        pr["jira_key"] = extract_jira_ticket_from_pr_title(pr["title"])
        if pr["jira_key"]:
            pr["jira_description"] = get_jira_ticket_description(pr["jira_key"])

        pr = {"project_name": repo_name,"link_to_pr": f"https://github.com/{github_repo}/pull/{pr_number}", **pr}
        json_string_pr = json.dumps(pr)
        full_prompt = PROMPT_START_TEMPLATE + json_string_pr
        answer = gemini_model.generate_content(full_prompt).text

        ai_answers.append(answer)

    for answer in ai_answers:
        print("-"*100)
        print(answer)



if __name__ == "__main__":
    main()