Summary:	Xfce4 Dictionary
Summary(pl.UTF-8):	Słownik dla Xfce4
Name:		xfce4-dict
Version:	0.8.8
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	https://archive.xfce.org/src/apps/xfce4-dict/0.8/%{name}-%{version}.tar.bz2
# Source0-md5:	988a36f3893802a41c94b10a35d04fe4
URL:		https://goodies.xfce.org/projects/applications/xfce4-dict
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.24.0
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel >= 4.14.0
BuildRequires:	libxfce4util-devel >= 4.14.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	xfce4-dev-tools >= 4.14.0
BuildRequires:	xfce4-panel-devel >= 4.14.0
BuildRequires:	xfce4-panel-devel >= 4.14.0
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program allows you to search different kinds of dictionary
services for words or phrases and shows you the result. Currently you
can query a Dict server(RFC 2229), any online dictionary service by
opening a web browser or search for words using the aspell/ispell
program.

%description -l pl.UTF-8
Ten program pozwala przeszukiwać różne serwisy słownikowe w celu
wyszukania słów lub fraz. Obecnie można odpytywać serwer słownika
(zgodny z RFC 2229) przy pomocy przeglądarki albo programu
aspell/ispell.

%package plugin
Summary:	Xfce panel plugin for xfce4-dict
Summary(pl.UTF-8):	Wtyczka dla panelu Xfce dla xfce4-dict
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	xfce4-panel >= 4.11.0

%description plugin
Xfce panel plugin for xfce4-dict.

%description plugin -l pl.UTF-8
Wtyczka dla panelu Xfce dla xfce4-dict.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{fa_IR,hye,ur_PK}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/xfce4/panel/plugins/libxfce4dict.la
# unify
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{hy_AM,hy}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/xfce4-dict
%{_iconsdir}/hicolor/*x*/apps/org.xfce.Dictionary.png
%{_iconsdir}/hicolor/scalable/apps/*.svg
%{_desktopdir}/xfce4-dict.desktop
%{_mandir}/man1/xfce4-dict.1*

%files plugin
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libxfce4dict.so
%{_datadir}/xfce4/panel/plugins/xfce4-dict-plugin.desktop
