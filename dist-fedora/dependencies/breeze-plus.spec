Name:           breeze-plus
Version:        6.17.0
Release:        1
Summary:        Breeze Styled extra icon theme for KDE

License:        LGPL-2.1-only
URL:            https://github.com/mjkim0727/breeze-plus
BuildArch:      noarch

Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

Requires:       breeze-icon-theme

%description
Breeze Plus is a fork of the KDE Breeze icon theme, providing a light and a dark variant with more colorful and vibrant folder icons.

%prep
%autosetup

%build

%install
install -dm755 %{buildroot}%{_datadir}/icons
cp -r src/breeze-plus-dark %{buildroot}%{_datadir}/icons/
cp -r src/breeze-plus %{buildroot}%{_datadir}/icons/

%files
# List the files and directories owned by this package
%license LICENSE
%{_datadir}/icons/breeze-plus-dark
%{_datadir}/icons/breeze-plus
