%define api 1.0
%define major 0
%define libname %mklibname %{name} %{api} %{major}

%define url_ver %(echo %{version} | cut -d. -f1,2)

Name:		rygel
Version:	0.16.3
Release:	%mkrel 1
Summary:	A UPnP v2 Media Server
Group:		Sound
License:	LGPLv2+
URL:		http://live.gnome.org/Rygel
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	pkgconfig(gee-1.0) >= 0.5.2
BuildRequires:	pkgconfig(gio-2.0) >= 2.26
BuildRequires:	pkgconfig(gssdp-1.0) >= 0.11.0
BuildRequires:	pkgconfig(gssdp-1.0) <= 0.12.9999
BuildRequires:	pkgconfig(gstreamer-0.10) >= 0.10.35
BuildRequires:	pkgconfig(gstreamer-app-0.10) >= 0.10.28
BuildRequires:	pkgconfig(gstreamer-base-0.10) >= 0.10.35
BuildRequires:	pkgconfig(gstreamer-pbutils-0.10) >= 0.10.35
BuildRequires:	pkgconfig(gstreamer-tag-0.10) >= 0.10.28
BuildRequires:	pkgconfig(gtk+-3.0) >= 2.90.3
BuildRequires:	pkgconfig(gupnp-1.0) >= 0.17.1
BuildRequires:	pkgconfig(gupnp-av-1.0) >= 0.9.0
BuildRequires:	pkgconfig(gupnp-dlna-1.0) >= 0.5.0
BuildRequires:	pkgconfig(gupnp-vala-1.0) >= 0.10.2
BuildRequires:	pkgconfig(libsoup-2.4) >= 2.34.0
BuildRequires:	pkgconfig(sqlite3) >= 3.5
BuildRequires:	pkgconfig(tracker-sparql-0.14)
BuildRequires:	pkgconfig(uuid) >= 1.41.3
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

%package -n %{libname}
Summary:	Shared libraries for %{name}
Group:		System/Libraries

%description -n %{libname}
Shared libraries for %{name}.

%package devel
Summary:	Development package for %{name}
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

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

%files -n %{libname}
%{_libdir}/lib*-%{api}.so.%{major}
%{_libdir}/lib*-%{api}.so.%{major}.*

%files devel
%{_libdir}/*.so
%{_includedir}/rygel-1.0/
%{_libdir}/pkgconfig/rygel-core-1.0.pc
%{_libdir}/pkgconfig/rygel-renderer-1.0.pc
%{_libdir}/pkgconfig/rygel-server-1.0.pc
%{_datadir}/vala/vapi/*


%changelog

* Tue Nov 13 2012 fwang <fwang> 0.16.3-1.mga3
+ Revision: 317519
- new version 0.16.3

* Tue Nov 13 2012 fwang <fwang> 0.16.2-1.mga3
+ Revision: 317506
- update file list
- update rpm group
- new version 0.16.2

  + ovitters <ovitters>
    - new version 0.16.1

* Tue Sep 25 2012 ovitters <ovitters> 0.16.0-1.mga3
+ Revision: 297666
- new version 0.16.0

* Tue Sep 18 2012 ovitters <ovitters> 0.15.4-1.mga3
+ Revision: 295672
- new version 0.15.4

* Tue Sep 04 2012 ovitters <ovitters> 0.15.3-1.mga3
+ Revision: 287968
- new version 0.15.3

* Wed Aug 29 2012 fwang <fwang> 0.15.2-1.mga3
+ Revision: 285522
- update file list

  + ovitters <ovitters>
    - new version 0.15.2
    - update file list
    - br tracker-vala
    - br tracker-sparql-0.14
    - spec file: only tabs, not mix of spaces and tabs
    - new version 0.15.1

* Wed Jun 27 2012 ovitters <ovitters> 0.15.0.1-1.mga3
+ Revision: 264513
- new version 0.15.0.1

* Wed Jun 13 2012 ovitters <ovitters> 0.14.2-1.mga3
+ Revision: 260396
- new version 0.14.2

* Sat Apr 28 2012 ovitters <ovitters> 0.14.1-1.mga3
+ Revision: 234140
- new version 0.14.1

* Mon Apr 02 2012 fwang <fwang> 0.14.0-2.mga2
+ Revision: 227747
- drop max version requires
- drop unused br

* Mon Mar 26 2012 ovitters <ovitters> 0.14.0-1.mga2
+ Revision: 226745
- new version 0.14.0

* Mon Mar 19 2012 ovitters <ovitters> 0.13.4-1.mga2
+ Revision: 224497
- new version 0.13.4

* Fri Mar 09 2012 fwang <fwang> 0.13.3-1.mga2
+ Revision: 221988
- new version 0.13.3

* Thu Feb 23 2012 fwang <fwang> 0.13.2-1.mga2
+ Revision: 212467
- new version 0.13.2

* Sat Feb 11 2012 fwang <fwang> 0.13.1-2.mga2
+ Revision: 207130
- there is no dep on gconf now

* Sat Feb 11 2012 fwang <fwang> 0.13.1-1.mga2
+ Revision: 207125
- new version 0.13.1

* Thu Nov 24 2011 fwang <fwang> 0.13.0-1.mga2
+ Revision: 171532
- add br
- new version 0.13.0

* Sat Oct 22 2011 wally <wally> 0.12.5-1.mga2
+ Revision: 157334
- new version 0.12.5

* Sat Oct 08 2011 wally <wally> 0.12.4-1.mga2
+ Revision: 153371
- new version 0.12.4

* Tue Sep 27 2011 wally <wally> 0.12.3-2.mga2
+ Revision: 149580
- add requires

* Tue Sep 27 2011 wally <wally> 0.12.3-1.mga2
+ Revision: 149543
- new version 0.12.3
- enable more plugins
- clean .spec a bit
- imported package rygel

