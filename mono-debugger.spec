Summary:	Debugger for mono
Summary(pl):	Odpluskiwacz dla mono
Name:		mono-debugger
Version:	0.6
Release:	1
License:	GPL
Group:		Development/Libraries
Source0:	http://www.go-mono.com/archive/%{name}-%{version}.tar.gz
# Source0-md5:	5874029644c64bfa957cc538a9e3f906
URL:		http://www.go-mono.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	gtk+2-devel
BuildRequires:	gtk-sharp-devel >= 0.16
BuildRequires:	libgnome-devel
BuildRequires:	libtool
BuildRequires:	mono-csharp
BuildRequires:	mono-devel >= 0.31
BuildRequires:	mono-jay
BuildRequires:	monodoc
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
Requires:	gtk-sharp >= 0.18
Requires:	mono >= 0.31
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Debugger for mono.

%description -l pl
Odpluskiwacz dla mono.

%package devel
Summary:	Development files for mono debugger
Summary(pl):	Pliki potrzebne programistom korzystającym z bibliotek odpluskiwacza mono
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for mono debugger.

%description devel -l pl
Pliki potrzebne programistom korzystającym z bibliotek odpluskiwacza mono.

%package static
Summary:	Static mono debugger libraries
Summary(pl):	Statyczne biblioteki odpluskiwacza mono
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static mono debugger libraries.

%description static -l pl
Statyczne biblioteki odpluskiwacza mono.

%package doc
Summary:	Documentation for mono debugger
Summary(pl):	Dokumentacja odpluskiwacza dla mono
Group:		Documentation
Requires:	monodoc

%description doc
Documentation for mono debugger.

%description doc -l pl
Dokumentacja odpluskiwacza dla mono.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS README ChangeLog TODO AUTHORS doc/*.t* RELEASE-NOTES-*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/mono-debugger-mini-wrapper
%attr(755,root,root) %{_libdir}/*.so.*.*.*
%{_libdir}/*.dll

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files doc
%defattr(644,root,root,755)
%{_libdir}/monodoc/sources/*
