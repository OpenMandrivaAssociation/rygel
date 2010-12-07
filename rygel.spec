# (cg) It doesn't like to dbus properly... I know I should fix properly but it's late.... :p
%define _disable_ld_as_needed 1

Name:           rygel
Version:        0.4.12
Release:        %mkrel 2
Summary:        A UPnP v2 Media Server
Group:          Sound
License:        LGPLv2+
URL:            http://live.gnome.org/Rygel
Source0:        ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/0.4/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: dbus-glib-devel
BuildRequires: desktop-file-utils
BuildRequires: libgstreamer-devel
BuildRequires: gtk2-devel
BuildRequires: gupnp-devel
BuildRequires: gupnp-av-devel
BuildRequires: gupnp-vala
BuildRequires: libgee-devel >= 0.5
BuildRequires: libsoup-devel
BuildRequires: libuuid-devel
BuildRequires: sqlite-devel
BuildRequires: vala-devel
BuildRequires: vala-tools

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
%configure2_5x --enable-tracker-plugin --enable-media-export-plugin --enable-external-plugin --enable-mediathek-plugin --enable-gstlaunch-plugin --disable-silent-rules 
%make

%install
rm -rf %{buildroot}
%makeinstall_std

#Remove libtool archives.
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# Verify the desktop files
desktop-file-validate %{buildroot}/%{_datadir}/applications/rygel.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/rygel-preferences.desktop

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README TODO NEWS
%config(noreplace) %{_sysconfdir}/rygel.conf
%{_bindir}/rygel
%{_bindir}/rygel-preferences
%{_libdir}/rygel-1.0/librygel-external.so
%{_libdir}/rygel-1.0/librygel-media-export.so
%{_libdir}/rygel-1.0/librygel-mediathek.so
%{_libdir}/rygel-1.0/librygel-gst-renderer.so
%{_datadir}/rygel/
%{_datadir}/applications/rygel*
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

