#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Class
%define		pnam	Fields
Summary:	Class::Fields - Inspect the fields of a class
Summary(pl):	Class::Fields - Dogl�danie sk�adowych klasy
Name:		perl-Class-Fields
Version:	0.15
Release:	3
License:	?
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	536ba4dd740c1ceb30e322db98b6f0b6
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-Carp-Assert
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# needed only for perl >= 5.9
%define		_noautoreq	'perl(Hash::Util)'

%description
A collection of utility functions/methods for examining the data
members of a class. It provides a nice, high-level interface that
should stand the test of time and Perl upgrades nicely.

%description -l pl
Zestaw funkcji i metod narz�dziowych do sprawdzania sk�adowych
klasy. Daj� przyjemny, wysokopoziomowy interfejs, kt�ry powinien
wytrzyma� pr�b� czasu i uaktualnienia Perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=site
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/%{pnam}.pm
%{perl_sitelib}/%{pdir}/%{pnam}
%{perl_sitelib}/*.pm
%{_mandir}/man3/*
