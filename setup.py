from setuptools import setup, find_packages

setup(
    name='sudo-sdk',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A Python SDK for AI-powered task execution with container orchestration and blockchain integration.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/sudo-sdk',
    packages=find_packages(),
    install_requires=[
        'docker>=5.0.0',
        'web3>=5.0.0',
        'pytest>=6.0.0',
        'requests>=2.0.0',
        'pyyaml>=5.0.0',
        # Add any other dependencies you need
    ],
    tests_require=[
        'pytest',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    include_package_data=True,
    data_files=[
        # Optional: If you have other files to include (e.g., config files)
        ('/etc/sudo-sdk', ['config/default_config.yaml']),
    ],
    entry_points={
        'console_scripts': [
            'sudo-sdk-cli=sdk.cli:main',  # Example CLI command
        ],
    },
)
