from setuptools import setup

VERSION = "1.2.8"
REQUIRES = [
    "pyjwt>=1.7.1",
    "requests>=2.18.0",
    "dataclasses>=0.6",
    "dataclasses-json>=0.2.14",
    "meiga>=0.1.1",
]

setup(
    name="alice-onboarding",
    version=VERSION,
    description="Alice Onboarding Python SDK",
    url="http://alicebiometrics.com",
    author="ALiCE Biometrics",
    author_email="support@alicebiometrics.com",
    license="ALiCE Copyright",
    packages=["alice", "alice/onboarding", "alice/auth", "alice/sandbox"],
    zip_safe=False,
    install_requires=REQUIRES,
)
