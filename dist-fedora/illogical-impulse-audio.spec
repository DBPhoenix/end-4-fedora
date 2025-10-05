Name:           illogical-impulse-audio
Version:        1.0
Release:        1
Summary:        Illogical Impulse Audio Dependencies

License:        Proprietary # `Proprietary` is set to satisfy rpmbuild's requirement.
BuildArch:      noarch

Requires:       cava
Requires:       pavucontrol-qt
Requires:       wireplumber
Requires:       libdbusmenu-gtk3
Requires:       playerctl

%description
This is a metapackage that installs the necessary dependencies for Illogical Impulse Audio.

%files

%autochangelog
