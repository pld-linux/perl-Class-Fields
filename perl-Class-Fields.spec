#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	Fields
Summary:	Class::Fields - inspect the fields of a class
Summary(pl):	Class::Fields - dogl±danie sk³adowych klasy
Name:		perl-Class-Fields
Version:	0.201
Release:	4
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c4fbfdfa1219742dd971ab731ba26c2e
BuildRequires:	perl-Carp-Assert
BuildRequires:	perl(base) >= 2.0
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl(base) >= 2.0
Requires:	perl-base >= 1:5.8.1
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
rm t/bugs.t	# expected warning has changed; try to remove it after 0.201

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/%{pnam}.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{perl_vendorlib}/*.pm
%{_mandir}/man3/*
