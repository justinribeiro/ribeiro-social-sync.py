from setuptools import setup

setup(
    name='ribeiro-social-sync.py',
    version='2.0.0',
    description='Sync Mastodon to Twitter nicely so Justin looks more alive',
    license='MIT License',
    author='Justin Ribeiro',
    author_email='justin@justinribeiro.com',
    install_requires=[
        'docopt', 'Mastodon.py', 'twitter', 'html2text', 'requests'
    ],
    url='https://github.com/justinribeiro/ribeiro-social-sync.py')
