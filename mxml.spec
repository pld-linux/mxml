Summary:	Mini-XML: Lightweight XML support library
Summary(pl.UTF-8):	Mini-XML - lekka biblioteka obsługująca XML
Name:		mxml
Version:	2.10
Release:	1
License:	LGPL v2 with exceptions
Group:		Libraries
Source0:	http://www.msweet.org/files/project3/%{name}-%{version}.tar.gz
# Source0-md5:	8804c961a24500a95690ef287d150abe
Patch0:		%{name}-lpthread.patch
URL:		http://www.minixml.org/
BuildRequires:	autoconf
BuildRequires:	sed >= 4.0
# Conflicts due SONAME
Conflicts:	libmxml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mini-XML is a small XML library that you can use to read and write XML
and XML-like data files in your application without requiring large
non-standard libraries.

Mini-XML supports reading of UTF-8 and UTF-16 and writing of UTF-8
encoded XML files and strings. Data is stored in a linked-list tree
structure, preserving the XML data hierarchy, and arbitrary element
names, attributes, and attribute values are supported with no preset
limits, just available memory.

%description -l pl.UTF-8
Mini-XML to mała biblioteka XML, której można używać do odczytu i
zapisu plików w formacie XML i zbliżonym do XML w aplikacjach nie
wymagających dużych, niestandardowych bibliotek.

Mini-XML obsługuje odczyt plików i łańcuchów XML zakodowanych w UTF-8
i UTF-16 oraz zapisu w UTF-8. Dane są przechowywane w listowej
strukturze drzewiastej, z zachowaniem hierarchii danych XML;
obsługiwane są dowolne nazwy, atrybuty i wartości atrybutów elementów
bez narzuconych limitów poza dostępną pamięcią.

%package devel
Summary:	Header files for mxml library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki mxml
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Conflicts:	libmxml-devel

%description devel
Header files for mxml library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki mxml.

%package static
Summary:	Static mxml library
Summary(pl.UTF-8):	Statyczna biblioteka mxml
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Conflicts:	libmxml-static

%description static
Static mxml library.

%description static -l pl.UTF-8
Statyczna biblioteka mxml.

%prep
%setup -q
%patch -P0 -p1

%{__sed} -i -e '/^\.SILENT/d' Makefile.in

%build
%{__autoconf}
%configure \
	--enable-shared
%{__make} \
	OPTIM="%{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	BUILDROOT=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/mxml

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
# COPYING contains exceptions to LGPL
%doc CHANGES COPYING README
%attr(755,root,root) %{_bindir}/mxmldoc
%attr(755,root,root) %{_libdir}/libmxml.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libmxml.so.1
%{_mandir}/man1/mxmldoc.1*

%files devel
%defattr(644,root,root,755)
%doc doc/*.html
%attr(755,root,root) %{_libdir}/libmxml.so
%{_pkgconfigdir}/mxml.pc
%{_includedir}/mxml.h
%{_mandir}/man3/mxml.3*

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmxml.a
