#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeframever	5.105
%define		qtver		5.15.2
%define		kfname		purpose

Summary:	Offers available actions for a specific purpose
Name:		kf5-%{kfname}
Version:	5.105.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	65a69e068c958cf647c0a7986c67b365
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-kaccounts-integration-devel
BuildRequires:	kf5-extra-cmake-modules >= %{version}
BuildRequires:	kf5-kconfig-devel >= %{version}
BuildRequires:	kf5-kcoreaddons-devel >= %{version}
BuildRequires:	kf5-ki18n-devel >= %{version}
BuildRequires:	kf5-kio-devel >= %{version}
BuildRequires:	kf5-kirigami2-devel >= %{version}
BuildRequires:	libaccounts-glib-devel
BuildRequires:	libaccounts-qt5-devel
BuildRequires:	libsignon-qt5-devel >= 8.55
BuildRequires:	libutempter-devel
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	kf5-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
This framework offers the possibility to create integrate services and
actions on any application without having to implement them
specifically. Purpose will offer them mechanisms to list the different
alternatives to execute given the requested action type and will
facilitate components so that all the plugins can receive all the
information they need.

%package twitter
Summary:	Twitter plugin for purpose
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description twitter
Twitter plugin for purpose.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kfname}5 --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kfname}5.lang
%defattr(644,root,root,755)
%ghost %{_libdir}/libKF5Purpose.so.5
%attr(755,root,root) %{_libdir}/libKF5Purpose.so.5.*.*
%ghost %{_libdir}/libKF5PurposeWidgets.so.5
%attr(755,root,root) %{_libdir}/libKF5PurposeWidgets.so.5.*.*
%ghost %{_libdir}/libPhabricatorHelpers.so.5
%attr(755,root,root) %{_libdir}/libPhabricatorHelpers.so.5.*.*
%ghost %{_libdir}/libReviewboardHelpers.so.5
%attr(755,root,root) %{_libdir}/libReviewboardHelpers.so.5.*.*
%dir %{_libdir}/qt5/plugins/kf5/kfileitemaction
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kfileitemaction/sharefileitemaction.so
%dir %{_libdir}/qt5/plugins/kf5/purpose
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/purpose/barcodeplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/purpose/bluetoothplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/purpose/emailplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/purpose/imgurplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/purpose/kdeconnectplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/purpose/kdeconnectsmsplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/purpose/ktpsendfileplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/purpose/nextcloudplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/purpose/pastebinplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/purpose/phabricatorplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/purpose/reviewboardplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/purpose/saveasplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/purpose/telegramplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/purpose/youtubeplugin.so
%dir %{_libdir}/qt5/qml/org/kde/purpose
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/purpose/libpurposequickplugin.so
%dir %{_libdir}/qt5/qml/org/kde/purpose/phabricator
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/purpose/phabricator/libphabricatorquickplugin.so
%{_libdir}/qt5/qml/org/kde/purpose/phabricator/qmldir
%{_libdir}/qt5/qml/org/kde/purpose/qmldir
%dir %{_libdir}/qt5/qml/org/kde/purpose/reviewboard
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/purpose/reviewboard/librbpurposequickplugin.so
%{_libdir}/qt5/qml/org/kde/purpose/reviewboard/qmldir
%attr(755,root,root) %{_libexecdir}/kf5/purposeprocess
%dir %{_datadir}/accounts
%dir %{_datadir}/accounts/services
%dir %{_datadir}/accounts/services/kde
%{_datadir}/accounts/services/kde/google-youtube.service
%{_datadir}/accounts/services/kde/nextcloud-upload.service
%{_datadir}/qlogging-categories5/purpose.categories
%{_iconsdir}/hicolor/128x128/apps/phabricator-purpose.png
%{_iconsdir}/hicolor/128x128/apps/reviewboard-purpose.png
%{_iconsdir}/hicolor/16x16/actions/kipiplugin_youtube.png
%{_iconsdir}/hicolor/16x16/apps/phabricator-purpose.png
%{_iconsdir}/hicolor/16x16/apps/reviewboard-purpose.png
%{_iconsdir}/hicolor/22x22/actions/kipiplugin_youtube.png
%{_iconsdir}/hicolor/32x32/actions/kipiplugin_youtube.png
%{_iconsdir}/hicolor/48x48/actions/kipiplugin_youtube.png
%{_iconsdir}/hicolor/64x64/actions/kipiplugin_youtube.png
%{_datadir}/purpose
%{_datadir}/qlogging-categories5/purpose.renamecategories
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/purpose/twitterplugin.so
%{_libdir}/qt5/qml/org/kde/purpose/AlternativesView.qml
%{_libdir}/qt5/qml/org/kde/purpose/JobView.qml

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/purpose
%{_includedir}/KF5/purposewidgets
%{_libdir}/cmake/KDEExperimentalPurpose
%{_libdir}/cmake/KF5Purpose
%{_libdir}/libKF5Purpose.so
%{_libdir}/libKF5PurposeWidgets.so
