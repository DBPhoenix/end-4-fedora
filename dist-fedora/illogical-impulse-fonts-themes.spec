Name:           illogical-impulse-fonts-themes
Version:        1.0
Release:        1
Summary:        Illogical Impulse Fonts and Theming Dependencies

License:        Proprietary # `Proprietary` is set to satisfy rpmbuild's requirement.
BuildArch:      noarch

# Many of these dependencies have different names in Fedora's repositories.
# Some AUR packages may need to be sourced from COPR or packaged manually.

# Themes and Appearance
Requires:       adw-gtk3-theme
Requires:       breeze-icon-theme
# dependencies/breeze-plus
Requires:       breeze-plus
# coprs/deltacopy/darkly
Requires:       darkly
# config-manager addrepo --from-repofile=https://download.opensuse.org/repositories/home:luisbocanegra/Fedora_42/home:luisbocanegra.repo
Requires:       kde-material-you-colors
Requires:       matugen

# Shell and Utilities
Requires:       eza # TODO: missing from dnf
Requires:       fish
Requires:       starship # TODO: missing from dnf
Requires:       kitty
Requires:       fontconfig

# Fonts
Requires:       space-grotesk-fonts # TODO: missing from dnf
Requires:       google-gabarito-fonts # TODO: missing from dnf
# coprs/che/nerd-fonts
Requires:       jetbrains-mono-nerd-fonts # TODO: missing from dnf
Requires:       material-symbols-fonts # TODO: missing from dnf
Requires:       google-readex-pro-fonts # TODO: missing from dnf
Requires:       google-rubik-fonts
Requires:       twitter-twemoji-fonts

%description
This is a metapackage that installs the necessary dependencies for Illogical Impulse Font and Theming.

%files
