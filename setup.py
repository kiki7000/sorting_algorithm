import setuptools

setuptools.setup(
    name = 'kiki_sort',
    version = '1.0.1',
    description = 'Sort Functions',
    license = 'GNUv3',
    author = 'kiki7000',
    url = 'https://github.com/kiki7000/sorting_algorithm',
    author_email = 'devkiki7000@gmail.com',
    packages = setuptools.find_packages(),
    keywords = ['kiki', 'sort'],
    python_requires = '>=3.6',
    install_requires = ['asyncio'],
    zip_save = False
)