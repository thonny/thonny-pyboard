from setuptools import setup
import os.path
import sys

setupdir = os.path.dirname(__file__)

requirements = []
for line in open(os.path.join(setupdir, 'requirements.txt'), encoding="UTF-8"):
    if line.strip() and not line.startswith('#'):
        requirements.append(line)

setup(
      name="thonny-pyboard",
      version="0.1b1",
      description="PyBoard MicroPython support for Thonny",
      long_description="""This is a plug-in for Thonny which adds PyBoard MicroPython backend. 
More info about Thonny: http://thonny.org.""",
      url="https://bitbucket.org/plas/thonny-pyboard/",
      author="Aivar Annamaa",
	  author_email="aivar.annamaa@gmail.com",
      license="MIT",
      classifiers=[
        "Environment :: MacOS X",
        "Environment :: Win32 (MS Windows)",
        "Environment :: X11 Applications",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "License :: Freeware",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Education",
        "Topic :: Software Development",
        "Topic :: Software Development :: Embedded Systems",
      ],
      keywords="IDE education programming PyBoard MicroPython Thonny",
      platforms=["Windows", "macOS", "Linux"],
      python_requires=">=3.4",
	  package_data={'thonnycontrib.pyboard': ['dummy_modules/*',  'res/*']},
      install_requires=requirements,
      packages=["thonnycontrib.pyboard"],
)