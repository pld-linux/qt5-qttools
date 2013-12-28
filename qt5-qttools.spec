# TODO:
# - use PLD ldflags
# - cleanup
# - symlinks

%define		orgname		qttools
Summary:	The Qt5 Tools
Name:		qt5-%{orgname}
Version:	5.2.0
Release:	0.1
License:	LGPL v2.1 or GPL v3.0
Group:		X11/Libraries
Source0:	http://download.qt-project.org/official_releases/qt/5.2/%{version}/submodules/%{orgname}-opensource-src-%{version}.tar.xz
# Source0-md5:	76a0992967b6d02220ecb69a5ba04ef1
URL:		http://qt-project.org/
BuildRequires:	qt5-qtbase-devel = %{version}
BuildRequires:	rpmbuild(macros) >= 1.654
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_noautostrip	'.*_debug\\.so*'

%define		specflags	-fno-strict-aliasing
%define		_qtdir		%{_libdir}/qt5

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

%description doc
Qt5 Tools docs.

%package examples
Summary:	Qt5 Tools examples
Group:		X11/Development/Libraries

%description examples
Qt5 Tools - examples.

%prep
%setup -q -n %{orgname}-opensource-src-%{version}

%build
qmake-qt5
%{__make}
%{__make} html_docs

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install install_html_docs \
	INSTALL_ROOT=$RPM_BUILD_ROOT

# Prepare some files list
ifecho() {
	RESULT=`echo $RPM_BUILD_ROOT$2 2>/dev/null`
	[ "$RESULT" == "" ] && return # XXX this is never true due $RPM_BUILD_ROOT being set
	r=`echo $RESULT | awk '{ print $1 }'`

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

echo "%defattr(644,root,root,755)" > examples.files
ifecho examples %{_examplesdir}/qt5
for f in `find $RPM_BUILD_ROOT%{_examplesdir}/qt5 -printf "%%P "`; do
	ifecho examples %{_examplesdir}/qt5/$f
done

%clean
rm -rf $RPM_BUILD_ROOT

%post		-p /sbin/ldconfig
%postun		-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQt5CLucene.so.?
%attr(755,root,root) %{_libdir}/libQt5CLucene.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5Designer.so.?
%attr(755,root,root) %{_libdir}/libQt5Designer.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5DesignerComponents.so.?
%attr(755,root,root) %{_libdir}/libQt5DesignerComponents.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5Help.so.?
%attr(755,root,root) %{_libdir}/libQt5Help.so.*.*

%{_libdir}/libQt5UiTools.a
%attr(755,root,root) %{_qtdir}/bin/*
%attr(755,root,root) %{_qtdir}/plugins
%{_datadir}/qt5

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5CLucene.so
%attr(755,root,root) %{_libdir}/libQt5Designer.so
%attr(755,root,root) %{_libdir}/libQt5DesignerComponents.so
%attr(755,root,root) %{_libdir}/libQt5Help.so

%{_libdir}/libQt5CLucene.la
%{_libdir}/libQt5Designer.la
%{_libdir}/libQt5DesignerComponents.la
%{_libdir}/libQt5Help.la
%{_libdir}/libQt5UiTools.la

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

%{_pkgconfigdir}/*.pc

%{_qtdir}/mkspecs

%files examples -f examples.files

%files doc
%defattr(644,root,root,755)
%{_docdir}/qt5-doc