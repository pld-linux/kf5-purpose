%define		kdeframever	5.67
%define		qtver		5.9.0
%define		kfname		purpose

Summary:	purpose
Name:		kf5-%{kfname}
Version:	5.67.0
Release:	2
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	4039367834bc9039a84261b5a8d9912c
Patch0:		%{name}-main_js.patch
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
purpose.

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
%patch0 -p0

%build
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%ninja_build

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
%attr(755,root,root) %ghost %{_libdir}/libKF5Purpose.so.5
%attr(755,root,root) %{_libdir}/libKF5Purpose.so.5.*.*
%attr(755,root,root) %ghost %{_libdir}/libKF5PurposeWidgets.so.5
%attr(755,root,root) %{_libdir}/libKF5PurposeWidgets.so.5.*.*
%attr(755,root,root) %ghost %{_libdir}/libPhabricatorHelpers.so.5
%attr(755,root,root) %{_libdir}/libPhabricatorHelpers.so.5.*.*
%attr(755,root,root) %ghost %{_libdir}/libReviewboardHelpers.so.5
%attr(755,root,root) %{_libdir}/libReviewboardHelpers.so.5.*.*
%dir %{_libdir}/qt5/plugins/kf5/kfileitemaction
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kfileitemaction/sharefileitemaction.so
%dir %{_libdir}/qt5/plugins/kf5/purpose
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
%{_libdir}/qt5/qml/org/kde/purpose/plugins.qmltypes
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
%{_datadir}/accounts/services/kde/twitter-microblog.service
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
%dir %{_datadir}/kpackage/Purpose
%dir %{_datadir}/kpackage/Purpose/Twitter
%dir %{_datadir}/kpackage/Purpose/Twitter/contents
%dir %{_datadir}/kpackage/Purpose/Twitter/contents/code
%{_datadir}/kpackage/Purpose/Twitter/contents/code/main.js
%{_datadir}/kpackage/Purpose/Twitter/contents/code/package.json
%dir %{_datadir}/kpackage/Purpose/Twitter/contents/config
%{_datadir}/kpackage/Purpose/Twitter/contents/config/config.qml
%{_datadir}/kpackage/Purpose/Twitter/metadata.json
%dir %{_datadir}/purpose
%{_datadir}/purpose/bluetoothplugin_config.qml
%{_datadir}/purpose/kdeconnectplugin_config.qml
%{_datadir}/purpose/nextcloudplugin_config.qml
%{_datadir}/purpose/phabricatorplugin_config.qml
%{_datadir}/purpose/reviewboardplugin_config.qml
%{_datadir}/purpose/saveasplugin_config.qml
%{_datadir}/purpose/youtubeplugin_config.qml

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/purpose
%{_includedir}/KF5/purposewidgets
%{_libdir}/cmake/KDEExperimentalPurpose
%{_libdir}/cmake/KF5Purpose
%attr(755,root,root) %{_libdir}/libKF5Purpose.so
%attr(755,root,root) %{_libdir}/libKF5PurposeWidgets.so
