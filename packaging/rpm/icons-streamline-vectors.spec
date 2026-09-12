# Version is injected by packaging/rpm/Makefile via `zfr version`.
# RPM Version cannot contain '-'; use `zfr version -r` (hyphens → '_').
# srcversion is the unsanitized Meson/git version and names the tarball.
%{!?version:%global version 0.0.0}
%{!?srcversion:%global srcversion %{version}}

Name:           icons-streamline-vectors
Version:        %{version}
Release:        1%{?dist}
Summary:        Streamline vector icon collections

License:        AGPL-3.0-or-later
URL:            https://www.streamlinehq.com/
Packager:       Lenik (谢继雷) <lenik@bodz.net>
Source0:        %{name}-%{srcversion}.tar.xz

%global debug_package %{nil}
BuildArch:      noarch
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  python3
BuildRequires:  iconlibutils
BuildRequires:  asciidoctor
Requires:       iconlibutils
Requires:       bash-shlib

%description
Streamline vector icon collections
.
Provides icon assets under /usr/share/icons-streamline-vectors, a preview index, and a
launcher `icons-streamline-vectors` (`iconlib -l streamline-vectors`).

%prep
%setup -q -n %{name}-%{srcversion}

%build
meson setup build \
    --prefix=%{_prefix} \
    --bindir=%{_bindir} \
    --datadir=%{_datadir} \
    --mandir=%{_mandir} \
    --sysconfdir=%{_sysconfdir} \
    --localstatedir=%{_localstatedir} \
    --buildtype=plain
meson compile -C build

%install
meson install -C build --destdir=%{buildroot}

%files
%{_bindir}/icons-streamline-vectors
%{_datadir}/bash-completion/completions/streamline-find
%{_datadir}/bash-completion/completions/streamline-index
%{_mandir}/man1/streamline-find.1*
%{_mandir}/man1/streamline-index.1*
%{_datadir}/icons-streamline-vectors/
%{_datadir}/doc/icons-streamline-vectors/

%changelog
* Thu Aug 20 2026 Lenik (谢继雷) <lenik@bodz.net>
- Align spec with debian/control (Meson, AGPL-3.0-or-later).
- Version comes from `zfr version`, the same method meson.build uses.
