Name:       os-net-config
Version:    10.4.1
Release:    0.20170914.77fe592%{?dist}.1
Summary:    Host network configuration tool

License:    %{_platform_licence} and ASL 2.0
URL:        http://pypi.python.org/pypi/%{name}
Source0:    https://files.pythonhosted.org/packages/26/8d/c9ce44fd6a805a4ec56cba59c0a6743fba2230b7b79aa57a48709e94f47c/%{name}-%{version}.tar.gz
Patch0:     0001-initial.patch
Vendor:     OpenStack Foundation and %{_platform_vendor} modified

BuildArch:      noarch
BuildRequires:  python-setuptools
BuildRequires:  python2-devel
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx

Requires:   python-anyjson >= 0.3.3
Requires:   python-eventlet >= 0.18.2
Requires:   python-oslo-concurrency >= 3.8.0
Requires:   python-oslo-config
Requires:   python-oslo-utils >= 3.20.0
Requires:   python-netaddr >= 0.7.13
Requires:   python-netifaces >= 0.10.4
Requires:   python-iso8601 >= 0.1.11
Requires:   python-six >= 1.9.0
Requires:   initscripts
Requires:   iproute
Requires:   ethtool
Requires:   openvswitch
Requires:   dhclient
Requires:   PyYAML >= 3.10
Requires:   python2-pbr >= 2.0.0
Requires:   python-jsonschema >= 2.0.0
Requires:   driverctl

%description
Host network configuration tool for OpenStack.

%prep

%autosetup -n %{name}-%{version} -p 1

%build
%{__python} setup.py build
%{__python} setup.py build_sphinx

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc README.rst
%doc LICENSE
%doc doc/build/html
%{_bindir}/os-net-config
%{python_sitelib}/os_net_config*
