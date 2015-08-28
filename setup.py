from distutils.core import setup

setup(
    name='chimera_t80dome',
    version='0.0.1',
    packages=['chimera_t80dome', 'chimera_t80dome.instruments'],
    scripts=[],
    url='http://github.com/astroufsc/chimera-t80dome',
    license='GPL v2',
    author='Tiago Ribeiro and Salvador Agati',
    author_email='tribeiro@ufs.br',
    requires=['chimera','chimera-astelco','chimera-commander'],
    description=''
)
