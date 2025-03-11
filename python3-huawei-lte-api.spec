# Conditional build:
%bcond_without	tests	# unit tests

%define		pkgname	huawei-lte-api
%define		module	huawei_lte_api

Summary:	API For huawei LAN/WAN LTE Modems
Name:		python3-huawei-lte-api
Version:	1.9.3
Release:	3
License:	LGPL v3
Group:		Libraries/Python
# if pypi:
Source0:	https://github.com/Salamek/huawei-lte-api/archive/refs/tags/%{version}.tar.gz
# Source0-md5:	0ad940d542f881a03e1d8a4b3a60598e
URL:		https://github.com/Salamek/huawei-lte-api
BuildRequires:	python3-modules >= 1:3.7
%if %{with tests}
BuildRequires:	python3-pycryptodomex
BuildRequires:	python3-dicttoxml
BuildRequires:	python3-xmltodict
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
API For huawei LAN/WAN LTE Modems, you can use this to simply send
SMS, get information about your internet usage, signal, and tons of
other stuff.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%py3_build

%if %{with tests}
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}*-py*.egg-info
