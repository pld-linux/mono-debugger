Summary:	Debugger for mono
Summary(pl.UTF-8):	Odpluskiwacz dla mono
Name:		mono-debugger
Version:	2.10
Release:	3
# mono-debugger itself on MIT, but BFD libs enforce GPL
License:	GPL v2+
Group:		Development/Tools
# latest downloads summary at http://ftp.novell.com/pub/mono/sources-stable/
Source0:	http://ftp.novell.com/pub/mono/sources/mono-debugger/%{name}-%{version}.tar.bz2
# Source0-md5:	02ee485f2aae279f2fa3a7051c7d580e
Patch0:		%{name}-termcap.patch
URL:		http://www.mono-project.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.0.0
BuildRequires:	libtool
BuildRequires:	mono-csharp >= 4.0
BuildRequires:	monodoc
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
Requires:	mono >= 4.0
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
Pliki potrzebne programistom korzystającym z bibliotek odpluskwiacza
mono.

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
	MCS=/usr/bin/mcs \
	--disable-static
%{__make} -j1 \
	twodir=%{_prefix}/lib/mono/4.5

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	twodir=%{_prefix}/lib/mono/4.5

# these are used just as DllImport in C# code, so no devel part
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libmonodebugger*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README doc/*.txt
%attr(755,root,root) %{_bindir}/mdb
%attr(755,root,root) %{_bindir}/mdb-symbolreader
%attr(755,root,root) %{_libdir}/libmonodebuggerserver.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmonodebuggerserver.so.0
%attr(755,root,root) %{_libdir}/libmonodebuggerserver.so
%{_prefix}/lib/mono/4.5/mdb-symbolreader.exe
%{_prefix}/lib/mono/4.5/mdb.exe
%{_prefix}/lib/mono/gac/Mono.Debugger
%{_prefix}/lib/mono/gac/Mono.Debugger.SymbolWriter
%{_prefix}/lib/mono/gac/Mono.Debugger.Frontend

%files devel
%defattr(644,root,root,755)
%dir %{_prefix}/lib/mono/%{name}
%{_prefix}/lib/mono/%{name}/Mono.Debugger.dll
%{_prefix}/lib/mono/%{name}/Mono.Debugger.SymbolWriter.dll
%{_prefix}/lib/mono/%{name}/Mono.Debugger.Frontend.dll
%{_pkgconfigdir}/mono-debugger.pc
%{_pkgconfigdir}/mono-debugger-frontend.pc
