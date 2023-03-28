#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
Name     : gcab
Version  : 1.5
Release  : 23
URL      : https://download.gnome.org/sources/gcab/1.5/gcab-1.5.tar.xz
Source0  : https://download.gnome.org/sources/gcab/1.5/gcab-1.5.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: gcab-bin = %{version}-%{release}
Requires: gcab-data = %{version}-%{release}
Requires: gcab-lib = %{version}-%{release}
Requires: gcab-license = %{version}-%{release}
Requires: gcab-locales = %{version}-%{release}
Requires: gcab-man = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : docbook-xml
BuildRequires : gtk-doc
BuildRequires : vala
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: backport-meson-git-version-is-optional.patch

%description
GCab
====
A GObject library to create cabinet files
Fuzzing
-------
CC=afl-gcc meson --default-library=static ../
AFL_HARDEN=1 ninja
afl-fuzz -m 300 -i ../tests/fuzzing/ -o findings ./src/gcab-fuzz @@

%package bin
Summary: bin components for the gcab package.
Group: Binaries
Requires: gcab-data = %{version}-%{release}
Requires: gcab-license = %{version}-%{release}

%description bin
bin components for the gcab package.


%package data
Summary: data components for the gcab package.
Group: Data

%description data
data components for the gcab package.


%package dev
Summary: dev components for the gcab package.
Group: Development
Requires: gcab-lib = %{version}-%{release}
Requires: gcab-bin = %{version}-%{release}
Requires: gcab-data = %{version}-%{release}
Provides: gcab-devel = %{version}-%{release}
Requires: gcab = %{version}-%{release}

%description dev
dev components for the gcab package.


%package doc
Summary: doc components for the gcab package.
Group: Documentation
Requires: gcab-man = %{version}-%{release}

%description doc
doc components for the gcab package.


%package lib
Summary: lib components for the gcab package.
Group: Libraries
Requires: gcab-data = %{version}-%{release}
Requires: gcab-license = %{version}-%{release}

%description lib
lib components for the gcab package.


%package license
Summary: license components for the gcab package.
Group: Default

%description license
license components for the gcab package.


%package locales
Summary: locales components for the gcab package.
Group: Default

%description locales
locales components for the gcab package.


%package man
Summary: man components for the gcab package.
Group: Default

%description man
man components for the gcab package.


%prep
%setup -q -n gcab-1.5
cd %{_builddir}/gcab-1.5
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1680022826
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gcab
cp %{_builddir}/gcab-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gcab/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gcab

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gcab

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/GCab-1.0.typelib
/usr/share/gir-1.0/*.gir
/usr/share/vala/vapi/libgcab-1.0.deps
/usr/share/vala/vapi/libgcab-1.0.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/libgcab-1.0/libgcab.h
/usr/include/libgcab-1.0/libgcab/gcab-cabinet.h
/usr/include/libgcab-1.0/libgcab/gcab-enums.h
/usr/include/libgcab-1.0/libgcab/gcab-file.h
/usr/include/libgcab-1.0/libgcab/gcab-folder.h
/usr/lib64/libgcab-1.0.so
/usr/lib64/pkgconfig/libgcab-1.0.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/gcab/annotation-glossary.html
/usr/share/gtk-doc/html/gcab/api-index-0-5.html
/usr/share/gtk-doc/html/gcab/api-index-0-6.html
/usr/share/gtk-doc/html/gcab/api-index-1-0.html
/usr/share/gtk-doc/html/gcab/api-index-1-4.html
/usr/share/gtk-doc/html/gcab/api-index-deprecated.html
/usr/share/gtk-doc/html/gcab/api-index-full.html
/usr/share/gtk-doc/html/gcab/ch01.html
/usr/share/gtk-doc/html/gcab/gcab-GCabCabinet.html
/usr/share/gtk-doc/html/gcab/gcab-GCabFile.html
/usr/share/gtk-doc/html/gcab/gcab-GCabFolder.html
/usr/share/gtk-doc/html/gcab/gcab.devhelp2
/usr/share/gtk-doc/html/gcab/home.png
/usr/share/gtk-doc/html/gcab/index.html
/usr/share/gtk-doc/html/gcab/left-insensitive.png
/usr/share/gtk-doc/html/gcab/left.png
/usr/share/gtk-doc/html/gcab/right-insensitive.png
/usr/share/gtk-doc/html/gcab/right.png
/usr/share/gtk-doc/html/gcab/style.css
/usr/share/gtk-doc/html/gcab/up-insensitive.png
/usr/share/gtk-doc/html/gcab/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgcab-1.0.so.0
/usr/lib64/libgcab-1.0.so.0.2.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gcab/01a6b4bf79aca9b556822601186afab86e8c4fbf

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gcab.1

%files locales -f gcab.lang
%defattr(-,root,root,-)

