Name:      ibus-sunpinyin
Summary:   A statistical language model based Chinese input method
Version:   2.0.1
Release:   %mkrel 1
Group:     System/Internationalization
License:   LGPLv2+
URL:       http://code.google.com/p/sunpinyin
Source0:   http://sunpinyin.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ibus-devel >= 1.2.0
BuildRequires:	sqlite3-devel
BuildRequires:	glib2-devel
BuildRequires:	intltool >= 0.35.0
Requires:	ibus >= 1.2.0

%description
SunPinyin is a statistical language model based Chinese input method,
which was firstly developed by Sun Beijing Globalization team, and
opensource'd to community with opensolaris project, with LGPLv2 and
CDDL dual-licenses. 

SunPinyin had been ported to various input method platforms and
operating systems. The 2.0 release currently supports iBus, XIM, and
Mac OS X.

%prep
%setup -q -n sunpinyin-2.0

%build
%configure2_5x --enable-ibus
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang sunpinyin2

%clean
rm -rf $RPM_BUILD_ROOT

%files -f sunpinyin2.lang
%defattr(-,root,root)
%{_datadir}/%name
%{_datadir}/sunpinyin
%{_datadir}/ibus/component/sunpinyin.xml
%{_libexecdir}/ibus-engine-sunpinyin
%{_libexecdir}/ibus-setup-sunpinyin
