Summary:	Socket wrapper library
Summary(pl.UTF-8):	Biblioteka obudowująca dla gniazd
Name:		socket_wrapper
Version:	1.1.5
Release:	1
License:	BSD
Group:		Libraries
Source0:	https://www.samba.org/ftp/cwrap/%{name}-%{version}.tar.gz
# Source0-md5:	e4ac2c61cd87554a0050360fb563c3b2
URL:		https://cwrap.org/socket_wrapper.html
BuildRequires:	cmake >= 2.8.5
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library makes possible to run several instances of the full
software stack on the same machine and perform locally functional
testing of complex network configurations. It passes all socket
communication over unix domain sockets.

%description -l pl.UTF-8
Ta biblioteka umożliwia uruchamianie kilku instancji pełnego stosu
programowego na tej samej maszynie i wykonywanie lokalnie testów
funkcjonalnych złożonych konfiguracji sieciowych. Przekazuje całą
komunikację przez gniazda uniksowe.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README TODO
%attr(755,root,root) %{_libdir}/libsocket_wrapper.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsocket_wrapper.so.0
%attr(755,root,root) %{_libdir}/libsocket_wrapper.so
%{_pkgconfigdir}/socket_wrapper.pc
%{_libdir}/cmake/socket_wrapper
%{_mandir}/man1/socket_wrapper.1*
