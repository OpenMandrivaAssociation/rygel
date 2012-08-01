%define url_ver %(echo %{version} | cut -d. -f1,2)

Name:           rygel
Version:        0.15.1
Release:        1
Summary:        A UPnP v2 Media Server
Group:          Sound
License:        LGPLv2+
URL:            http://live.gnome.org/Rygel
Source0:        http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires: pkgconfig(gee-1.0) >= 0.5.2
BuildRequires: pkgconfig(gio-2.0) >= 2.26
BuildRequires: pkgconfig(gssdp-1.0) >= 0.11.0
BuildRequires: pkgconfig(gssdp-1.0) <= 0.12.9999
BuildRequires: pkgconfig(gstreamer-0.10) >= 0.10.35
BuildRequires: pkgconfig(gstreamer-app-0.10) >= 0.10.28
BuildRequires: pkgconfig(gstreamer-base-0.10) >= 0.10.35
BuildRequires: pkgconfig(gstreamer-pbutils-0.10) >= 0.10.35
BuildRequires: pkgconfig(gstreamer-tag-0.10) >= 0.10.28
BuildRequires: pkgconfig(gtk+-3.0) >= 2.90.3
BuildRequires: pkgconfig(gupnp-1.0) >= 0.17.1
BuildRequires: pkgconfig(gupnp-av-1.0) >= 0.9.0
BuildRequires: pkgconfig(gupnp-vala-1.0) >= 0.10.2
BuildRequires: pkgconfig(gupnp-dlna-1.0) >= 0.6.6
BuildRequires: pkgconfig(libsoup-2.4) >= 2.34.0
BuildRequires: pkgconfig(sqlite3) >= 3.5
BuildRequires: pkgconfig(uuid) >= 1.41.3
BuildRequires:	tracker-devel
BuildRequires:	intltool
BuildRequires:	vala >= 0.14.1
Requires:	shared-mime-info
Requires:	gstreamer0.10-plugins-good
Requires:	gstreamer0.10-ffmpeg
Requires:	gstreamer0.10-plugins-bad
Requires:	gstreamer0.10-plugins-ugly

%description
Rygel is an implementation of the UPnP MediaServer V 2.0 specification that is 
specifically designed for GNOME. It is based on GUPnP and is written (mostly) 
in Vala language. The project was previously known as gupnp-media-server. 

%package devel
Summary:	Development package for %{name}
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

%description devel
Files for development with %{name}.

%package tracker
Summary:	Tracker plugin for %{name}
Group:		Sound
Requires:	%{name} = %{version}-%{release}
Requires:	tracker

%description tracker
A plugin for rygel to use tracker to locate media on the local machine.

%prep
%setup -q

%build
%configure2_5x \
        --disable-media-export-plugin \
	--enable-test-plugin \
	--enable-tracker-plugin \
	--enable-external-plugin \
	--enable-mediathek-plugin \
	--enable-gst-launch-plugin \
	--enable-playbin-plugin \
	--disable-silent-rules 
%make

%install
%makeinstall_std

%find_lang %{name}

#Remove libtool archives.
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files -f %name.lang
%doc AUTHORS COPYING README TODO NEWS
%config(noreplace) %{_sysconfdir}/rygel.conf
%{_bindir}/rygel
%{_bindir}/rygel-preferences
%dir %{_libdir}/rygel-1.0/
%{_libdir}/rygel-1.0/librygel-gst-launch.so
%{_libdir}/rygel-1.0/librygel-external.so
%{_libdir}/rygel-1.0/librygel-mediathek.so
%{_libdir}/rygel-1.0/librygel-mpris.so
%{_libdir}/rygel-1.0/librygel-playbin.so
%{_libdir}/rygel-1.0/librygel-test.so
%{_datadir}/rygel/
%{_datadir}/applications/rygel*
%{_iconsdir}/*/*/*/*
%{_mandir}/man?/*
%{_datadir}/dbus-1/services/org.gnome.Rygel1.service

%files tracker
%{_libdir}/rygel-1.0/librygel-tracker.so

%files devel
%{_includedir}/rygel-1.0/
%{_libdir}/pkgconfig/rygel-1.0.pc
%{_datadir}/vala/vapi/rygel-1.0.deps
%{_datadir}/vala/vapi/rygel-1.0.vapi
