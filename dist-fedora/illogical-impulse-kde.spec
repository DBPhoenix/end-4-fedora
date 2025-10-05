Name:           illogical-impulse-kde
Version:        1.0
Release:        2
Summary:        Illogical Impulse KDE Dependencies

License:        Proprietary # `Proprietary` is set to satisfy rpmbuild's requirement.
BuildArch:      noarch

Requires:       bluedevil
Requires:       gnome-keyring
Requires:       NetworkManager
Requires:       plasma-nm
Requires:       polkit-kde
Requires:       dolphin
Requires:       systemsettings # TODO: missing from dnf

%description
This is a metapackage that installs the necessary dependencies for Illogical Impulse KDE.

%files
