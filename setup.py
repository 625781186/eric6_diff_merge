from setuptools import setup, find_packages


VERSION = '1.0.0'
NAME = "eric6_diff_merge"

with open("README.md","r",encoding="utf-8") as fp:
    long_description = fp.read()

      
setup(name=NAME,
      version=VERSION,
      classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='python、python diff merge',
      author='Lin JH',
      author_email='625781186@qq.com',
      url='https://github.com/625781186/eric6_diff_merge',
      license='GPL-3.0',
      description="python diff merge tool.",
      long_description=long_description,
      long_description_content_type='text/markdown',  # This is important
      # --------------------------------------------#
      # package_dir={'source': './gitpyman'},
      packages=find_packages(),
      include_package_data=True,  # 和下面的写法冲突

      zip_safe=False,
      # copy .py file to python's Srcipts
      scripts=[],


      )


