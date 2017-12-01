#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gcab
Version  : 0.7
Release  : 8
URL      : https://download.gnome.org/sources/gcab/0.7/gcab-0.7.tar.xz
Source0  : https://download.gnome.org/sources/gcab/0.7/gcab-0.7.tar.xz
Summary  : Cabinet file library
Group    : Development/Tools
License  : LGPL-2.1
Requires: gcab-bin
Requires: gcab-data
Requires: gcab-lib
Requires: gcab-doc
Requires: gcab-locales
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : intltool
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(zlib)

%description
No detailed description available

%package bin
Summary: bin components for the gcab package.
Group: Binaries
Requires: gcab-data

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
Requires: gcab-lib
Requires: gcab-bin
Requires: gcab-data
Provides: gcab-devel

%description dev
dev components for the gcab package.


%package doc
Summary: doc components for the gcab package.
Group: Documentation

%description doc
doc components for the gcab package.


%package lib
Summary: lib components for the gcab package.
Group: Libraries
Requires: gcab-data

%description lib
lib components for the gcab package.


%package locales
Summary: locales components for the gcab package.
Group: Default

%description locales
locales components for the gcab package.


%prep
%setup -q -n gcab-0.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1512144748
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1512144748
rm -rf %{buildroot}
%make_install
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
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
/usr/share/gtk-doc/html/gcab/GCabCabinet.html
/usr/share/gtk-doc/html/gcab/GCabFile.html
/usr/share/gtk-doc/html/gcab/GCabFolder.html
/usr/share/gtk-doc/html/gcab/annotation-glossary.html
/usr/share/gtk-doc/html/gcab/api-index-full.html
/usr/share/gtk-doc/html/gcab/ch01.html
/usr/share/gtk-doc/html/gcab/deprecated-api-index.html
/usr/share/gtk-doc/html/gcab/gcab.devhelp2
/usr/share/gtk-doc/html/gcab/home.png
/usr/share/gtk-doc/html/gcab/index.html
/usr/share/gtk-doc/html/gcab/index.sgml
/usr/share/gtk-doc/html/gcab/left-insensitive.png
/usr/share/gtk-doc/html/gcab/left.png
/usr/share/gtk-doc/html/gcab/object-tree.html
/usr/share/gtk-doc/html/gcab/right-insensitive.png
/usr/share/gtk-doc/html/gcab/right.png
/usr/share/gtk-doc/html/gcab/style.css
/usr/share/gtk-doc/html/gcab/up-insensitive.png
/usr/share/gtk-doc/html/gcab/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgcab-1.0.so.0
/usr/lib64/libgcab-1.0.so.0.0.0

%files locales -f gcab.lang
%defattr(-,root,root,-)

