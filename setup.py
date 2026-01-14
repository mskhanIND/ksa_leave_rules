from setuptools import setup, find_packages

setup(
    name="ksa_leave_rules",
    version="0.1.0",
    description="Saudi Arabia compliant sick leave rules for Frappe HRMS",
    author="Mohd Mohsin Khan",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=["frappe"],
)

