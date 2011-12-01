Name:      ibus-sunpinyin
Summary:   A statistical language model based Chinese input method
Version:   2.0.3
Release:   %mkrel 2
Group:     System/Internationalization
License:   LGPLv2+
URL:       http://code.google.com/p/sunpinyin
Source0:   http://sunpinyin.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ibus-devel >= 1.3.9-5
BuildRequires:	sqlite3-devel
BuildRequires:	glib2-devel
BuildRequires:	intltool >= 0.35.0
BuildRequires:	sunpinyin-devel >= %version
BuildRequires:	gtk+2-devel
BuildRequires:	cmake
Requires:	ibus >= 1.2.0
Requires(post,preun): GConf2

%description
SunPinyin is a statistical language model based Chinese input method,
which was firstly developed by Sun Beijing Globalization team, and
opensource'd to community with opensolaris project, with LGPLv2 and
CDDL dual-licenses. 

SunPinyin had been ported to various input method platforms and
operating systems. The 2.0 release currently supports iBus, XIM, and
Mac OS X.

%prep
%setup -q

%build
%cmake -DLIBEXEC_DIR=%{_libexecdir}
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%find_lang %name

%clean
rm -rf %{buildroot}

%post
%post_ibus_register_engine sunpinyin zh_CN

%preun
%preun_ibus_unregister_engine sunpinyin

%files -f %name.lang
%defattr(-,root,root)
%{_datadir}/%name
%{_datadir}/ibus/component/sunpinyin.xml
%{_libexecdir}/ibus-engine-sunpinyin
%{_libexecdir}/ibus-setup-sunpinyin
