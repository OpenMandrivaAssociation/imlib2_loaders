Summary: Additional image loaders for Imlib2
Name: imlib2_loaders
Version: 1.12.2
Release: 1
License: Distributable
Group: System/Libraries
Source0: https://sourceforge.net/projects/enlightenment/files/imlib2-src/%{version}/imlib2_loaders-%{version}.tar.xz
URL: https://www.enlightenment.org/pages/imlib2.html

Buildrequires: pkgconfig(imlib2) 
BuildRequires: libltdl-devel
Requires: imlib2 

%description
This package contains additional image loaders for Imlib2,
which for some reason (such as license issues, Imlib2 is BSD licensed, see 
README inside) are not distributed with Imlib2 directly.

%prep
%autosetup -p1

%build
./autogen.sh
%make_build

%install
%make_install

%files
%defattr(-,root,root) 
%doc AUTHORS COPYING* 
%_libdir/imlib2/loaders/*


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.2-0.20060103.3mdv2011.0
+ Revision: 619624
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.1.2-0.20060103.2mdv2010.0
+ Revision: 429507
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.1.2-0.20060103.1mdv2009.0
+ Revision: 140776
- restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.1.2-0.20060103.1mdv2008.1
+ Revision: 127040
- kill re-definition of %%buildroot on Pixel's request
- Import imlib2_loaders



* Tue Jan 03 2006 Lenny Cartier <lenny@mandriva.com> 1.1.2-0.20060103.1mdk
- 1.1.2 20060103

* Mon Sep 13 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.1.2-0.20040913.1mdk
- 1.1.2 20040913

* Thu Jul 31 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.0.4-0.20030730.2mdk
- fix requires

* Thu Jul 31 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.0.4-0.20030730.1mdk
- 20030730

* Thu Jun 26 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.0.4-0.20030624.1mdk
- new

* Sun Aug 12 2001 Tom Gilbert <tom@linuxbrit.co.uk>
- Added db loader.

* Sat Aug 11 2001 Mark Bainter <mark-e@cymry.org>
- Corrected web URL.  
- Changed Copyright to mixed, since not all items
  in this package will be BSD Licensed.

* Wed Jul 04 2001 Mark Bainter <mark-e@cymry.org>
- Corrected ftp location.

* Wed Jun 28 2001 Mark Bainter <mark-e@cymry.org>
- Made package relocateable.

* Wed Jun 13 2001 Mark Bainter <mark-e@cymry.org>
- Cleanup and adjustments to reflect new ownership

* Tue May 22 2001 Christian Kreibich <cK@whoop.org>
- Initial spec file
