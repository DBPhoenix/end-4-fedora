%global _pkgname OneUI4-Icons
%global commit 55eada4
%global __strip /bin/true

Name:           illogical-impulse-oneui4-icons-git
Version:        0.70
Release:        1
Summary:        A fork of mjkim0727/OneUI4-Icons for illogical-impulse dotfiles.

License:        GPL-3.0-only
URL:            https://github.com/end-4/OneUI4-Icons
BuildArch:      noarch

Source0:        %{url}/archive/%{commit}/%{_pkgname}-%{commit}.tar.gz

%description
A fork of the OneUI4-Icons theme, packaged for the illogical-impulse dotfiles setup.

%prep
%setup -q -n %{_pkgname}-%{commit}

%build

%install
install -dm755 %{buildroot}%{_datadir}/icons
cp -dr --no-preserve=mode OneUI %{buildroot}%{_datadir}/icons/
cp -dr --no-preserve=mode OneUI-dark %{buildroot}%{_datadir}/icons/
cp -dr --no-preserve=mode OneUI-light %{buildroot}%{_datadir}/icons/

%files
%license LICENSE
%{_datadir}/icons/OneUI
%{_datadir}/icons/OneUI-dark
%{_datadir}/icons/OneUI-light
