from setuptools import find_packages, setup
setup(
    name='robustify',
    packages=find_packages(include=['robustify', 'tests']),
    version='0.0.1',
    description='no description',
    author='Isabel Foster',
    license='MIT',
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.10",
    ],
    install_requires=['numpy<=1.24', 
                      'scikit-learn==1.2.2', 
                      'matplotlib==3.7.1', 
                      'pandas==2.0.1', 
                      'plotly==5.14.1', 
                      'tqdm==4.64.1',
                      'chart_studio==1.1.0', 
                      'python-dotenv==1.0.0',
                      'tensorflow==2.11.1',
                      'kaleido==0.2.1',
                      'ipython==8.11.0',
                      'eli5==0.13.0',
                      'lime==0.2.0.1',
                      'shap==0.41.0',
                      'torch==2.0.1'], # list of packages that are absolutely needed, not standard library
    setup_requires=['pytest-runner'], # only installed when required to run tests
    tests_require=['pytest==7.3.1'],
    test_suite='tests',
)
    
