Name:       libxrandr
Summary:    X.Org X11 libXrandr runtime library
Version:    1.3.1
Release:    2.6
Group:      System/Libraries
License:    MIT
URL:        http://www.x.org/
Source0:    http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(randrproto) >= 1.3
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xorg-macros)


%description
Xorg libXrandr runtime library


%package devel
Summary:    Development components for the libXrandr library
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   libxrender-devel

%description devel
Xorg libXrandr development package


%prep
%setup -q -n %{name}-%{version}


%build
export LDFLAGS+=" -Wl,--hash-style=both -Wl,--as-needed"
%reconfigure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install




%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig





%files
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/libXrandr.so.2
%{_libdir}/libXrandr.so.2.2.0


%files devel
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog
%dir %{_includedir}/X11
%dir %{_includedir}/X11/extensions
%{_includedir}/X11/extensions/Xrandr.h
%{_libdir}/libXrandr.so
%{_libdir}/pkgconfig/xrandr.pc
%doc %{_mandir}/man3/*.3*

