# TODO:
# - make it shared
#
Summary:	Small XML parsing library
Summary(pl.UTF-8):	Mała biblioteka parsująca XML
Name:		mxml
Version:	2.2
Release:	2
License:	GPL v.2
Group:		Libraries
Source0:	http://ftp.easysw.com/pub/mxml/2.2/%{name}-%{version}.tar.gz
# Source0-md5:	2c28aedee8a06eac173104a3fccce096
URL:		http://www.easysw.com/~mike/mxml/software.php
BuildRequires:	autoconf
Conflicts:	libmxml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mini-XML is a small XML parsing library.

%description -l pl.UTF-8
Mini-XML jest małą biblioteką parsującą XML.

%package devel
Summary:	Header files for mxml
Summary(pl.UTF-8):	Pliki nagłówkowe dla mxml
Group:		Development/Libraries
Conflicts:	libmxml-devel
Requires:	%{name} = %{version}-%{release}

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

rm -rf $RPM_BUILD_ROOT%{_docdir}/mxml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_libdir}/lib*.a
%{_mandir}/man3/*

#%files devel
#%defattr(644,root,root,755)
%doc doc/*.html
%attr(755,root,root) %{_bindir}/*
%{_pkgconfigdir}/*.pc
%{_includedir}/*.h
%{_mandir}/man1/*

#%%files static
#%%defattr(644,root,root,755)
#%%{_libdir}/*.a
