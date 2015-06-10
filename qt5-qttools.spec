#
# Conditional build:
%bcond_with	bootstrap	# disable features to able to build without installed qt5
# -- build targets
%bcond_without	qch		# QCH documentation
%bcond_without	qm		# QM translations
%bcond_without	qtdeclarative	# Quick2 plugin for Qt5Declarative
%bcond_without	qtwebkit	# WebKit plugin for Qt5Declarative

%if %{with bootstrap}
%undefine	with_qch
%undefine	with_qm
%endif

%define		orgname		qttools
%define		qtbase_ver		%{version}
%define		qttools_ver		5.2
%define		qtdeclarative_ver	5.4
%define		qtwebkit_ver		5.4
Summary:	Development tools for Qt 5
Summary(pl.UTF-8):	Narzędzia programistyczne dla Qt 5
Name:		qt5-%{orgname}
Version:	5.4.1
Release:	1
License:	LGPL v2.1 with Digia Qt LGPL Exception v1.1 or GPL v3.0
Group:		X11/Libraries
Source0:	http://download.qt-project.org/official_releases/qt/5.4/%{version}/submodules/%{orgname}-opensource-src-%{version}.tar.xz
# Source0-md5:	5b2fd42304e9294bc0f77095fdb35ad6
Source1:	http://download.qt-project.org/official_releases/qt/5.4/%{version}/submodules/qttranslations-opensource-src-%{version}.tar.xz
# Source1-md5:	0bdd1b0a83b03a04a4ebeedfa3057d21
URL:		http://qt-project.org/
BuildRequires:	OpenGL-devel
BuildRequires:	Qt5Core-devel >= %{qtbase_ver}
BuildRequires:	Qt5DBus-devel >= %{qtbase_ver}
BuildRequires:	Qt5Gui-devel >= %{qtbase_ver}
BuildRequires:	Qt5Network-devel >= %{qtbase_ver}
BuildRequires:	Qt5PrintSupport-devel >= %{qtbase_ver}
%{?with_qtdeclarative:BuildRequires:	Qt5Quick-devel >= %{qtdeclarative_ver}}
BuildRequires:	Qt5Sql-devel >= %{qtbase_ver}
%{?with_qtwebkit:BuildRequires:	Qt5WebKit-devel >= %{qtwebkit_ver}}
BuildRequires:	Qt5Widgets-devel >= %{qtbase_ver}
BuildRequires:	Qt5Xml-devel >= %{qtbase_ver}
%{?with_qch:BuildRequires:	qt5-assistant >= %{qttools_ver}}
BuildRequires:	qt5-build >= %{qtbase_ver}
BuildRequires:	qt5-doc-common >= %{qtbase_ver}
%{?with_qm:BuildRequires:	qt5-linguist >= %{qttools_ver}}
BuildRequires:	qt5-qmake >= %{qtbase_ver}
BuildRequires:	rpmbuild(macros) >= 1.654
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
# pixeltool: Core, Gui, Widgets
# qtpaths: Core
Requires:	Qt5Core >= %{qtbase_ver}
Requires:	Qt5Gui >= %{qtbase_ver}
Requires:	Qt5Widgets >= %{qtbase_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing
%define		qt5dir		%{_libdir}/qt5

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.

This package contains additional tools for building Qt applications.

%description -l pl.UTF-8
Qt to wieloplatformowy szkielet aplikacji i interfejsów użytkownika.
Przy użyciu Qt można pisać aplikacje powiązane z WWW i wdrażać je w
systemach biurkowych, przenośnych i wbudowanych bez przepisywania kodu
źródłowego.

Ten pakiet zawiera dodatkowe narzędzia do budowania aplikacji Qt.

%package -n qt5-assistant
Summary:	Qt documentation browser
Summary(pl.UTF-8):	Przeglądarka dokumentacji Qt
Group:		X11/Development/Tools
# assistant: Core, Gui, Help, Network, PrintSupport, Sql, Widgets
# qcollectiongenerator: Core, Gui, Help
# qhelpconverter: Core, Gui, Widgets
# qhelpgenerator: Core, Gui, Help; sqldriver-sqlite3 to work
Requires:	Qt5Core >= %{qtbase_ver}
Requires:	Qt5Help = %{version}-%{release}
Requires:	Qt5Gui >= %{qtbase_ver}
Requires:	Qt5Network >= %{qtbase_ver}
Requires:	Qt5PrintSupport >= %{qtbase_ver}
Requires:	Qt5Sql >= %{qtbase_ver}
Requires:	Qt5Sql-sqldriver-sqlite3 >= %{qtbase_ver}
Requires:	Qt5Widgets >= %{qtbase_ver}

%description -n qt5-assistant
Qt Assistant is a tool for browsing on-line documentation with
indexing, bookmarks and full-text search.

%description -n qt5-assistant -l pl.UTF-8
Qt Assistant to narzędzie do przeglądania dokumentacji z możliwością
indeksowania, dodawania zakładek i pełnotekstowego wyszukiwania.

%package -n qt5-designer
Summary:	IDE used for GUI designing with Qt 5 library
Summary(pl.UTF-8):	IDE służące do projektowania GUI przy użyciu biblioteki Qt 5
Group:		X11/Applications
Requires:	Qt5Core >= %{qtbase_ver}
Requires:	Qt5Designer = %{version}-%{release}
Requires:	Qt5Gui >= %{qtbase_ver}
Requires:	Qt5Network >= %{qtbase_ver}
Requires:	Qt5PrintSupport >= %{qtbase_ver}
Requires:	Qt5Widgets >= %{qtbase_ver}
Requires:	Qt5Xml >= %{qtbase_ver}

%description -n qt5-designer
An advanced tool used for GUI designing with Qt 5 library.

%description -n qt5-designer -l pl.UTF-8
Zaawansowane narzędzie służące do projektowania interfejsu graficznego
przy użyciu biblioteki Qt 5.

%package -n qt5-linguist
Summary:	Translation helper for Qt 5
Summary(pl.UTF-8):	Aplikacja ułatwiająca tłumaczenie aplikacji opartych na Qt 5
Group:		X11/Development/Tools
# lconvert,lrelease,lupdate: Core, Xml
# linguist: Core, Gui, PrintSupport, Widgets, Xml
Requires:	Qt5Core >= %{qtbase_ver}
Requires:	Qt5Gui >= %{qtbase_ver}
Requires:	Qt5PrintSupport >= %{qtbase_ver}
Requires:	Qt5Widgets >= %{qtbase_ver}
Requires:	Qt5Xml >= %{qtbase_ver}

%description -n qt5-linguist
Translation helper for Qt 5.

%description -n qt5-linguist -l pl.UTF-8
Aplikacja ułatwiająca tłumaczenie aplikacji opartych na Qt 5.

%package -n qt5-qdbus
Summary:	Qt5 DBus tools
Summary(pl.UTF-8):	Narzędzia Qt5 do magistrali DBus
Group:		X11/Applications
# qdbus: Core, DBus, Xml
# qdbusviewer: Core, DBus, Gui, Widgets, Xml
Requires:	Qt5Core >= %{qtbase_ver}
Requires:	Qt5DBus >= %{qtbase_ver}
Requires:	Qt5Gui >= %{qtbase_ver}
Requires:	Qt5Widgets >= %{qtbase_ver}
Requires:	Qt5Xml >= %{qtbase_ver}

%description -n qt5-qdbus
This package contains the qdbus and qdbusviewer tools.

%description -n qt5-qdbus -l pl.UTF-8
Ten pakiet zawiera narzędzia qdbus i qdbusviewer.

%package -n Qt5CLucene
Summary:	Qt5 CLucene library
Summary(pl.UTF-8):	Biblioteka Qt5 CLucene
Group:		Libraries
Requires:	Qt5Core >= %{qtbase_ver}

%description -n Qt5CLucene
The Qt5 CLucene library provides Qt API to CLucene, a C++ port of
Lucene high-performance, full-featured text search engine.

%description -n Qt5CLucene -l pl.UTF-8
Biblioteka Qt5 CLucene dostarcza API Qt do CLucene - portu C++
wysoko wydajnego, w pełni funkcjonalnego silnika wyszukiwania
pełnotekstowego.

%package -n Qt5CLucene-devel
Summary:	Qt5 CLucene library - development files
Summary(pl.UTF-8):	Biblioteka Qt5 CLucene - pliki programistyczne
Group:		Development/Libraries
Requires:	Qt5CLucene = %{version}-%{release}
Requires:	Qt5Core-devel >= %{qtbase_ver}
Obsoletes:	qt5-qttools-devel

%description -n Qt5CLucene-devel
Header files for Qt5 CLucene library.

%description -n Qt5CLucene-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Qt5 CLucene.

%package -n Qt5Designer
Summary:	Qt5 Designer libraries
Summary(pl.UTF-8):	Biblioteki Qt5 Designer
Group:		X11/Libraries
Requires:	Qt5Core >= %{qtbase_ver}
Requires:	Qt5Gui >= %{qtbase_ver}
Requires:	Qt5Widgets >= %{qtbase_ver}
Requires:	Qt5Xml >= %{qtbase_ver}

%description -n Qt5Designer
The Qt5 Designer libraries provide classes to create your own custom
widget plugins for Qt Designer and classes to access Qt Designer
components.

%description -n Qt5Designer -l pl.UTF-8
Biblioteki Qt5 Designer dostarczają klasy do tworzenia wtyczek Qt
Designera do obsługi własnych widgetów oraz klasy pozwalające na
dostęp do komponentów Qt Designera.

%package -n Qt5Designer-devel
Summary:	Qt5 Designer libraries - development files
Summary(pl.UTF-8):	Biblioteki Qt5 Designer - pliki programistyczne
Group:		X11/Development/Libraries
Requires:	OpenGL-devel
Requires:	Qt5Core >= %{qtbase_ver}
Requires:	Qt5Designer = %{version}-%{release}
Requires:	Qt5Gui >= %{qtbase_ver}
Requires:	Qt5Widgets >= %{qtbase_ver}
Requires:	Qt5Xml >= %{qtbase_ver}
Obsoletes:	qt5-qttools-devel

%description -n Qt5Designer-devel
Header files for Qt5 Designer libraries.

%description -n Qt5Designer-devel -l pl.UTF-8
Pliki nagłówkowe bibliotek Qt5 Designer.

%package -n Qt5Designer-plugin-qquickwidget
Summary:	QQuickWidget (Quick2) plugin for Qt5 Designer
Summary(pl.UTF-8):	Wtyczka QQuickWidget (Quick2) dla Qt5 Designera
Group:		X11/Libraries
Requires:	Qt5Designer = %{version}-%{release}
Requires:	Qt5Quick >= %{qtdeclarative_ver}

%description -n Qt5Designer-plugin-qquickwidget
QQuickWidget (Quick2) plugin for Qt5 Designer.

%description -n Qt5Designer-plugin-qquickwidget -l pl.UTF-8
Wtyczka QQuickWidget (Quick2) dla Qt5 Designera.

%package -n Qt5Designer-plugin-qwebview
Summary:	QWebView plugin for Qt5 Designer
Summary(pl.UTF-8):	Wtyczka QWebView dla Qt5 Designera
Group:		X11/Libraries
Requires:	Qt5Designer = %{version}-%{release}
Requires:	Qt5WebKit >= %{qtwebkit_ver}

%description -n Qt5Designer-plugin-qwebview
QWebView plugin for Qt5 Designer.

%description -n Qt5Designer-plugin-qwebview -l pl.UTF-8
Wtyczka QWebView dla Qt5 Designera.

%package -n Qt5Help
Summary:	Qt5 Help library
Summary(pl.UTF-8):	Biblioteka Qt5 Help
Group:		X11/Libraries
Requires:	Qt5CLucene = %{version}-%{release}
Requires:	Qt5Core >= %{qtbase_ver}
Requires:	Qt5Gui >= %{qtbase_ver}
Requires:	Qt5Network >= %{qtbase_ver}
Requires:	Qt5Sql >= %{qtbase_ver}
Requires:	Qt5Widgets >= %{qtbase_ver}

%description -n Qt5Help
Qt5 Help library provides classes for integrating online documentation
in applications.

%description -n Qt5Help -l pl.UTF-8
Biblioteka Qt5 Help dostarcza klasy służące do integracji dokumentacji
online w aplikacjach.

%package -n Qt5Help-devel
Summary:	Qt5 Help library - development files
Summary(pl.UTF-8):	Biblioteka Qt5 Help - pliki programistyczne
Group:		X11/Development/Libraries
Requires:	Qt5CLucene-devel = %{version}-%{release}
Requires:	Qt5Core-devel >= %{qtbase_ver}
Requires:	Qt5Gui-devel >= %{qtbase_ver}
Requires:	Qt5Help = %{version}-%{release}
Requires:	Qt5Network-devel >= %{qtbase_ver}
Requires:	Qt5Sql-devel >= %{qtbase_ver}
Requires:	Qt5Widgets-devel >= %{qtbase_ver}
Obsoletes:	qt5-qttools-devel

%description -n Qt5Help-devel
Header files for Qt5 Help library.

%description -n Qt5Help-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Qt5 Help.

%package -n Qt5UiTools-devel
Summary:	Qt5 Ui Tools library - development files
Summary(pl.UTF-8):	Biblioteka Qt5 Ui Tools - pliki programistyczne
Group:		X11/Development/Libraries
Requires:	OpenGL-devel
Requires:	Qt5Core-devel >= %{qtbase_ver}
Requires:	Qt5Gui-devel >= %{qtbase_ver}
Requires:	Qt5Widgets-devel >= %{qtbase_ver}
Obsoletes:	qt5-qttools-devel

%description -n Qt5UiTools-devel
Header files and static Qt5 Ui Tools library.

Qt5 Ui Tools library provides classes to handle forms created with Qt
Designer.

%description -n Qt5UiTools-devel -l pl.UTF-8
Pliki nagłówkowe i statyczna biblioteka Qt5 Ui Tools.

Biblioteka Qt5 Ui Tools dostarcza klasy do obsługi formularzy
utworzonych przy użyciu Qt Designera.

%package doc
Summary:	Qt5 Tools documentation in HTML format
Summary(pl.UTF-8):	Dokumentacja do narzędzi Qt5 w formacie HTML
Group:		X11/Development/Libraries
Requires:	qt5-doc-common >= %{qtbase_ver}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc
Qt5 Tools documentation in HTML format.

%description doc -l pl.UTF-8
Dokumentacja do narzędzi Qt5 w formacie HTML.

%package doc-qch
Summary:	Qt5 Tools documentation in QCH format
Summary(pl.UTF-8):	Dokumentacja do narzędzi Qt5 w formacie QCH
Group:		X11/Development/Libraries
Requires:	qt5-doc-common >= %{qtbase_ver}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc-qch
Qt5 Tools documentation in QCH format.

%description doc-qch -l pl.UTF-8
Dokumentacja do narzędzi Qt5 w formacie QCH.

%package examples
Summary:	Qt5 Tools examples
Summary(pl.UTF-8):	Przykłady do narzędzi Qt5
Group:		X11/Development/Libraries
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description examples
Qt5 Tools - examples.

%description examples -l pl.UTF-8
Przykłady do narzędzi Qt5.

%prep
%setup -q -n %{orgname}-opensource-src-%{version} %{?with_qm:-a1}

%build
qmake-qt5
%{__make}

# build only HTML docs if without qch (which needs already installed qhelpgenerator)
%{__make} %{!?with_qch:html_}docs

%if %{with qm}
cd qttranslations-opensource-src-%{version}
qmake-qt5
%{__make}
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%{__make} install_%{!?with_qch:html_}docs \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%if %{with qm}
%{__make} -C qttranslations-opensource-src-%{version} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT
# keep only assistant, designer, linguist, qt_help, qtconfig here
%{__rm} $RPM_BUILD_ROOT%{_datadir}/qt5/translations/{qmlviewer,qtbase,qtconnectivity,qtdeclarative,qtlocation,qtmultimedia,qtquick1,qtquickcontrols,qtscript,qtxmlpatterns}_*.qm
%{__rm} $RPM_BUILD_ROOT%{_datadir}/qt5/translations/qt_{??,??_??}.qm
# qtconfig build is currently disabled (see src/src.pro)
%{__rm} $RPM_BUILD_ROOT%{_datadir}/qt5/translations/qtconfig_*.qm
%endif

# kill unnecessary -L%{_libdir} from *.la, *.prl, *.pc
%{__sed} -i -e "s,-L%{_libdir} \?,,g" \
	$RPM_BUILD_ROOT%{_libdir}/*.{la,prl} \
	$RPM_BUILD_ROOT%{_pkgconfigdir}/*.pc

# useless symlinks
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.so.5.?
# actually drop *.la, follow policy of not packaging them when *.pc exist
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.la

# symlinks in system bin dir
cd $RPM_BUILD_ROOT%{_bindir}
ln -sf ../%{_lib}/qt5/bin/assistant assistant-qt5
ln -sf ../%{_lib}/qt5/bin/designer designer-qt5
ln -sf ../%{_lib}/qt5/bin/lconvert lconvert-qt5
ln -sf ../%{_lib}/qt5/bin/linguist linguist-qt5
ln -sf ../%{_lib}/qt5/bin/lrelease lrelease-qt5
ln -sf ../%{_lib}/qt5/bin/lupdate lupdate-qt5
ln -sf ../%{_lib}/qt5/bin/pixeltool pixeltool-qt5
ln -sf ../%{_lib}/qt5/bin/qcollectiongenerator qcollectiongenerator-qt5
ln -sf ../%{_lib}/qt5/bin/qdbus qdbus-qt5
ln -sf ../%{_lib}/qt5/bin/qdbusviewer qdbusviewer-qt5
ln -sf ../%{_lib}/qt5/bin/qhelpconverter qhelpconverter-qt5
ln -sf ../%{_lib}/qt5/bin/qhelpgenerator qhelpgenerator-qt5
ln -sf ../%{_lib}/qt5/bin/qtdiag qtdiag-qt5
ln -sf ../%{_lib}/qt5/bin/qtpaths qtpaths-qt5
cd -

# Prepare some files list
ifecho() {
	r="$RPM_BUILD_ROOT$2"
	if [ -d "$r" ]; then
		echo "%%dir $2" >> $1.files
	elif [ -x "$r" ] ; then
		echo "%%attr(755,root,root) $2" >> $1.files
	elif [ -f "$r" ]; then
		echo "$2" >> $1.files
	else
		echo "Error generation $1 files list!"
		echo "$r: no such file or directory!"
		return 1
	fi
}
ifecho_tree() {
	ifecho $1 $2
	for f in `find $RPM_BUILD_ROOT$2 -printf "%%P "`; do
		ifecho $1 $2/$f
	done
}

echo "%defattr(644,root,root,755)" > examples.files
ifecho_tree examples %{_examplesdir}/qt5/assistant
ifecho_tree examples %{_examplesdir}/qt5/designer
ifecho_tree examples %{_examplesdir}/qt5/help
ifecho_tree examples %{_examplesdir}/qt5/linguist
ifecho_tree examples %{_examplesdir}/qt5/uitools

# find_lang --with-qm supports only PLD qt3/qt4 specific %{_datadir}/locale/*/LC_MESSAGES layout
find_qt5_qm()
{
	name="$1"
	find $RPM_BUILD_ROOT%{_datadir}/qt5/translations -name "${name}_*.qm" | \
		sed -e "s:^$RPM_BUILD_ROOT::" \
		    -e 's:\(.*/'$name'_\)\([a-z][a-z][a-z]\?\)\(_[A-Z][A-Z]\)\?\(\.qm\)$:%lang(\2\3) \1\2\3\4:'
}

echo '%defattr(644,root,root,755)' > assistant.lang
echo '%defattr(644,root,root,755)' > designer.lang
echo '%defattr(644,root,root,755)' > linguist.lang
echo '%defattr(644,root,root,755)' > qt_help.lang
%if %{with qm}
find_qt5_qm assistant >> assistant.lang
find_qt5_qm designer >> designer.lang
find_qt5_qm linguist >> linguist.lang
find_qt5_qm qt_help >> qt_help.lang
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n Qt5CLucene -p /sbin/ldconfig
%postun	-n Qt5CLucene -p /sbin/ldconfig

%post	-n Qt5Designer -p /sbin/ldconfig
%postun	-n Qt5Designer -p /sbin/ldconfig

%post	-n Qt5Help -p /sbin/ldconfig
%postun	-n Qt5Help -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LGPL_EXCEPTION.txt dist/changes-*
%attr(755,root,root) %{_bindir}/pixeltool-qt5
%attr(755,root,root) %{_bindir}/qtdiag-qt5
%attr(755,root,root) %{_bindir}/qtpaths-qt5
%attr(755,root,root) %{qt5dir}/bin/pixeltool
%attr(755,root,root) %{qt5dir}/bin/qtdiag
%attr(755,root,root) %{qt5dir}/bin/qtpaths

%files -n qt5-assistant -f assistant.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/assistant-qt5
%attr(755,root,root) %{_bindir}/qcollectiongenerator-qt5
%attr(755,root,root) %{_bindir}/qhelpconverter-qt5
%attr(755,root,root) %{_bindir}/qhelpgenerator-qt5
%attr(755,root,root) %{qt5dir}/bin/assistant
%attr(755,root,root) %{qt5dir}/bin/qcollectiongenerator
%attr(755,root,root) %{qt5dir}/bin/qhelpconverter
%attr(755,root,root) %{qt5dir}/bin/qhelpgenerator

%files -n qt5-designer -f designer.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/designer-qt5
%attr(755,root,root) %{qt5dir}/bin/designer

%files -n qt5-linguist -f linguist.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lconvert-qt5
%attr(755,root,root) %{_bindir}/linguist-qt5
%attr(755,root,root) %{_bindir}/lrelease-qt5
%attr(755,root,root) %{_bindir}/lupdate-qt5
%attr(755,root,root) %{qt5dir}/bin/lconvert
%attr(755,root,root) %{qt5dir}/bin/linguist
%attr(755,root,root) %{qt5dir}/bin/lrelease
%attr(755,root,root) %{qt5dir}/bin/lupdate
%{_datadir}/qt5/phrasebooks
%{_libdir}/cmake/Qt5LinguistTools

%files -n qt5-qdbus
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qdbus-qt5
%attr(755,root,root) %{_bindir}/qdbusviewer-qt5
%attr(755,root,root) %{qt5dir}/bin/qdbus
%attr(755,root,root) %{qt5dir}/bin/qdbusviewer

%files -n Qt5CLucene
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5CLucene.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5CLucene.so.5

%files -n Qt5CLucene-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5CLucene.so
%{_libdir}/libQt5CLucene.prl
%{_includedir}/qt5/QtCLucene
%{_pkgconfigdir}/Qt5CLucene.pc
%{qt5dir}/mkspecs/modules/qt_lib_clucene_private.pri

%files -n Qt5Designer
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Designer.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5Designer.so.5
%attr(755,root,root) %{_libdir}/libQt5DesignerComponents.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5DesignerComponents.so.5

%dir %{qt5dir}/plugins/designer
%attr(755,root,root) %{qt5dir}/plugins/designer/libcontainerextension.so
%attr(755,root,root) %{qt5dir}/plugins/designer/libcustomwidgetplugin.so
%attr(755,root,root) %{qt5dir}/plugins/designer/libtaskmenuextension.so
%attr(755,root,root) %{qt5dir}/plugins/designer/libworldtimeclockplugin.so

# common for base -devel and plugin-specific files (from other source packages)
%dir %{_libdir}/cmake/Qt5Designer

%files -n Qt5Designer-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Designer.so
%attr(755,root,root) %{_libdir}/libQt5DesignerComponents.so
%{_libdir}/libQt5Designer.prl
%{_libdir}/libQt5DesignerComponents.prl
%{_includedir}/qt5/QtDesigner
%{_includedir}/qt5/QtDesignerComponents
%{_pkgconfigdir}/Qt5Designer.pc
%{_pkgconfigdir}/Qt5DesignerComponents.pc
%{_libdir}/cmake/Qt5Designer/Qt5DesignerConfig*.cmake
%{_libdir}/cmake/Qt5Designer/Qt5Designer_AnalogClockPlugin.cmake
%{_libdir}/cmake/Qt5Designer/Qt5Designer_MultiPageWidgetPlugin.cmake
%{_libdir}/cmake/Qt5Designer/Qt5Designer_TicTacToePlugin.cmake
%{_libdir}/cmake/Qt5Designer/Qt5Designer_WorldTimeClockPlugin.cmake
%{qt5dir}/mkspecs/modules/qt_lib_designer.pri
%{qt5dir}/mkspecs/modules/qt_lib_designer_private.pri
%{qt5dir}/mkspecs/modules/qt_lib_designercomponents_private.pri

%if %{with qtdeclarative}
%files -n Qt5Designer-plugin-qquickwidget
%defattr(644,root,root,755)
%attr(755,root,root) %{qt5dir}/plugins/designer/libqquickwidget.so
%{_libdir}/cmake/Qt5Designer/Qt5Designer_QQuickWidgetPlugin.cmake
%endif

%if %{with qtwebkit}
%files -n Qt5Designer-plugin-qwebview
%defattr(644,root,root,755)
%attr(755,root,root) %{qt5dir}/plugins/designer/libqwebview.so
%{_libdir}/cmake/Qt5Designer/Qt5Designer_QWebViewPlugin.cmake
%endif

%files -n Qt5Help -f qt_help.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Help.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5Help.so.5

%files -n Qt5Help-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Help.so
%{_libdir}/libQt5Help.prl
%{_includedir}/qt5/QtHelp
%{_pkgconfigdir}/Qt5Help.pc
%{_libdir}/cmake/Qt5Help
%{qt5dir}/mkspecs/modules/qt_lib_help.pri
%{qt5dir}/mkspecs/modules/qt_lib_help_private.pri

%files -n Qt5UiTools-devel
%defattr(644,root,root,755)
# static-only
%{_libdir}/libQt5UiTools.a
%{_libdir}/libQt5UiTools.prl
%{_includedir}/qt5/QtUiTools
%{_pkgconfigdir}/Qt5UiTools.pc
%{_libdir}/cmake/Qt5UiTools
%{qt5dir}/mkspecs/modules/qt_lib_uitools.pri
%{qt5dir}/mkspecs/modules/qt_lib_uitools_private.pri

%files examples -f examples.files
%defattr(644,root,root,755)
# XXX: dir shared with qt5-qtbase-examples
%dir %{_examplesdir}/qt5

%files doc
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtassistant
%{_docdir}/qt5-doc/qtdesigner
%{_docdir}/qt5-doc/qthelp
%{_docdir}/qt5-doc/qtlinguist
%{_docdir}/qt5-doc/qtuitools

%if %{with qch}
%files doc-qch
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtassistant.qch
%{_docdir}/qt5-doc/qtdesigner.qch
%{_docdir}/qt5-doc/qthelp.qch
%{_docdir}/qt5-doc/qtlinguist.qch
%{_docdir}/qt5-doc/qtuitools.qch
%endif
