Name:           illogical-impulse-python
Version:        1.1
Release:        4
Summary:        Illogical Impulse Python Dependencies

License:        Proprietary # `Proprietary` is set to satisfy rpmbuild's requirement.
BuildArch:      noarch

Requires:       clang
Requires:       uv
Requires:       gtk4
Requires:       libadwaita
Requires:       libsoup3
Requires:       libportal-gtk4
Requires:       gobject-introspection
Requires:       sassc
Requires:       python3-opencv

%description
This is a metapackage that installs the necessary dependencies for Illogical Impulse Python.

%files

%autochangelog
