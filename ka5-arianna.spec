#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.01.95
%define		qtver		5.15.2
%define		kf5ver		5.71.0
%define		kaname		arianna
Summary:	An ebook reader
Name:		ka5-%{kaname}
Version:	24.01.95
Release:	0.1
License:	GPL v3
Group:		X11/Applications
Source0:	https://download.kde.org/unstable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	a037f28706b6746ac3548570964d1b4f
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel
BuildRequires:	Qt6Gui-devel >= 5.15.2
BuildRequires:	Qt6HttpServer-devel
BuildRequires:	Qt6Network-devel >= 5.15.10
BuildRequires:	Qt6Positioning-devel >= 5.15
BuildRequires:	Qt6Qml-devel >= 5.15.10
BuildRequires:	Qt6Quick-devel
BuildRequires:	Qt6Sql-devel
BuildRequires:	Qt6Svg-devel
BuildRequires:	Qt6Test-devel
BuildRequires:	Qt6WebChannel-devel
BuildRequires:	Qt6WebSockets-devel
BuildRequires:	Qt6Widgets-devel >= 5.15.2
BuildRequires:	Qt6Xml-devel >= 5.15.2
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	gettext-devel
BuildRequires:	kf6-baloo-devel >= 5.98.0
BuildRequires:	kf6-extra-cmake-modules >= 5.110.0
BuildRequires:	kf6-karchive-devel >= 5.98.0
BuildRequires:	kf6-kconfig-devel >= 5.98.0
BuildRequires:	kf6-kcoreaddons-devel >= 5.110.0
BuildRequires:	kf6-kdbusaddons-devel >= 5.98.0
BuildRequires:	kf6-kfilemetadata-devel >= 5.110.0
BuildRequires:	kf6-ki18n-devel >= 5.98.0
BuildRequires:	kf6-kirigami-devel >= 5.98.0
BuildRequires:	kf6-kquickcharts-devel >= 5.98.0
BuildRequires:	kf6-kwindowsystem-devel >= 5.98.0
BuildRequires:	kf6-qqc2-desktop-style-devel
BuildRequires:	kirigami-addons-devel >= 0.10
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	python3
BuildRequires:	qt6-build >= %{qtver}
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
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DQT_MAJOR_VERSION=6
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
%{_datadir}/qlogging-categories6/arianna.categories
