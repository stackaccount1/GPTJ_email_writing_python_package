from setuptools import setup, find_packages

setup(name='ira_email_writer',
      version='0.0',
      description='ira_email_writer',
      url='na',
      author='stackaccount1',
      author_email='na',
      license='mit',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      package_data={'ira_email_writer': ['data/*.txt']},
      install_requires=[
              "importlib-resources==5.2.2", 
      	      "gptj==2.2.5", 
              "numpy==1.21.2", 
              "pandas==1.3.3", 
              "pandas-ods-reader==0.1.2", 
              "python-dateutil==2.8.2",
      		],
      zip_safe=False)
      
     
