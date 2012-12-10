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
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

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


%changelog
* Fri May 06 2011 Funda Wang <fwang@mandriva.org> 2.0.3-2mdv2011.0
+ Revision: 669831
- rebuild

* Tue Apr 26 2011 Funda Wang <fwang@mandriva.org> 2.0.3-1
+ Revision: 659359
- br gtk
- new verrsion 2.0.3

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.1-3mdv2011.0
+ Revision: 611141
- rebuild

* Mon Apr 26 2010 Funda Wang <fwang@mandriva.org> 2.0.1-2mdv2010.1
+ Revision: 538923
- rebuild

* Wed Apr 14 2010 Funda Wang <fwang@mandriva.org> 2.0.1-1mdv2010.1
+ Revision: 534690
- update file list
- fix tarball dir
- New version 2.0.1

* Sun Mar 28 2010 Funda Wang <fwang@mandriva.org> 2.0-1mdv2010.1
+ Revision: 528583
- BR intltool
- import ibus-sunpinyin


