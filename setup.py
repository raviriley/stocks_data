from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='stocks_data',
    version='0.1',
    description='data management system',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    author='Ravi Riley',
    author_email='ravi@intoolovation.com',
    keywords=['stocks', 'data', 'stockdata'],
    url='https://github.com/raviriley/stocks_data',
    download_url='https://pypi.org/project/stocks_data/'
)

install_requires = [
    'pandas',
    'pandas-datareader'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)