#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.08.1
%define		qtver		5.15.2
%define		kf5ver		5.71.0
%define		kaname		arianna
Summary:	An ebook reader
Name:		ka5-%{kaname}
Version:	23.08.1
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	c663f040accdf3ff9c7bf9f68909ab6a
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Gui-devel >= 5.15.2
BuildRequires:	Qt5Network-devel >= 5.15.10
BuildRequires:	Qt5Positioning-devel >= 5.15
BuildRequires:	Qt5Qml-devel >= 5.15.10
BuildRequires:	Qt5Quick-controls2-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	Qt5Sql-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5WebChannel-devel
BuildRequires:	Qt5WebSockets-devel
BuildRequires:	Qt5Widgets-devel >= 5.15.2
BuildRequires:	Qt5Xml-devel >= 5.15.2
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	gettext-devel
BuildRequires:	kf5-baloo-devel >= 5.98.0
BuildRequires:	kf5-extra-cmake-modules >= 5.110.0
BuildRequires:	kf5-karchive-devel >= 5.98.0
BuildRequires:	kf5-kconfig-devel >= 5.98.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.110.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.98.0
BuildRequires:	kf5-kfilemetadata-devel >= 5.110.0
BuildRequires:	kf5-ki18n-devel >= 5.98.0
BuildRequires:	kf5-kirigami2-devel >= 5.98.0
BuildRequires:	kf5-kquickcharts-devel >= 5.98.0
BuildRequires:	kf5-kwindowsystem-devel >= 5.98.0
BuildRequires:	kf5-qqc2-desktop-style-devel
BuildRequires:	kirigami-addons-devel >= 0.10
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	python3
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Arianna is an ebook reader.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/{sr,zh_CN}

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/arianna
%{_desktopdir}/org.kde.arianna.desktop
%{_iconsdir}/hicolor/scalable/apps/org.kde.arianna.svg
%{_datadir}/metainfo/org.kde.arianna.appdata.xml
%{_datadir}/qlogging-categories5/arianna.categories
