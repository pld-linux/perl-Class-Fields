#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Class
%define		pnam	Fields
Summary:	Class::Fields - inspect the fields of a class
Summary(pl):	Class::Fields - dogl±danie sk³adowych klasy
Name:		perl-Class-Fields
Version:	0.16
Release:	1
License:	?
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0f62dd9e464f357eab2d6c75e65aa7c6
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	perl-Carp-Assert
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A collection of utility functions/methods for examining the data
members of a class. It provides a nice, high-level interface that
should stand the test of time and Perl upgrades nicely.

%description -l pl
Zestaw funkcji i metod narzêdziowych do sprawdzania sk³adowych
klasy. Daj± przyjemny, wysokopoziomowy interfejs, który powinien
wytrzymaæ próbê czasu i uaktualnienia Perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=site \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/%{pnam}.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{perl_vendorlib}/*.pm
%{_mandir}/man3/*
