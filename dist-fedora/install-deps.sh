# This script is meant to be sourced.
# It's not for directly running.

add_external_repos(){
  echo -e "${STY_YELLOW}[$0]: This script needs to add third-party COPR and other repositories to install all dependencies.${STY_RESET}"
  echo "The following will be added:"
  echo "  - COPR: che/nerd-fonts"
  echo "  - COPR: deltacopy/darkly"
  echo "  - COPR: solopasha/hyprland"
  echo "  - COPR: errornointernet/quickshell"
  echo "  - Repo: home:luisbocanegra (for wlogout)"
  echo ""
  read -p "Do you want to proceed? [Y/n] " p
  if [[ "$p" =~ ^[Nn]$ ]]; then
    echo "Aborting."
    # Use 'return' instead of 'exit' so it doesn't close the parent shell
    return 1
  fi

  coprs_to_add=(
    "che/nerd-fonts"
    "deltacopy/darkly"
    "solopasha/hyprland"
    "errornointernet/quickshell"
  )

  for copr in "${coprs_to_add[@]}"; do
    x sudo dnf copr enable -y "$copr"
  done

  x sudo dnf config-manager addrepo --from-repofile=https://download.opensuse.org/repositories/home:luisbocanegra/Fedora_42/home:luisbocanegra.repo
}

#####################################################################################
if ! command -v dnf >/dev/null 2>&1; then
  printf "${STY_RED}[$0]: dnf not found, it seems that the system is not Fedora or a Fedora-based distro. Aborting...${STY_RESET}\n"
  # Use 'return' as the script is sourced
  return 1
fi

# Issue #363
case $SKIP_SYSUPDATE in
  true) sleep 0;;
  *) v sudo dnf upgrade -y;;
esac

# Add required third-party repositories.
showfun add_external_repos
v add_external_repos || return 1 # Stop if the user chose not to add repos

# In the RPM world, it's best to build packages first, then install them.
# This function builds a single spec file and installs the resulting RPM.
# This is necessary for local dependencies that are required by other local packages.
install-local-spec() {
  local location=$1

  # Download required sources
  x spectool -g -R "$location"
  # Install build dependencies for the spec file
  x sudo dnf builddep -y "$location"
  # Build the binary RPM
  x rpmbuild -bb "$location"

  # Find the RPM we just built. We query the spec file to get the exact name.
  local rpm_name=$(basename "$location" .spec)
  local rpm_file=$(find "$HOME/rpmbuild/RPMS" -name "${rpm_name}-*.rpm" | head -n 1)

  # Install the built package
  x sudo dnf install -y "$rpm_file"
}

# RPM build dependencies for RPM specifications
v sudo dnf install -y rpm-build rpmdevtools

# Install core dependencies from the meta-packages
metapkgs=(./dist-fedora/dependencies/breeze-plus.spec)
metapkgs+=(./dist-fedora/illogical-impulse-{audio,backlight,basic,fonts-themes,kde,portal,python,screencapture,toolkit,widgets}.spec)
metapkgs+=(./dist-fedora/illogical-impulse-hyprland.spec)
metapkgs+=(./dist-fedora/illogical-impulse-microtex-git.spec)
# metapkgs+=(./dist-fedora/illogical-impulse-oneui4-icons-git.spec)
[[ -f /usr/share/icons/Bibata-Modern-Classic/index.theme ]] || \
  metapkgs+=(./dist-fedora/illogical-impulse-bibata-modern-classic-bin.spec)

for i in "${metapkgs[@]}"; do
  $ask && showfun install-local-spec
  v install-local-spec "$i"
done

## Optional dependencies
if dnf list installed plasma-browser-integration &>/dev/null; then SKIP_PLASMAINTG=true; fi
case $SKIP_PLASMAINTG in
  true) sleep 0;;
  *)
    if $ask;then
      echo -e "${STY_YELLOW}[$0]: NOTE: The package \"plasma-browser-integration\" is about 600 MiB.${STY_RESET}"
      echo -e "${STY_YELLOW}It is needed if you want playtime of media in Firefox to be shown on the music controls widget.${STY_RESET}"
      echo -e "${STY_YELLOW}Install it? [y/N]${STY_RESET}"
      read -p "====> " p
    else
      p=y
    fi
    case $p in
      y) x sudo dnf install -y plasma-browser-integration ;;
      *) echo "Ok, won't install"
    esac
    ;;
esac
