Summary: X.Org X11 libXrandr runtime library
Name: libXrandr
Version: 1.4.2
Release: 3
License: MIT
Group: System Environment/Libraries
URL: http://www.x.org

Source0: %{name}-%{version}.tar.gz

BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xproto)
BuildRequires: pkgconfig(randrproto) >= 1.3.0
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(xext)

%description
X.Org X11 libXrandr runtime library

%package devel
Summary: X.Org X11 libXrandr development package
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Provides: libxrandr-devel

%description devel
X.Org X11 libXrandr development package

%prep
%setup -q

%build
%reconfigure  --disable-static \
	       LDFLAGS="${LDFLAGS} -Wl,--hash-style=both -Wl,--as-needed"
make %{?jobs:-j%jobs}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/share/license
cp -af COPYING %{buildroot}/usr/share/license/%{name}
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%remove_docs

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
/usr/share/license/%{name}
%doc AUTHORS COPYING
%{_libdir}/libXrandr.so.2
%{_libdir}/libXrandr.so.2.2.0

%files devel
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/Xrandr.h
%{_libdir}/libXrandr.so
%{_libdir}/pkgconfig/xrandr.pc
#%dir %{_mandir}/man3x
#%{_mandir}/man3/*.3*