%define url_ver %(echo %{version} | cut -d. -f1,2)
%define _disable_ld_no_undefined 1

%define api	2.6
%define major	2
%define libname %mklibname %{name} %{api} %{major}
%define devname %mklibname %{name} %{api} -d

%define ruihapi 2.0
%define ruihmajor 1
%define libruihname %mklibname %{name}-ruih %{ruihapi} %{ruihmajor}

Summary:	A UPnP v2 Media Server
Name:		rygel
Version:	0.26.0
Release:	2
Group:		Sound
License:	LGPLv2+
URL:		http://live.gnome.org/Rygel
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	vala >= 0.14.1
BuildRequires:	pkgconfig(gee-0.8)
BuildRequires:	pkgconfig(gio-2.0) >= 2.26
BuildRequires:	pkgconfig(gssdp-1.0) >= 0.11.0
BuildRequires:	pkgconfig(gssdp-1.0)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gstreamer-app-1.0)
BuildRequires:	pkgconfig(gstreamer-base-1.0)
BuildRequires:	pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:	pkgconfig(gstreamer-tag-1.0)
BuildRequires:	pkgconfig(gtk+-3.0) >= 2.90.3
BuildRequires:	pkgconfig(gupnp-1.0) >= 0.17.1
BuildRequires:	pkgconfig(gupnp-av-1.0) >= 0.9.0
BuildRequires:	pkgconfig(gupnp-dlna-2.0)
BuildRequires:	pkgconfig(libmediaart-2.0)
BuildRequires:	pkgconfig(libsoup-2.4) >= 2.34.0
BuildRequires:	pkgconfig(sqlite3) >= 3.5
BuildRequires:	pkgconfig(uuid) >= 1.41.3
BuildRequires:	pkgconfig(tracker-sparql-1.0)

Requires:	shared-mime-info
Requires:	gstreamer1.0-plugins-good
Requires:	gstreamer1.0-libav
Requires:	gstreamer1.0-plugins-bad
Requires:	gstreamer1.0-plugins-ugly

%description
Rygel is an implementation of the UPnP MediaServer V 2.0 specification that is
specifically designed for GNOME. It is based on GUPnP and is written (mostly)
in Vala language. The project was previously known as gupnp-media-server.

%package -n %{libname}
Summary:	Shared libraries for %{name}
Group:		System/Libraries

%description -n %{libname}
Shared libraries for %{name}.

%package -n %{libruihname}
Summary:        Shared libraries for %{name}
Group:          System/Libraries

%description -n %{libruihname}
Shared libraries for %{name}.


%package -n %{devname}
Summary:	Development package for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libruihname} = %{version}-%{release}

%description -n %{devname}
Files for development with %{name}.

%prep
%setup -q

%build
%configure \
	--disable-media-export-plugin \
	--enable-test-plugin \
	--enable-external-plugin \
	--enable-mediathek-plugin \
	--enable-gst-launch-plugin \
	--enable-playbin-plugin \
	--disable-introspection \
	--disable-silent-rules LIBS='-lxml2'

%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome --with-html

#Remove libtool archives.
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files -f %name.lang
%doc AUTHORS COPYING README TODO NEWS
%config(noreplace) %{_sysconfdir}/rygel.conf
%{_bindir}/rygel
%{_bindir}/rygel-preferences
%{_libdir}/rygel-%{api}
%{_datadir}/rygel/
%{_datadir}/applications/rygel*
%{_iconsdir}/*/*/*/*
%{_mandir}/man?/*
%{_datadir}/dbus-1/services/org.gnome.Rygel1.service

%files -n %{libname}
%{_libdir}/lib*-%{api}.so.%{major}*

%files -n %{libruihname}
%{_libdir}/librygel-ruih-%{ruihapi}.so.%{ruihmajor}*

%files -n %{devname}
%{_libdir}/*.so
%{_includedir}/rygel-%{api}/
%{_libdir}/pkgconfig/rygel-core-%{api}.pc
%{_libdir}/pkgconfig/rygel-renderer-%{api}.pc
%{_libdir}/pkgconfig/rygel-renderer-gst-%{api}.pc
%{_libdir}/pkgconfig/rygel-server-%{api}.pc
%{_datadir}/vala/vapi/*
%{_datadir}/gtk-doc/html/librygel-*
