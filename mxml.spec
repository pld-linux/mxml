# TODO:
# - make it shared
#
Summary:	Small XML parsing library
Summary(pl):	Ma³a biblioteka parsuj±ca XML
Name:		mxml
Version:	2.0
Release:	1
License:	GPL v.2
Group:		Libraries
Source0:	http://www.easysw.com/~mike/mxml/swfiles/%{name}-%{version}.tar.gz
# Source0-md5:	bd9194cdbf717550a130789802e5b81c
URL:		http://www.easysw.com/~mike/mxml/software.php
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mini-XML is a small XML parsing library.

%description -l pl
Mini-XML jest ma³± bibliotek± parsuj±c± XML.

%package devel
Summary:	Header files for mxml
Summary(pl):	Pliki nag³ówkowe dla mxml
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for mxml.

%description devel -l pl
Pliki nag³ówkowe dla mxml.

%package static
Summary:	Static mxml library
Summary(pl):	Statyczna biblioteka mxml
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static mxml library.

%description static -l pl
Statyczna biblioteka mxml.

%prep
%setup -q
%{__perl} -pi -e 's/OPTIM="-O"/OPTIM=$OPTFLAGS/' configure.in

%build
%{__autoconf}
%configure 
%{__make} \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	BUILDROOT=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT/%{_docdir}/mxml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO
%attr(755,root,root) %{_libdir}/lib*.a
%{_mandir}/man3/*

%files devel
%defattr(644,root,root,755)
%doc doc/*.html
%attr(755,root,root) %{_bindir}/*
%{_pkgconfigdir}/*.pc
%{_includedir}/*.h
%{_mandir}/man1/*


#%%files static
#%%defattr(644,root,root,755)
#%%{_libdir}/*.a
