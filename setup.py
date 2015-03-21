import os
from setuptools import setup, find_packages

version = '0.2.5'
long_description = '\n\n'.join([
    open(filename).read() for filename in (
        'README.rst',
        os.path.join('collective', 'elephantvocabulary', 'tests.rst'),
        'CREDITS.rst',
        'CHANGES.rst',)
    ])

setup(name='collective.elephantvocabulary',
      version=version,
      description="type of zope vocabularies that dont \"forget\", like \
                   elephants",
      long_description=long_description,
      classifiers=[
          "Programming Language :: Python",
          "Programming Language :: Zope",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          ],
      keywords='zope plone vocabulary',
      author='Rok Garbas',
      author_email='rok@garbas.si',
      url='http://github.com/collective/collective.elephantvocabulary',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'zope.interface',
          'zope.component',
          'zope.schema',
      ],
      extras_require={
          'test': [
              'plone.registry',
              'zope.dottedname',  # should be dependency of plone.registry
              'plone.testing [zca]',
              ]
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
