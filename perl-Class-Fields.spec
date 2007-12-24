#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Class
%define		pnam	Fields
Summary:	Class::Fields - inspect the fields of a class
Summary(pl.UTF-8):	Class::Fields - doglądanie składowych klasy
Name:		perl-Class-Fields
Version:	0.203
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Class/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fd91cb4bb99825e75fa646501e1cb621
URL:		http://search.cpan.org/dist/Class-Fields/
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

%description -l pl.UTF-8
Zestaw funkcji i metod narzędziowych do sprawdzania składowych
klasy. Dają przyjemny, wysokopoziomowy interfejs, który powinien
wytrzymać próbę czasu i uaktualnienia Perla.

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
