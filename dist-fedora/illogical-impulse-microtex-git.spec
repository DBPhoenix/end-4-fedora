%global _pkgname MicroTeX
%global commit 0e3707f

Version:        0.494
Release:        2

Name:           illogical-impulse-microtex-git
Summary:        MicroTeX for illogical-impulse dotfiles.
URL:            https://github.com/NanoMichael/%{_pkgname}
License:        MIT
BuildArch:      x86_64

Source0:        %{url}/archive/%{commit}/%{_pkgname}-%{commit}.tar.gz

BuildRequires:  git-core
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  tinyxml2-devel
BuildRequires:  gtkmm30-devel
BuildRequires:  gtksourceviewmm4-devel
BuildRequires:  cairomm-devel

Requires:       tinyxml2
Requires:       gtkmm30
Requires:       gtksourceviewmm4
Requires:       cairomm

%description
MicroTeX for illogical-impulse dotfiles. A dynamic, cross-platform, and embeddable LaTeX rendering library.

%prep
%setup -q -n %{_pkgname}-%{commit}

sed -i 's/gtksourceviewmm-3.0/gtksourceviewmm-4.0/' CMakeLists.txt

%build
%cmake -DCMAKE_BUILD_TYPE=None
%cmake_build

%install
install -Dm0755 -t %{buildroot}/opt/%{_pkgname}/ build/LaTeX
cp -r build/res %{buildroot}/opt/%{_pkgname}/

%files
%license LICENSE
/opt/%{_pkgname}/LaTeX
/opt/%{_pkgname}/res
