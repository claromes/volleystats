from setuptools import setup, find_packages
import re

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt', 'r', encoding='utf-8') as f:
    install_requires = f.read().splitlines()

with open('matchscraper/version.py', 'r', encoding='utf-8') as f:
    version = re.search(r"^__version__\s*=\s*'(.*)'.*$",
        f.read(), flags=re.MULTILINE).group(1)

setup(
    name='matchscraper',
    version=version,
    author='claromes',
    description='CLI tool to get volleyball match statistics from the Web Competition by Data Project websites',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='volleyball sports cli dataset analytics',
    url='https://github.com/claromes/matchscraper',
    project_urls={
        'Documentation': 'https://claromes.github.io/matchscraper/',
        'Issue Tracker': 'https://github.com/claromes/matchscraper/issues',
    },
    packages=find_packages(exclude=['docs']),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Framework :: Scrapy',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Utilities'
    ],
    python_requires='>=3.8',
    install_requires=install_requires,
    entry_points = {
		'console_scripts': [
			'matchscraper = matchscraper.main:main',
		],
	},
)
