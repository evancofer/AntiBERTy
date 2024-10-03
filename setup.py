import os
import tarfile
import urllib.request
import shutil
import setuptools
from setuptools.command.install import install


class DownloadModelCommand(install):
    def run(self):
        install.run(self)
        url = "https://files.pythonhosted.org/packages/a1/3b/2cf48ec21956252fdc5c5dd1b7f8bb8b12f5208bd3eaaad412ced3ed0ff5/antiberty-0.1.3.tar.gz"
        urllib.request.urlretrieve(url, "./antiberty-0.1.3.tar.gz")
        with tarfile.open("antiberty-0.1.3.tar.gz", "r:gz") as tar:
            tar.extractall()
        shutil.move("antiberty-0.1.3/antiberty/trained_models", "antiberty/trained_models")
        shutil.rmtree("antiberty-0.1.3")
        os.remove("./antiberty-0.1.3.tar.gz")



setuptools.setup(cmdclass={"install": DownloadModelCommand})
