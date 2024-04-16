from setuptools import setup, find_packages


setup(
    name='ai_assisted_prs',
    description='Tool for enchansing PRs information with AI',
    version='1.0',
    url="https://github.com/vlad-watcher/ai_assisted_prs",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'google-generativeai', "python-dotenv", "jira"
    ],
    entry_points={
        'console_scripts': [
            'ai_pr = internals.app:main',
        ],
    },
)
