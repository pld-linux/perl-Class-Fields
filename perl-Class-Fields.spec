%include	/usr/lib/rpm/macros.perl
%define		pdir	Class
%define		pnam	Fields
Summary:	%{pdir}::%{pnam} perl module
Summary(cs):	Modul %{pdir}::%{pnam} pro Perl
Summary(da):	Perlmodul %{pdir}::%{pnam}
Summary(de):	%{pdir}::%{pnam} Perl Modul
Summary(es):	Módulo de Perl %{pdir}::%{pnam}
Summary(fr):	Module Perl %{pdir}::%{pnam}
Summary(it):	Modulo di Perl %{pdir}::%{pnam}
Summary(ja):	%{pdir}::%{pnam} Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	%{pdir}::%{pnam} ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul %{pdir}::%{pnam}
Summary(pl):	Modu³ perla %{pdir}::%{pnam}
Summary(pt_BR):	Módulo Perl %{pdir}::%{pnam}
Summary(pt):	Módulo de Perl %{pdir}::%{pnam}
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl %{pdir}::%{pnam}
Summary(sv):	%{pdir}::%{pnam} Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl %{pdir}::%{pnam}
Summary(zh_CN):	%{pdir}::%{pnam} Perl Ä£¿é
Name:		perl-Class-Fields
Version:	0.14
Release:	1
License:	?
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-Carp-Assert
BuildRequires:	rpm-perlprov >= 3.0.3-16
Conflicts:	perl <= 5.6.1-45
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
perl Makefile.PL
%{__make}
#%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_privlib}/%{pdir}/%{pnam}.pm
%{perl_privlib}/%{pdir}/%{pnam}
%{perl_privlib}/*.pm
%{_mandir}/man3/*
