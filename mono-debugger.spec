%define _snap 20030226
Summary:	Debugger for mono
Summary(pl):	Odpluskiwacz dla mono
Name:		mono-debugger
Version:	0.2.1
Release:	0.%{_snap}.0
License:	GPL
Group:		Development/Libraries
Source0:	%{name}-cvs-%{_snap}.tar.bz2
# Source0-md5:	dc78ca8cb5ac123538a704e7d1911993
Patch0:		%{name}-recent-gtk-sharp.patch
URL:		http://www.go-mono.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	gtk+2-devel
BuildRequires:	gtk-sharp-devel >= 0.8
BuildRequires:	libgnome-devel
BuildRequires:	libtool
BuildRequires:	mono-csharp
BuildRequires:	mono-devel >= 0.20-2
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Debugger for mono.

%description -l pl
Odpluskiwacz dla mono.

%prep
%setup -q -n debugger
%patch0 -p0

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

# make .so symlinks, they are dynamically loaded
for f in $RPM_BUILD_ROOT%{_libdir}/*.so.* ; do
	b=$(basename $f)
	ln -s $b $RPM_BUILD_ROOT%{_libdir}$(echo $b | sed -e 's/\.so.*/.so/')
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README ChangeLog TODO AUTHORS doc/*.t*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/mono-debugger-jit-wrapper
%attr(755,root,root) %{_libdir}/*.so*
%{_libdir}/*.dll
