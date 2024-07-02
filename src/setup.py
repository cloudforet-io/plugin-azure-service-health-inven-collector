#
#   Copyright 2020 The SpaceONE Authors.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


from setuptools import setup, find_packages

with open("VERSION", "r") as f:
    VERSION = f.read().strip()
    f.close()

setup(
    name="plugin-azure-inven-v2-collector",
    version=VERSION,
    description="MS Azure cloud service inventory v2 collector",
    long_description="",
    url="https://cloudforet.io/",
    author="Cloudforet Admin",
    author_email="admin@cloudforet.io",
    license="Apache License 2.0",
    packages=find_packages(),
    install_requires=[
        "spaceone-api",
        "azure-identity",
        "azure-mgmt-resource",
        "azure-mgmt-resourcehealth",
        "azure-mgmt-advisor==10.0.0b1",
    ],
    package_data={
        "plugin": [
            "metadata/*/*.yaml",
            "metrics/**/**/*.yaml",
        ]
    },
    zip_safe=False,
)