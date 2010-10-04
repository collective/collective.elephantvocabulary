from setuptools import setup, find_packages

version = '0.1'

setup(name='collective.hiddentermsvocabulary',
      version=version,
      description="zope vocabulary with possibility to hide terms",
      long_description=open("README.txt").read(),
      classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Zope",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        ],
      keywords='zope plone vocabulary',
      author='Rok Garbas',
      author_email='rok@garbas.si',
      url='http://github.com/collective/collective.hiddentermsvocabulary',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
