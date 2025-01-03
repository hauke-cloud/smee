Name:           smee
Version:        0.0.1
Release:        1%{?dist}
Summary:        A package which provides smee a container ships captian best friend

License:        GPL-3.0
Source0:        %{name}-%{version}.tar.gz

%global debug_package %{nil}

%description
Smee provides easy to spin up working environments by using open container technologies.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/usr/bin
cp -a src/usr/bin/smee %{buildroot}/usr/bin/

%files
/usr/bin/smee

%changelog
* Wed Dec 25 2024 Hauke Mettendorf <hauke@mettendorf.it> - 0.0.1
- Initial version
