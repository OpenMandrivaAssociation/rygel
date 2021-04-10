%define url_ver %(echo %{version} | cut -d. -f1,2)
%define _disable_ld_no_undefined 1
%define _disable_rebuild_configure 1

%define api	2.6
%define major	2
%define girapi		2.6
%define libname %mklibname %{name} %{api} %{major}
%define devname %mklibname %{name} %{api} -d
%define girname		%mklibname %{name}-gir %{girapi}


%define ruihapi 2.0
%define ruihmajor 1
%define libruihname %mklibname %{name}-ruih %{ruihapi} %{ruihmajor}

Summary:	A UPnP v2 Media Server
Name:		rygel
Version:	0.40.1
Release:	1
Group:		Sound
License:	LGPLv2+
URL:		http://live.gnome.org/Rygel
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:	intltool
BuildRequires:	meson
BuildRequires:	vala >= 0.14.1
BuildRequires:  valadoc
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gee-0.8)
BuildRequires:	pkgconfig(gio-2.0) >= 2.26
BuildRequires:	pkgconfig(gssdp-1.2)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gstreamer-app-1.0)
BuildRequires:	pkgconfig(gstreamer-base-1.0)
BuildRequires:	pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:	pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gst-editing-services-1.0)
BuildRequires:	pkgconfig(gtk+-3.0) >= 2.90.3
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:	pkgconfig(gupnp-1.2)
BuildRequires:	pkgconfig(gupnp-av-1.0) >= 0.9.0
BuildRequires:	pkgconfig(gupnp-dlna-2.0)
BuildRequires:	pkgconfig(libmediaart-2.0)
BuildRequires:	pkgconfig(libsoup-2.4) >= 2.34.0
BuildRequires:	pkgconfig(sqlite3) >= 3.5
BuildRequires:	pkgconfig(uuid) >= 1.41.3
BuildRequires:	pkgconfig(tracker-sparql-2.0)
BuildRequires:	tracker-vala

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
Requires:	%{name} = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libruihname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}

%description -n %{devname}
Files for development with %{name}.

%package tracker
Summary:	Tracker plugin for %{name}
Group:		Sound/Utilities
Requires:	%{name} = %{version}-%{release}
Requires:	tracker

%description tracker
A plugin for rygel to use tracker to locate media on the local machine.


%package -n %{girname}
Summary:	GObject Introspection interface library for %{name}
Group:		System/Libraries

Conflicts:	%{name} < 0.36.2-2

%description -n %{girname}
GObject Introspection interface library for %{name}.


%prep
%setup -q
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome --with-html

#Remove libtool archives.
find %{buildroot} -name '*.la' -exec rm -f {} ';'
%files -f %name.lang

%doc AUTHORS COPYING TODO NEWS
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}
%{_bindir}/%{name}-preferences
%{_libexecdir}/%{name}/mx-extract
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}*
%{_iconsdir}/*/*/*/*
%{_datadir}/dbus-1/services/org.gnome.Rygel1.service
%{_userunitdir}/%{name}.service
#{_mandir}/man?/%{name}*
%{_mandir}/man1/rygel.1.*
%{_mandir}/man5/rygel.conf.5.*

%dir %{_libdir}/%{name}-%{api}
%dir %{_libdir}/%{name}-%{api}/plugins
%{_libdir}/%{name}-%{api}/plugins/*media-export.*
%{_libdir}/%{name}-%{api}/plugins/*external.*
%{_libdir}/%{name}-%{api}/plugins/*playbin.*
%{_libdir}/%{name}-%{api}/plugins/*lms.*
%{_libdir}/%{name}-%{api}/plugins/*mpris.*
%{_libdir}/%{name}-%{api}/plugins/*gst-launch.*
%{_libdir}/%{name}-%{api}/plugins/*ruih.*
%{_libdir}/%{name}-%{api}/plugins/*example-*.*
%{_libdir}/%{name}-%{api}/engines/*media-engine-simple.*
%{_libdir}/%{name}-%{api}/engines/*media-engine-gst.*

%files -n %{libname}
%{_libdir}/lib*-%{api}.so.%{major}*

%files -n %{libruihname}
%{_libdir}/librygel-ruih-%{ruihapi}.so.%{ruihmajor}*

%files -n %{devname}
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}-*-%{api}.pc
%{_libdir}/pkgconfig/rygel-ruih-%{ruihapi}.pc
%{_includedir}/%{name}-%{api}
%{_datadir}/vala/vapi/*
%{_datadir}/gir-1.0/RygelCore-%{girapi}.gir
%{_datadir}/gir-1.0/RygelRendererGst-%{girapi}.gir
%{_datadir}/gir-1.0/RygelRenderer-%{girapi}.gir
%{_datadir}/gir-1.0/RygelServer-%{girapi}.gir

%files tracker
%{_libdir}/%{name}-%{api}/plugins/*tracker.*
%{_libdir}/%{name}-%{api}/plugins/librygel-tracker3.so
%{_libdir}/%{name}-%{api}/plugins/tracker3.plugin

%files -n %{girname}
%{_libdir}/girepository-1.0/RygelCore-%{girapi}.typelib
%{_libdir}/girepository-1.0/RygelRendererGst-%{girapi}.typelib
%{_libdir}/girepository-1.0/RygelRenderer-%{girapi}.typelib
%{_libdir}/girepository-1.0/RygelServer-%{girapi}.typelib
