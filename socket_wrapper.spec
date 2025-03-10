Summary:	Socket wrapper library
Summary(pl.UTF-8):	Biblioteka obudowująca dla gniazd
Name:		socket_wrapper
Version:	1.4.4
Release:	1
License:	BSD
Group:		Libraries
Source0:	https://download.samba.org/pub/cwrap/%{name}-%{version}.tar.gz
# Source0-md5:	8c170eb0d285bc8ca954151986d364d8
URL:		https://cwrap.org/socket_wrapper.html
BuildRequires:	cmake >= 3.10.0
# for tests
#BuildRequires:	cmocka >= 1.1.0
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

%package noop
Summary:	Socket wrapper noop library
Summary(pl.UTF-8):	Biblioteka socket wrapper noop
Group:		Libraries

%description noop
Applications with the need to alter their behaviour when socket
wrapper is active, can link to this with -lsocket_wrapper_noop in
order to call get the required public functions at link time.

During runtime these are overloaded with LD_PRELOAD by the real
libsocket_wrapper.so.

%description noop -l pl.UTF-8
Aplikacje potrzebujące zmienić swoje zachowanie, kiedy moduł socket
wrapper jest aktywny mogą włączyć tę bibliotekę jako
-lsocket_wrapper_noop, aby uzyskać potrzebne funkcje publiczne w
czasie budowania.

W czasie działania funkcje te są nadpisywane poprzez LD_PRELOAD
prawdziwej biblioteki libsocket_wrapper.so.

%package noop-devel
Summary:	Header file for socket_wrapper_noop library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki socket_wrapper_noop
Group:		Development/Libraries
Requires:	%{name}-noop = %{version}-%{release}

%description noop-devel
Applications with the need to alter their behaviour when socket
wrapper is active, can link to this with -lsocket_wrapper_noop in
order to call get the required public functions at link time.

During runtime these are overloaded with LD_PRELOAD by the real
libsocket_wrapper.so.

This package contains header file with public functions.

%description noop-devel -l pl.UTF-8
Aplikacje potrzebujące zmienić swoje zachowanie, kiedy moduł socket
wrapper jest aktywny mogą włączyć tę bibliotekę jako
-lsocket_wrapper_noop, aby uzyskać potrzebne funkcje publiczne w
czasie budowania.

W czasie działania funkcje te są nadpisywane poprzez LD_PRELOAD
prawdziwej biblioteki libsocket_wrapper.so.

Ten pakiet zawiera plik nagłówkowy z funkcjami publicznymi.

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

%post	noop -p /sbin/ldconfig
%postun	noop -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG LICENSE README.md TODO
%attr(755,root,root) %{_libdir}/libsocket_wrapper.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsocket_wrapper.so.0
%attr(755,root,root) %{_libdir}/libsocket_wrapper.so
%{_pkgconfigdir}/socket_wrapper.pc
%dir %{_libdir}/cmake/socket_wrapper
%{_libdir}/cmake/socket_wrapper/socket_wrapper-config*.cmake
%{_mandir}/man1/socket_wrapper.1*

%files noop
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsocket_wrapper_noop.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsocket_wrapper_noop.so.0

%files noop-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsocket_wrapper_noop.so
%{_includedir}/socket_wrapper.h
%{_pkgconfigdir}/socket_wrapper_noop.pc
%dir %{_libdir}/cmake/socket_wrapper
%{_libdir}/cmake/socket_wrapper/socket_wrapper_noop-config*.cmake
