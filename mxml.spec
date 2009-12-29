Summary:	Mini-XML: Lightweight XML Library
Summary(pl.UTF-8):	Mała biblioteka parsująca XML
Name:		mxml
Version:	2.6
Release:	2
License:	GPL v2
Group:		Libraries
Source0:	http://ftp.easysw.com/pub/mxml/2.6/%{name}-%{version}.tar.gz
# Source0-md5:	68977789ae64985dddbd1a1a1652642e
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
Mini-XML jest małą biblioteką parsującą XML.

%package devel
Summary:	Header files for mxml
Summary(pl.UTF-8):	Pliki nagłówkowe dla mxml
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Conflicts:	libmxml-devel

%description devel
Header files for mxml.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla mxml.

%package static
Summary:	Static mxml library
Summary(pl.UTF-8):	Statyczna biblioteka mxml
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static mxml library.

%description static -l pl.UTF-8
Statyczna biblioteka mxml.

%prep
%setup -q
%{__sed} -i -e 's/OPTIM="-O"/OPTIM=$OPTFLAGS/' configure.in

%build
%{__autoconf}
%configure \
	--enable-shared
%{__make} \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	BUILDROOT=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_docdir}/mxml
rm -f $RPM_BUILD_ROOT%{_mandir}/cat1/mxmldoc.1*
rm -f $RPM_BUILD_ROOT%{_mandir}/cat3/mxml.3*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_libdir}/libmxml.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libmxml.so.1
%attr(755,root,root) %{_bindir}/mxmldoc*
%{_mandir}/man1/mxmldoc.1*

%files devel
%defattr(644,root,root,755)
%doc doc/*.html
%{_libdir}/libmxml.so
%{_pkgconfigdir}/*.pc
%{_includedir}/*.h
%{_mandir}/man3/mxml.3*

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.a
