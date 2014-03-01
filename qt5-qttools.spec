# TODO:
# - cleanup
# - symlinks

%define		orgname		qttools
Summary:	The Qt5 Tools
Name:		qt5-%{orgname}
Version:	5.2.0
Release:	0.1
License:	LGPL v2.1 with Digia Qt LGPL Exception v1.1 or GPL v3.0
Group:		X11/Libraries
Source0:	http://download.qt-project.org/official_releases/qt/5.2/%{version}/submodules/%{orgname}-opensource-src-%{version}.tar.xz
# Source0-md5:	76a0992967b6d02220ecb69a5ba04ef1
URL:		http://qt-project.org/
BuildRequires:	OpenGL-devel
BuildRequires:	Qt5Core-devel >= %{version}
BuildRequires:	Qt5Gui-devel >= %{version}
BuildRequires:	Qt5Network-devel >= %{version}
BuildRequires:	Qt5PrintSupport-devel >= %{version}
BuildRequires:	Qt5Sql-devel >= %{version}
BuildRequires:	Qt5Widgets-devel >= %{version}
BuildRequires:	Qt5Xml-devel >= %{version}
BuildRequires:	qt5-build >= %{version}
BuildRequires:	qt5-doc-common >= %{version}
BuildRequires:	qt5-qmake >= %{version}
BuildRequires:	rpmbuild(macros) >= 1.654
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing
%define		qt5dir		%{_libdir}/qt5

%description
Qt5 Tools.

%package devel
Summary:	The Qt5 Tools - development files
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Qt5 Tools - development files.

%package doc
Summary:	Qt5 Tools docs
Group:		X11/Development/Libraries
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc
Qt5 Tools docs.

%package examples
Summary:	Qt5 Tools examples
Group:		X11/Development/Libraries
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description examples
Qt5 Tools - examples.

%prep
%setup -q -n %{orgname}-opensource-src-%{version}

%build
qmake-qt5
%{__make}

# build only HTML docs (for now? qch docs target tries to use already installed qhelpgenerator)
%{__make} html_docs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%{__make} install_html_docs \
	INSTALL_ROOT=$RPM_BUILD_ROOT

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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LGPL_EXCEPTION.txt dist/changes-*

%attr(755,root,root) %{_libdir}/libQt5CLucene.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5CLucene.so.5
%attr(755,root,root) %{_libdir}/libQt5Designer.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5Designer.so.5
%attr(755,root,root) %{_libdir}/libQt5DesignerComponents.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5DesignerComponents.so.5
%attr(755,root,root) %{_libdir}/libQt5Help.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5Help.so.5

%attr(755,root,root) %{_bindir}/assistant-qt5
%attr(755,root,root) %{_bindir}/designer-qt5
%attr(755,root,root) %{_bindir}/lconvert-qt5
%attr(755,root,root) %{_bindir}/linguist-qt5
%attr(755,root,root) %{_bindir}/lrelease-qt5
%attr(755,root,root) %{_bindir}/lupdate-qt5
%attr(755,root,root) %{_bindir}/pixeltool-qt5
%attr(755,root,root) %{_bindir}/qcollectiongenerator-qt5
%attr(755,root,root) %{_bindir}/qdbus-qt5
%attr(755,root,root) %{_bindir}/qdbusviewer-qt5
%attr(755,root,root) %{_bindir}/qhelpconverter-qt5
%attr(755,root,root) %{_bindir}/qhelpgenerator-qt5
%attr(755,root,root) %{_bindir}/qtpaths-qt5
%attr(755,root,root) %{qt5dir}/bin/assistant
%attr(755,root,root) %{qt5dir}/bin/designer
%attr(755,root,root) %{qt5dir}/bin/lconvert
%attr(755,root,root) %{qt5dir}/bin/linguist
%attr(755,root,root) %{qt5dir}/bin/lrelease
%attr(755,root,root) %{qt5dir}/bin/lupdate
%attr(755,root,root) %{qt5dir}/bin/pixeltool
%attr(755,root,root) %{qt5dir}/bin/qcollectiongenerator
%attr(755,root,root) %{qt5dir}/bin/qdbus
%attr(755,root,root) %{qt5dir}/bin/qdbusviewer
%attr(755,root,root) %{qt5dir}/bin/qhelpconverter
%attr(755,root,root) %{qt5dir}/bin/qhelpgenerator
%attr(755,root,root) %{qt5dir}/bin/qtpaths

%dir %{qt5dir}/plugins
%dir %{qt5dir}/plugins/designer
%attr(755,root,root) %{qt5dir}/plugins/designer/libcontainerextension.so
%attr(755,root,root) %{qt5dir}/plugins/designer/libcustomwidgetplugin.so
%attr(755,root,root) %{qt5dir}/plugins/designer/libtaskmenuextension.so
%attr(755,root,root) %{qt5dir}/plugins/designer/libworldtimeclockplugin.so

%dir %{_datadir}/qt5
%{_datadir}/qt5/phrasebooks

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5CLucene.so
%attr(755,root,root) %{_libdir}/libQt5Designer.so
%attr(755,root,root) %{_libdir}/libQt5DesignerComponents.so
%attr(755,root,root) %{_libdir}/libQt5Help.so

# static-only
%{_libdir}/libQt5UiTools.a

%{_libdir}/libQt5CLucene.prl
%{_libdir}/libQt5Designer.prl
%{_libdir}/libQt5DesignerComponents.prl
%{_libdir}/libQt5Help.prl
%{_libdir}/libQt5UiTools.prl

%{_libdir}/cmake/Qt5Designer
%{_libdir}/cmake/Qt5Help
%{_libdir}/cmake/Qt5LinguistTools
%{_libdir}/cmake/Qt5UiTools

%{_includedir}/qt5/QtCLucene
%{_includedir}/qt5/QtDesigner
%{_includedir}/qt5/QtDesignerComponents
%{_includedir}/qt5/QtHelp
%{_includedir}/qt5/QtUiTools

%{_pkgconfigdir}/Qt5CLucene.pc
%{_pkgconfigdir}/Qt5Designer.pc
%{_pkgconfigdir}/Qt5DesignerComponents.pc
%{_pkgconfigdir}/Qt5Help.pc
%{_pkgconfigdir}/Qt5UiTools.pc

%{qt5dir}/mkspecs/modules/qt_lib_clucene_private.pri
%{qt5dir}/mkspecs/modules/qt_lib_designer.pri
%{qt5dir}/mkspecs/modules/qt_lib_designer_private.pri
%{qt5dir}/mkspecs/modules/qt_lib_designercomponents_private.pri
%{qt5dir}/mkspecs/modules/qt_lib_help.pri
%{qt5dir}/mkspecs/modules/qt_lib_help_private.pri
%{qt5dir}/mkspecs/modules/qt_lib_uitools.pri
%{qt5dir}/mkspecs/modules/qt_lib_uitools_private.pri

%files examples -f examples.files
%defattr(644,root,root,755)
# XXX: dir shared with qt5-qtbase-examples
%dir %{_examplesdir}/qt5

%files doc
%defattr(644,root,root,755)
# XXX: dir shared with qt5-qtbase-doc
%dir %{_docdir}/qt5-doc
%{_docdir}/qt5-doc/qtassistant
%{_docdir}/qt5-doc/qtdesigner
%{_docdir}/qt5-doc/qthelp
%{_docdir}/qt5-doc/qtlinguist
%{_docdir}/qt5-doc/qtuitools
