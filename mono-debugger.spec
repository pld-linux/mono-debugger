%define _snap 20030914
Summary:	Debugger for mono
Summary(pl):	Odpluskiwacz dla mono
Name:		mono-debugger
Version:	0.4.99
Release:	0.%{_snap}.1
License:	GPL
Group:		Development/Libraries
Source0:	%{name}-cvs-%{_snap}.tar.bz2
# Source0-md5:	f650a9f04f49dea600cd917cc14dda09
URL:		http://www.go-mono.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	gtk+2-devel
BuildRequires:	gtk-sharp-devel >= 0.10
BuildRequires:	libgnome-devel
BuildRequires:	libtool
BuildRequires:	mono-csharp
BuildRequires:	mono-devel >= 0.26-3.1
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Debugger for mono.

%description -l pl
Odpluskiwacz dla mono.

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

%files
%defattr(644,root,root,755)
%doc NEWS README ChangeLog TODO AUTHORS doc/*.t* RELEASE-NOTES-*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/mono-debugger-mini-wrapper
%attr(755,root,root) %{_libdir}/*.so*
%{_libdir}/*.dll
