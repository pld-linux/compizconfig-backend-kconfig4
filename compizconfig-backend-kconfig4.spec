Summary:	The kconfig backend for CompizConfig
Summary(pl.UTF-8):	Backend kconfig dla CompizConfiga
Name:		compizconfig-backend-kconfig4
Version:	0.8.4
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://releases.compiz.org/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	89f3cdbdbb8b1bc88f55ccaedbc8404d
URL:		http://www.compiz.org/
BuildRequires:	QtSvg-devel
BuildRequires:	automoc4
BuildRequires:	cmake
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	libcompizconfig-devel >= %{version}
BuildRequires:	pkgconfig
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The kconfig backend for CompizConfig. It uses the KDE4 configuration
system to store the compiz configuration and provides integration into
the KDE4 desktop environment.

%description -l pl.UTF-8
Backend kconfig dla CompizConfiga. Używa systemu konfiguracji KDE4 do
przechowywania konfiguracji compiza i zapewnia integrację ze
środowiskiem KDE4.

%prep
%setup -q

%build
mkdir build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/compizconfig/backends/libkconfig4.so
