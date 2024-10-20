#
# Conditional build:
%bcond_with	tests		# test suite
%bcond_without	qtwebengine	# QtWebEngine support

%ifarch x32
%undefine	with_qtwebengine
%endif

%define		kdeappsver	23.08.5
%define		qt_ver		5.15.10
%define		kf_ver		5.98.0
%define		kaname		arianna
Summary:	An ebook reader
Summary(pl.UTF-8):	Czytnik e-booków
Name:		ka5-%{kaname}
Version:	23.08.5
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	a658239afbb982d5a78a0e6766ad2921
URL:		https://apps.kde.org/arianna/
BuildRequires:	Qt5Core-devel >= %{qt_ver}
BuildRequires:	Qt5Gui-devel >= %{qt_ver}
BuildRequires:	Qt5Network-devel >= %{qt_ver}
BuildRequires:	Qt5Qml-devel >= %{qt_ver}
BuildRequires:	Qt5Quick-controls2-devel >= %{qt_ver}
BuildRequires:	Qt5Quick-devel >= %{qt_ver}
BuildRequires:	Qt5Sql-devel >= %{qt_ver}
BuildRequires:	Qt5Svg-devel >= %{qt_ver}
BuildRequires:	Qt5Test-devel >= %{qt_ver}
BuildRequires:	Qt5WebChannel-devel >= %{qt_ver}
%if %{with qtwebengine}
BuildRequires:	Qt5WebEngine-devel >= %{qt_ver}
%endif
BuildRequires:	Qt5WebSockets-devel >= %{qt_ver}
BuildRequires:	Qt5Widgets-devel >= %{qt_ver}
BuildRequires:	Qt5Xml-devel >= %{qt_ver}
BuildRequires:	cmake >= 3.16
BuildRequires:	gettext-tools
BuildRequires:	kf5-baloo-devel >= %{kf_ver}
BuildRequires:	kf5-extra-cmake-modules >= %{kf_ver}
BuildRequires:	kf5-karchive-devel >= %{kf_ver}
BuildRequires:	kf5-kconfig-devel >= %{kf_ver}
BuildRequires:	kf5-kcoreaddons-devel >= %{kf_ver}
BuildRequires:	kf5-kdbusaddons-devel >= %{kf_ver}
BuildRequires:	kf5-kfilemetadata-devel >= %{kf_ver}
BuildRequires:	kf5-ki18n-devel >= %{kf_ver}
BuildRequires:	kf5-kirigami2-devel >= %{kf_ver}
BuildRequires:	kf5-kirigami-addons-devel >= 0.10
BuildRequires:	kf5-kquickcharts-devel >= %{kf_ver}
BuildRequires:	kf5-kwindowsystem-devel >= %{kf_ver}
BuildRequires:	kf5-qqc2-desktop-style-devel
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	python3
BuildRequires:	qt5-build >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	Qt5Core >= %{qt_ver}
Requires:	Qt5Gui >= %{qt_ver}
Requires:	Qt5Network >= %{qt_ver}
Requires:	Qt5Qml >= %{qt_ver}
Requires:	Qt5Quick-controls2 >= %{qt_ver}
Requires:	Qt5Quick >= %{qt_ver}
Requires:	Qt5Sql >= %{qt_ver}
Requires:	Qt5Svg >= %{qt_ver}
Requires:	Qt5WebChannel >= %{qt_ver}
%if %{with qtwebengine}
Requires:	Qt5WebEngine >= %{qt_ver}
%endif
Requires:	Qt5WebSockets >= %{qt_ver}
Requires:	Qt5Widgets >= %{qt_ver}
Requires:	Qt5Xml >= %{qt_ver}
Requires:	kf5-baloo >= %{kf_ver}
Requires:	kf5-karchive >= %{kf_ver}
Requires:	kf5-kconfig >= %{kf_ver}
Requires:	kf5-kcoreaddons >= %{kf_ver}
Requires:	kf5-kdbusaddons >= %{kf_ver}
Requires:	kf5-kfilemetadata >= %{kf_ver}
Requires:	kf5-ki18n >= %{kf_ver}
Requires:	kf5-kirigami2 >= %{kf_ver}
Requires:	kf5-kirigami-addons >= 0.10
Requires:	kf5-kquickcharts >= %{kf_ver}
Requires:	kf5-kwindowsystem >= %{kf_ver}
Requires:	kf5-qqc2-desktop-style
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Arianna is an ebook reader.

%description -l pl.UTF-8
Arianna to czytnik e-booków.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_SYSCONFDIR=%{_sysconfdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{kaname}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/arianna
%{_desktopdir}/org.kde.arianna.desktop
%{_iconsdir}/hicolor/scalable/apps/org.kde.arianna.svg
%{_datadir}/metainfo/org.kde.arianna.appdata.xml
%{_datadir}/qlogging-categories5/arianna.categories
