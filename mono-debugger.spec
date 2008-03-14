%include	/usr/lib/rpm/macros.mono
Summary:	Debugger for mono
Summary(pl.UTF-8):	Odpluskiwacz dla mono
Name:		mono-debugger
Version:	0.60
Release:	1
License:	GPL
Group:		Development/Tools
#Source0Download: http://go-mono.com/sources-stable/
Source0:	http://go-mono.com/sources/mono-debugger/%{name}-%{version}.tar.bz2
# Source0-md5:	5d13af893299af49ad6abf2d76a35df6
#Source0:	http://primates.ximian.com/~martin/debugger/%{name}-%{version}.tar.gz
Patch0:		%{name}-termcap.patch
URL:		http://www.go-mono.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	libtool
BuildRequires:	mono-csharp >= 1.2.4
BuildRequires:	mono-jay
BuildRequires:	monodoc
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
Requires:	mono >= 1.2.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Debugger for mono.

%description -l pl.UTF-8
Odpluskwiacz dla mono.

%package devel
Summary:	Development files for mono debugger
Summary(pl.UTF-8):	Pliki potrzebne programistom korzystającym z bibliotek odpluskiwacza mono
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for mono debugger.

%description devel -l pl.UTF-8
Pliki potrzebne programistom korzystającym z bibliotek odpluskwiacza mono.

%package static
Summary:	Static mono debugger libraries
Summary(pl.UTF-8):	Statyczne biblioteki odpluskiwacza mono
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static mono debugger libraries.

%description static -l pl.UTF-8
Statyczne biblioteki odpluskwiacza mono.

%package doc
Summary:	Documentation for mono debugger
Summary(pl.UTF-8):	Dokumentacja odpluskiwacza dla mono
Group:		Documentation
Requires:	monodoc

%description doc
Documentation for mono debugger.

%description doc -l pl.UTF-8
Dokumentacja odpluskwiacza dla mono.

%prep
%setup -q
#%patch0 -p1
%patch0 -p1

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

#cp doc/debugger.source $RPM_BUILD_ROOT%{_libdir}/monodoc/sources
#cp doc/debugger.tree $RPM_BUILD_ROOT%{_libdir}/monodoc/sources
#cp doc/debugger.zip $RPM_BUILD_ROOT%{_libdir}/monodoc/sources

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS README ChangeLog TODO AUTHORS doc/*.t* RELEASE-NOTES-*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %{_libdir}/lib*.so
%{_prefix}/lib/mono/1.0/mdb.exe
%{_prefix}/lib/mono/gac/*
%{_prefix}/lib/mono/%{name}

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.la
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

#%files doc
#%defattr(644,root,root,755)
#%{_libdir}/monodoc/sources/*
