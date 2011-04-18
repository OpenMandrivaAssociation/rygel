Name:           rygel
Version:        0.8.3
Release:        %mkrel 1
Summary:        A UPnP v2 Media Server
Group:          Sound
License:        LGPLv2+
URL:            http://live.gnome.org/Rygel
Source0:        ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/0.4/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: dbus-glib-devel
BuildRequires: libgstreamer-devel >= 0.10.28
BuildRequires: gtk2-devel
BuildRequires: gupnp-devel >= 0.13.4
BuildRequires: gupnp-av-devel >= 0.5.9
BuildRequires: gupnp-dlna-devel >= 0.3
BuildRequires: gupnp-vala >= 0.6.11
BuildRequires: libgee-devel >= 0.5
BuildRequires: libsoup-devel >= 2.26.0
BuildRequires: libuuid-devel >= 1.41.3
BuildRequires: libxml2-devel
BuildRequires: sqlite3-devel >= 3.5
BuildRequires: vala-devel >= 0.9.5
BuildRequires: vala-tools
BuildRequires: intltool

%description
Rygel is an implementation of the UPnP MediaServer V 2.0 specification that is 
specifically designed for GNOME. It is based on GUPnP and is written (mostly) 
in Vala language. The project was previously known as gupnp-media-server. 

%package devel
Summary: Development package for %{name}
Group: Development/Other
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
Files for development with %{name}.

%package tracker
Summary: Tracker plugin for %{name}
Group: Sound
Requires: %{name} = %{version}-%{release}
Requires: tracker

%description tracker
A plugin for rygel to use tracker to locate media on the local machine.

%prep
%setup -q

%build
%configure2_5x --enable-tracker-plugin --disable-media-export-plugin --enable-external-plugin --enable-mediathek-plugin --disable-silent-rules 
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %name

#Remove libtool archives.
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%clean
rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README TODO NEWS
%config(noreplace) %{_sysconfdir}/rygel.conf
%{_bindir}/rygel
%{_bindir}/rygel-preferences
%dir %{_libdir}/rygel-1.0
%{_libdir}/rygel-1.0/librygel-external.so
%{_libdir}/rygel-1.0/librygel-mediathek.so
%{_libdir}/rygel-1.0/librygel-mpris.so
%{_libdir}/rygel-1.0/librygel-playbin.so
%{_datadir}/rygel
%{_datadir}/applications/rygel*
%{_iconsdir}/*/*/*/*
%{_mandir}/man?/*
%{_datadir}/dbus-1/services/org.gnome.Rygel1.service

%files tracker
%defattr(-,root,root,-)
%{_libdir}/rygel-1.0/librygel-media-tracker.so

%files devel
%defattr(-,root,root,-)
%{_includedir}/rygel-1.0
%{_libdir}/pkgconfig/rygel-1.0.pc
%{_datadir}/vala/vapi/rygel-1.0.deps
%{_datadir}/vala/vapi/rygel-1.0.vapi

