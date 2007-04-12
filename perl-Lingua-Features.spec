%define module	Lingua-Features
%define name	perl-%{module}
%define version 0.3.1
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Natural languages features
License:	GPL or Artistic
Group:		Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Lingua/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
Buildrequires:	perl-XML-Generator
Buildrequires:	perl-List-Compare
Buildrequires:  perl-Tie-IxHash
Buildarch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This module implements natural languages features in Perl. Its brings the
following advantages:
- type verification
- features and values normalization
- smart comparisons between structures


%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
make test

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc ChangeLog README
%{perl_vendorlib}/Lingua
%{_mandir}/*/*

