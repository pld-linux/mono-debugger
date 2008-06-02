%include	/usr/lib/rpm/macros.mono
Summary:	Debugger for mono
Summary(pl.UTF-8):	Odpluskiwacz dla mono
Name:		mono-debugger
Version:	0.60
Release:	1
# mono-debugger itself on MIT, but BFD libs enforce GPL
License:	GPL v2+
Group:		Development/Tools
#Source0Download: http://go-mono.com/sources-stable/
Source0:	http://go-mono.com/sources/mono-debugger/%{name}-%{version}.tar.bz2
# Source0-md5:	5d13af893299af49ad6abf2d76a35df6
Patch0:		%{name}-termcap.patch
URL:		http://www.go-mono.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	libtool
BuildRequires:	mono-csharp >= 1.2.5
BuildRequires:	mono-jay
BuildRequires:	monodoc
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
Requires:	mono >= 1.2.5
ExclusiveArch:	%{ix86} %{x8664}
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
Obsoletes:	mono-debugger-static

%description devel
Development files for mono debugger.

%description devel -l pl.UTF-8
Pliki potrzebne programistom korzystającym z bibliotek odpluskwiacza mono.

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
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#cp doc/debugger.source $RPM_BUILD_ROOT%{_libdir}/monodoc/sources
#cp doc/debugger.tree $RPM_BUILD_ROOT%{_libdir}/monodoc/sources
#cp doc/debugger.zip $RPM_BUILD_ROOT%{_libdir}/monodoc/sources

# these are used just as DllImport in C# code, so no devel part
rm $RPM_BUILD_ROOT%{_libdir}/libmonodebugger*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README RELEASE-NOTES-* TODO doc/*.txt
%attr(755,root,root) %{_bindir}/mdb
%attr(755,root,root) %{_libdir}/libmonodebuggerreadline.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmonodebuggerreadline.so.0
%attr(755,root,root) %{_libdir}/libmonodebuggerreadline.so
%attr(755,root,root) %{_libdir}/libmonodebuggerserver.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmonodebuggerserver.so.0
%attr(755,root,root) %{_libdir}/libmonodebuggerserver.so
%{_prefix}/lib/mono/1.0/mdb.exe
%{_prefix}/lib/mono/gac/Mono.Debugger
%{_prefix}/lib/mono/gac/Mono.Debugger.Backend
%{_prefix}/lib/mono/gac/Mono.Debugger.Cecil

%files devel
%defattr(644,root,root,755)
%dir %{_prefix}/lib/mono/%{name}
%{_prefix}/lib/mono/%{name}/Mono.Debugger.dll
%{_prefix}/lib/mono/%{name}/Mono.Debugger.Backend.dll
%{_prefix}/lib/mono/%{name}/Mono.Debugger.Cecil.dll
%{_pkgconfigdir}/mono-debugger.pc

#%files doc
#%defattr(644,root,root,755)
#%{_libdir}/monodoc/sources/*
