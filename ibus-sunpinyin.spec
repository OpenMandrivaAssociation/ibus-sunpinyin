Summary:	A statistical language model based Chinese input method
Name:		ibus-sunpinyin
Version:	2.0.3
Release:	5
License:	LGPLv2+
Group:		System/Internationalization
Url:		http://code.google.com/p/sunpinyin
Source0:	http://sunpinyin.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:		ibus-sunpinyin-2.0.3-ibus-1.4.patch
BuildRequires:	cmake
BuildRequires:	intltool
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(ibus-1.0)
BuildRequires:	pkgconfig(pangoxft)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(sunpinyin-2.0) >= %{version}
Requires:	ibus

%description
SunPinyin is a statistical language model based Chinese input method,
which was firstly developed by Sun Beijing Globalization team, and
opensource'd to community with opensolaris project, with LGPLv2 and
CDDL dual-licenses.

SunPinyin had been ported to various input method platforms and
operating systems. The 2.0 release currently supports iBus, XIM, and
Mac OS X.

%files -f %{name}.lang
%{_datadir}/%{name}
%{_datadir}/ibus/component/sunpinyin.xml
%{_libexecdir}/ibus-engine-sunpinyin
%{_libexecdir}/ibus-setup-sunpinyin

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0

%build
%cmake -DLIBEXEC_DIR=%{_libexecdir}
%make

%install
%makeinstall_std -C build

%find_lang %name

