%define module	Lingua-Features

Name:		perl-%{module}
Version:	0.3.1
Release:	8
Summary:	Natural languages features
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Lingua/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl(XML::Generator)
BuildRequires:	perl(List::Compare)
BuildRequires:	perl(Tie::IxHash)
BuildArch:	noarch

%description
This module implements natural languages features in Perl. Its brings the
following advantages:
- type verification
- features and values normalization
- smart comparisons between structures

%prep
%setup -q -n %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
make test

%files 
%doc ChangeLog README
%{perl_vendorlib}/Lingua
%{_mandir}/*/*

%changelog
* Sun Feb 28 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.1-5mdv2010.1
+ Revision: 512695
- package restoration

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.3.1-5mdv2010.0
+ Revision: 430478
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.3.1-4mdv2009.0
+ Revision: 241606
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.1-2mdv2008.0
+ Revision: 86520
- rebuild


* Tue Sep 05 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.1-1mdv2007.0
- new version

* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.3-5mdv2007.0
- Rebuild

* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.3-4mdk
- fix buildrequires

* Sat Jun 11 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.3-3mdk 
- don't ship useless empty dirs
- better url
- spec cleanup
- make test in %%check

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.3-2mdk
- fix buildrequires in a backward compatible way

* Fri Jun 11 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.3-1mdk 
- new version
- update description

* Wed Apr 21 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.2-1mdk
- new version
- rpmbuildupdate aware

* Thu Apr 15 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.1-1mdk
- first mdk release

