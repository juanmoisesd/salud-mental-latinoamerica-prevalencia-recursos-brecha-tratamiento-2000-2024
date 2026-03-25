from setuptools import setup, find_packages
setup(
    name="salud-mental-latinoamerica-prevalencia-recursos-brecha-tratamiento-2000-2024",
    version="1.0.0",
    description="Base de datos de salud mental en 10 países de América Latina (2000–2024): depresión, ansiedad, suici",
    author="de la Serna, Juan Moisés",
    url="https://github.com/juanmoisesd/salud-mental-latinoamerica-prevalencia-recursos-brecha-tratamiento-2000-2024",
    packages=find_packages(),
    install_requires=["pandas>=1.3.0","requests>=2.26.0"],
    python_requires=">=3.7",
    classifiers=["Programming Language :: Python :: 3","License :: OSI Approved :: MIT License","Topic :: Scientific/Engineering"],
    keywords="zenodo, open-data",
)