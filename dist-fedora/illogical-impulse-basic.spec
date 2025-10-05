Name:           illogical-impulse-basic
Version:        1.0
Release:        1
Summary:        Illogical Impulse Basic Dependencies

License:        Proprietary # `Proprietary` is set to satisfy rpmbuild's requirement.
BuildArch:      noarch

Requires:       axel
Requires:       bc
Requires:       coreutils
Requires:       cliphist
Requires:       cmake
Requires:       curl
Requires:       rsync
Requires:       wget
Requires:       ripgrep
Requires:       jq
Requires:       meson
Requires:       xdg-user-dirs

%description
This is a metapackage that installs the necessary dependencies for Illogical Impulse Basic.

%files

%autochangelog
