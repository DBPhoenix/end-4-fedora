%global _variant Bibata-Modern-Classic
%global __strip /bin/true

Name:           illogical-impulse-bibata-modern-classic-bin
Version:        2.0.6
Release:        1
Summary:        Material Based Cursor Theme, installed for illogical-impulse dotfiles

License:        GPL-3.0-or-later
URL:            https://github.com/ful1e5/Bibata_Cursor
BuildArch:      noarch

Source0:        %{url}/releases/download/v%{version}/%{_variant}.tar.xz

Conflicts:      bibata-cursor-theme
Conflicts:      bibata-cursor-theme-bin

%description
This package provides the Bibata-Modern-Classic variant for the illogical-impulse dotfiles setup.

%prep
%autosetup

%build
# No build steps are necessary for this package.

%install
install -dm755 %{buildroot}%{_datadir}/icons
cp -dr --no-preserve=mode ./%{_variant} %{buildroot}%{_datadir}/icons/

%files
%license LICENSE
%{_datadir}/icons/%{_variant}
