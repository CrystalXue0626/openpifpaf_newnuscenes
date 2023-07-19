from setuptools import setup, find_packages

setup(
    name='openpifpaf_newnuscenes',
    packages= ['openpifpaf_newnuscenes'],
    license='MIT',
    version = '0.1.0',
    description='OpenPifPaf newNuScenes datset PlugIn',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='CrystalXue0626',
    url='https://github.com/CrystalXue0626/openpifpaf_newnuscenes',

    install_requires=[
        'openpifpaf>=0.12b1',
    ],
)
