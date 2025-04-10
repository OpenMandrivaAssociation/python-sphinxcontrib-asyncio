%define module sphinxcontrib-asyncio
%define oname sphinxcontrib_asyncio

Name:		python-sphinxcontrib-asyncio
Version:	0.3.0
Release:	1
Summary:	Sphinx extension to support coroutines in markup
URL:		https://pypi.org/project/sphinxcontrib-asyncio/
License:	Apache-2.0
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/s/sphinxcontrib-asyncio/sphinxcontrib-asyncio-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch

BuildRequires:	make
BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(sphinx)

%description
Sphinx extension to support coroutines in markup.

%prep
%autosetup -n %{module}-%{version} -p1
# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
%py3_build

%install
%py3_install

%files
%{python3_sitelib}/sphinxcontrib
%{python3_sitelib}/%{oname}-%{version}*.*-info
%doc README.rst
