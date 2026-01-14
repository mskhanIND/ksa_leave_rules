from setuptools import setup, find_packages

setup(
    name="ksa_leave_rules",
    version="0.1.0",
    description="Sick-leave splitting logic for KSA leave rules (Article 117)",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="mskhanIND",
    license="MIT",
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=[],
)
